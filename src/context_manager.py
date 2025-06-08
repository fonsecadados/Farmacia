from models import Conversation, Product
import json
import spacy
import re
from nltk.tokenize import word_tokenize


nlp = spacy.load("pt_core_news_sm")

with open(r'C:\Users\syafo\VIX_Intelligence\Farmacia\json\sintomas_med.json', 'r', encoding='utf-8') as f:
    known_symptoms = json.load(f)

class ContextManager:
    """Gerenciador de contexto para fluxos de conversação"""
    
    CONTEXT_TYPES = {
        'NONE': 'none',
        'ASKING_MEDICINE_INFO': 'asking_medicine_info',
        'CHECKING_STOCK': 'checking_stock',
        'WAITING_SYMPTOM': 'waiting_symptom',
        'CONFIRMING_ORDER': 'confirming_order',
        'HUMAN': 'human',
        'MAIN_MENU': 'main_menu',
        'FAQ' : 'faq'
    }
    
    @staticmethod
    def get_current_context(user_id, platform):
        context = Conversation.get_context(user_id, platform)
        if not context:
            return {'type': ContextManager.CONTEXT_TYPES['NONE'], 'data': {}}
        return context
    
    @staticmethod
    def set_context(user_id, platform, context_type, context_data=None):
        if context_type not in ContextManager.CONTEXT_TYPES.values():
            raise ValueError(f"Tipo de contexto inválido: {context_type}")
        Conversation.set_context(user_id, platform, context_type, context_data or {})
    
    @staticmethod
    def clear_context(user_id, platform):
        Conversation.clear_context(user_id, platform)
        
    @staticmethod
    def detectar_sintoma_spacy(texto_usuario, known_symptoms):
        doc = nlp(texto_usuario.lower())
        texto_processado = " ".join([token.lemma_ for token in doc])

        sintomas_detectados = set()

        for sintoma, info in known_symptoms.items():
            if sintoma in texto_processado:
                sintomas_detectados.add(sintoma)
                for sinonimo in info.get("sinonimos", []):
                    if sinonimo in texto_processado:
                        sintomas_detectados.add(sintoma)

        return list(sintomas_detectados) if sintomas_detectados else None

    @staticmethod
    def process_in_context(user_id, platform, message_text, nlp_result):
        current_context = ContextManager.get_current_context(user_id, platform)
        context_type = current_context.get('type', ContextManager.CONTEXT_TYPES['NONE'])
        context_data = current_context.get('data', {})
        
        if context_type == ContextManager.CONTEXT_TYPES['NONE']:
            return None, None, None
        
        if context_type == ContextManager.CONTEXT_TYPES['ASKING_MEDICINE_INFO']:
            medicine_name = context_data.get('medicine_name')
            if nlp_result['intent'] in ['despedida', 'ajuda']:
                return None, ContextManager.CONTEXT_TYPES['NONE'], None

            product = Product.find_by_name(medicine_name)

            if product:
                response = (
                    f"Aqui estão as informações sobre {product['name']}:\n\n"
                    f"- Indicação: {product.get('indicacao', 'Não informado')}\n"
                    f"- Posologia: {product.get('posologia', 'Não informado')}\n"
                    f"- Efeitos colaterais: {product.get('efeitos_colaterais', 'Não informado')}\n"
                    f"- Contraindicações: {product.get('contraindicacoes', 'Não informado')}\n\n"
                    "Posso ajudar com mais alguma informação sobre este medicamento?"
                )
            else:
                response = f"Desculpe, não encontrei informações sobre '{medicine_name}'. Você pode verificar o nome ou tentar outro medicamento?"
            
            return response, context_type, context_data
        
        elif context_type == ContextManager.CONTEXT_TYPES['CHECKING_STOCK']:
            product_name = context_data.get('product_name')
            if nlp_result['intent'] in ['despedida', 'ajuda']:
                ContextManager.clear_context(user_id, platform)
                return None, ContextManager.CONTEXT_TYPES['NONE'], None
            
            response = (
                f"Verificamos e temos {product_name} disponível em estoque!\n"
                "Deseja saber o preço ou mais informações sobre este produto?"
            )
            return response, context_type, context_data
                        
        elif context_type == ContextManager.CONTEXT_TYPES['WAITING_SYMPTOM']:

            def check_symptom_severity(symptom_text):
                severe_patterns = [
                    r"\b41\s*graus\b", r"\b40\s*graus\b", r"\bfebre alta\b",
                    r"\bdor (muito )?forte\b", r"\bdor insuportável\b",
                    r"\bdesmaio\b", r"\bsangramento\b", r"\bdificuldade para respirar\b",
                    r"\bperda de consciência\b", r"\bconfusão mental\b", r"\bparalisia\b"
                ]
                symptom_text = symptom_text.lower()
                for pattern in severe_patterns:
                    if re.search(pattern, symptom_text):
                        return True
                return False

            symptom = message_text.strip().lower()

            if check_symptom_severity(symptom):
                response = (
                    "⚠️ ATENÇÃO ⚠️\n\n"
                    "SEUS SINTOMAS INDICAM UMA CONDIÇÃO POSSIVELMENTE GRAVE.\n\n"
                    "RECOMENDAMOS PROCURAR O ATENDIMENTO MÉDICO MAIS PRÓXIMO DA SUA REGIÃO.\n\n"
                    "Quer conversar com um dos nossos farmacêuticos? \n\n ✅ Digite SIM para ser redirecionado\n\n "
                    "❌ DIgitie NÃO para continuar com a ajuda automatizada.\n\n"
                    "Estamos aqui para atendê-lo(a) da melhor maneira."
                )
                return response, ContextManager.CONTEXT_TYPES['HUMAN'], None

            matched_symptom = ContextManager.detectar_sintoma_spacy(symptom, known_symptoms)

            if matched_symptom:
                response = ""
                for sintoma in matched_symptom:
                    medicamentos = known_symptoms.get(sintoma, {}).get('medicamentos', [])

                    if not medicamentos:
                        response += f"⚠️ Nenhum medicamento sugerido para o sintoma: *{sintoma}*\n\n"
                        continue

                    response += f" Para o sintoma {sintoma}, posso sugerir:\n\n"

                    for i, med_name in enumerate(medicamentos, 1):
                        product = Product.get_product_by_name(med_name)
                        if product:
                            description = product.get('description', 'Sem descrição disponível.')
                            manufacturer = product.get('manufacturer', 'Desconhecido')
                            price = product.get('price', 'N/A')
                            administration = product.get('administration_route', 'Via não informada')
                        else:
                            description = 'Medicamento não encontrado no banco de dados.'
                            manufacturer = 'Desconhecido'
                            price = 'N/A'
                            administration = 'Via não informada'

                        response += (
                            f"🔹\n\n"
                            f"{i}. {med_name.upper()} - {description}\n\n"
                        )

                    response += "────────────\n\n"

                response += (
                    "⚠️ ATENÇÃO ⚠️\n\n"
                    "Não indicamos a automedicação.\n"
                    "Para Dosagem e valores, favor falar com um de nossos atendentes\n\n"
                    "Digite 1️⃣ para ser redirecionado\n"
                    "Digite 0️⃣ para ser redirecionado\n"
                )

                return response, ContextManager.CONTEXT_TYPES['NONE'], None


            else:
                response = (
                    "Desculpe, não entendi. Por favor, escreva um **SINTOMA** válido.\n"
                    "Exemplos: *dor de cabeça*, *febre*, *tosse*, *náusea*..."
                )
                return response, ContextManager.CONTEXT_TYPES['WAITING_SYMPTOM'], context_data
            
        elif context_type == ContextManager.CONTEXT_TYPES['FAQ']:
            from models import FAQ  # coloque no topo do arquivo se preferir
            numero = message_text.strip()

            if numero == "0":
                return (
                    "Você voltou ao menu principal. Como posso te ajudar hoje?",
                    ContextManager.CONTEXT_TYPES['MAIN_MENU'],
                    {}
                )

            all_faqs = FAQ.get_all()  # Retorna todas as FAQs em ordem

            try:
                idx = int(numero) - 1
                if 0 <= idx < len(all_faqs):
                    faq = all_faqs[idx]
                    return (
                        f"❓ *{faq['question']}*\n\n💬 {faq['answer']}",
                        ContextManager.CONTEXT_TYPES['FAQ'],
                        context_data
                    )
                else:
                    return (
                        "❌ Opção inválida. Por favor, digite um número válido ou 0️⃣ para voltar ao menu principal.",
                        ContextManager.CONTEXT_TYPES['FAQ'],
                        context_data
                    )
            except ValueError:
                return (
                    "⚠️ Digite apenas o número da pergunta desejada ou 0️⃣ para retornar.",
                    ContextManager.CONTEXT_TYPES['FAQ'],
                    context_data
                )

        # Redirecionamentos gerais, talvez colocar fora do if context_type
        if message_text.strip().lower() == "sim":
            whatsapp_link = "https://wa.me/5527995239355?text=Olá,%20preciso%20de%20ajuda%20com%20meus%20sintomas"
            response = (
                "✅ Certo! Você será redirecionado para um dos nossos farmacêuticos.\n\n"
                f"Clique aqui para iniciar a conversa pelo WhatsApp:\n\n {whatsapp_link}\n\n"
                "Para reiniciar o atendimento digite VOLTAR"
            )
            return response, ContextManager.CONTEXT_TYPES['NONE'], {"solicitou_atendente": True}

        elif message_text.strip().lower() == "não":
            response = (
                "Tudo bem! Como posso te ajudar agora?\n\n"
                "1️⃣ Relatar novamente os sintomas\n"
                "2️⃣ Retornar ao menu principal"
            )
            return response, ContextManager.CONTEXT_TYPES['NONE'], None

        elif message_text.strip() == "1":
            response = "Claro! Por favor, descreva novamente os sintomas que está sentindo."
            return response, ContextManager.CONTEXT_TYPES['WAITING_SYMPTOM'], None

        elif message_text.strip() == "2":
            response = "Você voltou ao menu principal. Como posso te ajudar hoje?"
            return response, ContextManager.CONTEXT_TYPES['MAIN_MENU'], None

        return None, None, None

from nlp_processor import NLPProcessor
from context_manager import ContextManager
from models import Product, FAQ, Conversation
import json

with open(r'C:\Users\syafo\VIX_Intelligence\Farmacia\json\sintomas_med.json', 'r', encoding='utf-8') as f:
    known_symptoms = json.load(f)

instagram_link = "https://www.instagram.com/xxxxx"
instagram_link_promos = "https://www.instagram.com/xxxxx"

MENU_OPTIONS = {
    '1': (f"🏪 Nossa loja fica em XXXX, n° 123 - XXXX - XX\n\n"
          f"💟 Aqui nós cuidamos de você! 💟\n"
          f"✔️ Funcionamos de Segunda à Sábado de 08h às 22h 🕜\n\n"
          f"📍 Tudo em perfumeria e medicamentos com precinho que cabe no seu bolso! 💲\n\n"
          f"Contamos com vagas de estacionamento para PCD, além de atendimento personalizado!\n\n"
          f"\n"
          f"Visite nossa página no Instagram e fique por dentro das melhores promoções do mercado!"
          f"\n\n"
          f"{instagram_link}\n\n"
          f"Digite 1️⃣ para voltar ao Menu principal\n"
          f"Digite 2️⃣ para ver PROMOÇÕES\n"
         ),
    '2': (f"Bem vindo(a) ao cadastro na Farmácia XXXX!\n\n"
          f"⚠️ Atenção ⚠️\n"
          f"Para continuar com o cadastro é preciso que você aceite a nossa POLÍTICA DE PRIVACIDADE, conforme orientado pela Lei Geral de Proteção aos Dados (LGPD)\n\n"
          f"Acesse:\n"
          f"https:/www.xxxxx.com.br/institucional/politica-de-privacidade\n\n\n"
          f"Digite a opção escolhida:\n\n"
          f"1️⃣ Aceito os termos\n"
          f"2️⃣ Não aceito os termos"
          ),
    '3': (f"🔥 Fique por dentro das PROMOÇÕES da semana na nossa página!\n\n"
          f"{instagram_link_promos}\n\n"
          ),
    '4': ("💬 Entendemos que você está apresentando alguns sintomas.\n\n Fale mais sobre eles para que possamos sugerir uma medicação\n\n"
          "Digite 0️⃣ para voltar ao menu principal"),
    '5': (f"Algumas perguntas Frequentes no nosso canal:\n\n"
          f"Digite o N° para receber resposta:\n\n"
          f"1️⃣ Qual o horário de funcionamento da farmácia?\n\n"
          f"2️⃣ Quais formas de pagamento são aceitas?\n\n"
          f"3️⃣ Vocês fazem entrega?\n\n"
          f"4️⃣ Preciso de receita para comprar antibióticos?\n\n"
          f"5️⃣ Vocês aceitam receitas digitais?\n\n"
          f"6️⃣ Vocês aplicam vacinas na farmácia?\n\n"
          f"7️⃣ Vocês medem pressão arterial e glicose?\n\n"
          f"8️⃣ É possível fazer cadastro para receber promoções?\n\n"
          f"9️⃣ Vocês vendem medicamentos manipulados?\n\n"
          f"1️⃣0️⃣ Posso trocar um produto comprado na farmácia?\n\n"
          f"1️⃣1️⃣ Como funciona o programa de fidelidade da farmácia?\n\n"
          f"1️⃣2️⃣ Vocês possuem estacionamento para clientes?\n\n"
          f"1️⃣3️⃣ Tem desconto para convênios ou planos de saúde?\n\n"
          f"1️⃣4️⃣ Quais são os canais de atendimento da farmácia?\n\n\n"
          f"Digite 0️⃣ para retornar ao menu principal."
          ),
    '6': "🔔 Outras opções: falar com atendente, localização no mapa etc."
}

class ResponseGenerator:
    """Gerador de respostas para o bot de farmácia"""

    @staticmethod
    def get_welcome_message(first_name=None):
        """Retorna a mensagem de boas-vindas personalizada"""
        num_loja = 27999999999
        name_greeting = f", {first_name}" if first_name else ""
        
        return (
            f"👋 Olá{name_greeting}! 👋\n\n"
            "📍 Bem-vindo(a) ao Saúde Virtual📍\n🔹 Seu Farmacêutico Virtual em parceria com a Farmácia XXX 🔹\n\n" 
            "Nosso objetivo é te auxiliar na escolha do medicamento ideal para cada situação.\n\n"
            "Está com algum sintoma? Digite o que você está sentindo que vamos indicar a medicação correta!\n\n"
            "NÃO INDICAMOS MEDICAÇÃO COM PRESCRIÇÃO MÉDICA\n\n\n"
            "OU digite o número da opção:\n\n"
            "1️⃣ Conheça nossa loja e os horários de funcionamento 🏥\n\n"
            "2️⃣ Fazer cadastro na loja 🕜\n\n"
            "3️⃣ Fique por dentro das PROMOÇÕES 💯\n\n"
            "4️⃣ Tenho sintomas, preciso de recomendações 💊\n\n"
            "5️⃣ Perguntas Frequentes ❔\n\n"
            "6️⃣ Sugestões/Reclamações 📢\n\n\n"
            f"Esse é um canal de atendimento automatizado, para falar com vendedor ligue para nossa loja:\n\n"
            f"{num_loja}\n\n"
            "💟 Como podemos te ajudar hoje? 💟"
        )

    @staticmethod
    def _get_main_menu_text():
        """Retorna o texto do menu principal"""
        return ResponseGenerator.get_welcome_message()

    @staticmethod
    def generate_response(user_id, platform, message_text):
        """Gera uma resposta com base na mensagem do usuário e no contexto"""
        Conversation.save_message(user_id, platform, message_text, is_from_user=True)

        opcao = message_text.strip()
        current_context = ContextManager.get_current_context(user_id, platform)

        # Tratamento do submenu da opção '1' (informações da loja)
        if current_context == ContextManager.CONTEXT_TYPES.get('INFO_LOJA_SUBMENU'):
            if opcao == '1':
                ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['MAIN_MENU'], {})
                resposta = ResponseGenerator._get_main_menu_text()
            elif opcao == '2':
                resposta = MENU_OPTIONS['3']
            else:
                resposta = "Por favor, digite 1️⃣ para voltar ao Menu principal ou 2️⃣ para ver PROMOÇÕES."
            
            Conversation.save_message(user_id, platform, resposta, is_from_user=False)
            return resposta

        # Se estiver no menu principal e digitar uma opção numérica
        elif current_context == ContextManager.CONTEXT_TYPES.get('MAIN_MENU') and opcao in MENU_OPTIONS:
            if opcao == '1':
                ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['INFO_LOJA_SUBMENU'], {})
                resposta = MENU_OPTIONS['1']
            elif opcao == '2':
                ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['WAITING_LGPD_RESPONSE'], {})
                resposta = MENU_OPTIONS['2']
            elif opcao == '3':
                resposta = MENU_OPTIONS['3']
            elif opcao == '4':
                ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['WAITING_SYMPTOM'], {})
                resposta = MENU_OPTIONS['4']
            elif opcao == '5':
                ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['FAQ'], {})
                resposta = MENU_OPTIONS['5']
            elif opcao == '6':
                ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['OTHER_OPTIONS'], {})
                resposta = MENU_OPTIONS['6']

            Conversation.save_message(user_id, platform, resposta, is_from_user=False)
            return resposta

        # Tratamento de respostas dentro do contexto WAITING_LGPD_RESPONSE
        elif current_context == ContextManager.CONTEXT_TYPES.get('WAITING_LGPD_RESPONSE'):
            if opcao == '1':
                resposta = "Obrigado por aceitar nossa Política de Privacidade. Agora podemos continuar com seu cadastro."
                ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['MAIN_MENU'], {})
            elif opcao == '2':
                resposta = "Você precisa aceitar a Política de Privacidade para continuar. Caso queira, digite 1️⃣ para aceitar."
            else:
                resposta = "Por favor, digite 1️⃣ para aceitar ou 2️⃣ para recusar a Política de Privacidade."

            Conversation.save_message(user_id, platform, resposta, is_from_user=False)
            return resposta

        # Tratamento do contexto FAQ
        elif current_context == ContextManager.CONTEXT_TYPES.get('FAQ'):
            faq_answers = {
                '1': "Nossa farmácia funciona de segunda à sábado, das 08h às 22h.",
                '2': "Aceitamos dinheiro, cartões de crédito e débito, e PIX.",
                '3': "Sim, fazemos entrega na cidade. Consulte a disponibilidade para sua região.",
                '4': "Sim, antibióticos só vendemos com receita médica.",
                '5': "Sim, aceitamos receitas digitais válidas conforme a legislação.",
                '6': "Sim, aplicamos vacinas contra gripe, covid e outras.",
                '7': "Sim, medimos pressão arterial e glicose gratuitamente.",
                '8': "Sim, você pode se cadastrar para receber nossas promoções via WhatsApp e e-mail.",
                '9': "Não, não trabalhamos com medicamentos manipulados.",
                '10': "Sim, troca de produtos pode ser feita conforme nossa política de trocas em até 7 dias.",
                '11': "Nosso programa de fidelidade oferece descontos e pontos em compras.",
                '12': "Sim, temos estacionamento gratuito para clientes.",
                '13': "Oferecemos descontos para convênios parceiros. Consulte na loja.",
                '14': "Atendemos via telefone, WhatsApp e presencialmente na loja."
            }
            if opcao == '0':
                ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['MAIN_MENU'], {})
                resposta = ResponseGenerator._get_main_menu_text()
            elif opcao in faq_answers:
                resposta = faq_answers[opcao] + "\n\nDigite outro número para mais perguntas ou 0️⃣ para voltar ao menu principal."
            else:
                resposta = "Por favor, digite um número válido das perguntas frequentes ou 0️⃣ para voltar ao menu principal."

            Conversation.save_message(user_id, platform, resposta, is_from_user=False)
            return resposta

        # Contexto de sintomas
        elif current_context == ContextManager.CONTEXT_TYPES.get('WAITING_SYMPTOM'):
            if opcao == '0':
                ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['MAIN_MENU'], {})
                resposta = ResponseGenerator._get_main_menu_text()
            else:
                resposta = f"Você mencionou: {message_text}. Estamos analisando seus sintomas para sugerir um medicamento."
            
            Conversation.save_message(user_id, platform, resposta, is_from_user=False)
            return resposta

        # Verificação de sintomas/medicamentos
        entities = NLPProcessor.get_entities_from_products()
        message_lower = message_text.lower()

        if any(ent.lower() in message_lower for ent in entities['sintomas'] + entities['medicamentos']):
            ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['WAITING_SYMPTOM'], {})
            print('OK até aqui')
            # Agora já processa diretamente
            resposta, new_context_type, context_data = ContextManager.process_in_context(user_id, platform, message_text, {'intent': None})
            if resposta:
                ContextManager.set_context(user_id, platform, new_context_type, context_data or {})
                Conversation.save_message(user_id, platform, resposta, is_from_user=False)
                return resposta

        # Caso padrão - mostrar menu principal
        ContextManager.set_context(user_id, platform, ContextManager.CONTEXT_TYPES['MAIN_MENU'], {})
        resposta = ResponseGenerator._get_main_menu_text()
        Conversation.save_message(user_id, platform, resposta, is_from_user=False)
        return resposta
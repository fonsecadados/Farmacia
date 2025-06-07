from nlp_processor import NLPProcessor
from context_manager import ContextManager
from models import Product, FAQ, Conversation

instagram_link = "https://www.instagram.com/farmes.colina?igsh=dXMwMzAycm9keHlp"
instagram_link_promos = "https://www.instagram.com/s/aGlnaGxpZ2h0OjE4MTA1ODI0OTM1NTE2NTAw?story_media_id=3646291519857893134_3212031575&igsh=MW94YXR5c2F2dHlzbw=="
MENU_OPTIONS = {
    '1':( f"🏪 Nossa loja fica em Colina de Laranjeiras, n° 123 - Serra - ES\n\n"
          f"💟 Aqui nós cuidamos de você! 💟\n"
          f"✔️ Funcionamos de Segunda à Sábado de 08h às 22h 🕜\n\n"
          f"📍 Tudo em perfumeria e medicamentos com precinho que cabe no seu bolso! 💲\n\n"
          f"Contamos com vagas de estacionamento para PCD, além de atendimento parsonalizado!\n\n"
          f"\n"
          f"Visite nossa página no Instagram e fique por dentro das melhores promoções do mercado!"
          f"\n\n"
          f"{instagram_link}\n\n"
          f"Digite 1️⃣ para voltar ao Menu principal\n"
          f"Digite 2️⃣ para ver PROMOÇÔES\n"
         ),
    '2':( f"Bem vindo(a) ao cadastro na REDE Farmes!\n\n"
          f"⚠️ Atenção ⚠️\n"
          f"Para continuar com o cadastro é preciso que você aceite a nossa POLÍTICA DE PRIVACIDADE, conforme orientedo pela Lei Geral de Proteção aos Dados (LGPD)\n\n"
          f"Acesse:\n"
          f"https:/www.redefarmes.com.br/institucional/politica-de-privacidade\n\n\n"
          f"Digite a opção escolhida:\n\n"
          f"1️⃣ Aceito os termos\n"
          f"2️⃣ Não aceito os termos"
          ),
    '3': (f"🔥 Fique por dentro das PROMOÇÔES da semana na nossa página!\n\n"
          f"{instagram_link_promos}\n\n"
          ),
    '4': "💬 Entendi, você está apresentando alguns sintomas. Me diga o que está sentindo para poder te ajudar",
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
    def generate_response(user_id, platform, message_text):
        """Gera uma resposta com base na mensagem do usuário e no contexto"""

        # Salvar a mensagem do usuário
        Conversation.save_message(user_id, platform, message_text, is_from_user=True)

        # Verificar se o usuário digitou uma opção numérica do menu
        opcao = message_text.strip()
        if opcao in MENU_OPTIONS:
            resposta_menu = MENU_OPTIONS[opcao]

            # Se a opção for 4, iniciar contexto de sintomas
            if opcao == '4':
                ContextManager.set_context(
                    user_id,
                    platform,
                    ContextManager.CONTEXT_TYPES['WAITING_SYMPTOM'],
                    {}
                )

            Conversation.save_message(user_id, platform, resposta_menu, is_from_user=False)
            return resposta_menu

        # Analisar o texto com NLP
        nlp_result = NLPProcessor.analyze_text(message_text)

        # Verificar se há um contexto ativo e processar a mensagem nesse contexto
        context_response = ContextManager.process_in_context(user_id, platform, message_text, nlp_result)

        if context_response and context_response[0]:
            response, new_context_type, new_context_data = context_response

            # Atualizar o contexto se necessário
            if new_context_type:
                ContextManager.set_context(user_id, platform, new_context_type, new_context_data)
            elif new_context_type == ContextManager.CONTEXT_TYPES['NONE']:
                ContextManager.clear_context(user_id, platform)

            # Salvar a resposta do bot
            Conversation.save_message(user_id, platform, response, is_from_user=False)
            return response

        # Se não houver contexto ativo ou o contexto não gerou resposta,
        # processar a mensagem normalmente com base na intenção
        intent = nlp_result['intent']
        entities = nlp_result['entities']

        # Gerar resposta com base na intenção
        response = ResponseGenerator._generate_response_by_intent(intent, entities, user_id, platform)

        # Salvar a resposta do bot
        Conversation.save_message(user_id, platform, response, is_from_user=False)
        return response

    @staticmethod
    def _generate_response_by_intent(intent, entities, user_id, platform):
        """Gera uma resposta com base na intenção identificada"""
        
        if intent == 'saudacao':
            return (
                "Olá! Bem-vindo à Farmácia Virtual. Como posso ajudar você hoje? 😊\n\n"
                "Posso fornecer informações sobre medicamentos, verificar disponibilidade de produtos, "
                "informar horários de funcionamento e muito mais."
            )
        
        elif intent == 'despedida':
            return (
                "Obrigado por entrar em contato! Estamos sempre à disposição para ajudar. "
                "Tenha um ótimo dia! 👋"
            )
        
        elif intent == 'agradecimento':
            return (
                "Por nada! Estou aqui para ajudar. Precisa de mais alguma coisa?"
            )
        
        elif intent == 'info_medicamento':
            # Verificar se há medicamentos mencionados
            medicamentos = entities.get('medicamentos', [])
            if medicamentos:#
                medicine_name = medicamentos[0]
                
                # Definir contexto para continuar falando sobre este medicamento
                ContextManager.set_context(
                    user_id, 
                    platform, 
                    ContextManager.CONTEXT_TYPES['ASKING_MEDICINE_INFO'],
                    {'medicine_name': medicine_name}
                )
                
                return (
                    f"Você gostaria de informações sobre {medicine_name}. "
                    f"Estou buscando os detalhes para você..."
                )
            else:
                return (
                    "Qual medicamento você gostaria de saber mais informações? "
                    "Por favor, informe o nome do medicamento."
                )
        
        elif intent == 'preco':
            # Verificar se há medicamentos mencionados
            medicamentos = entities.get('medicamentos', [])
            if medicamentos:
                medicine_name = medicamentos[0]
                
                # Aqui seria implementada a lógica para buscar o preço
                # Por enquanto, apenas simulamos uma resposta
                return f"O preço atual de {medicine_name} é R$ XX,XX. Posso ajudar com mais alguma informação?"
            else:
                return (
                    "Qual produto você gostaria de saber o preço? "
                    "Por favor, informe o nome do produto."
                )
        
        elif intent == 'disponibilidade':
            # Verificar se há medicamentos mencionados
            medicamentos = entities.get('medicamentos', [])
            if medicamentos:
                product_name = medicamentos[0]
                
                # Definir contexto para continuar falando sobre este produto
                ContextManager.set_context(
                    user_id, 
                    platform, 
                    ContextManager.CONTEXT_TYPES['CHECKING_STOCK'],
                    {'product_name': product_name}
                )
                
                return (
                    f"Você gostaria de verificar a disponibilidade de {product_name}. "
                    f"Estou consultando nosso estoque..."
                )
            else:
                return (
                    "Qual produto você gostaria de verificar a disponibilidade? "
                    "Por favor, informe o nome do produto."
                )
        
        elif intent == 'horario':
            return (
                "Nossa farmácia está aberta nos seguintes horários:\n\n"
                "Segunda a Sexta: 08:00 às 20:00\n"
                "Sábados: 08:00 às 18:00\n"
                "Domingos e Feriados: 09:00 às 13:00\n\n"
                "Posso ajudar com mais alguma informação?"
            )
        
        elif intent == 'localizacao':
            return (
                "Nossa farmácia está localizada na Av. Principal, 123 - Centro. \n\n"
                "Referência: Próximo ao Banco do Brasil.\n\n"
                "Você pode nos encontrar facilmente pelo Google Maps pesquisando por 'Farmácia Virtual'."
            )
        
        elif intent == 'ajuda':
            return (
                "Posso ajudar você com:\n\n"
                "- Informações sobre medicamentos\n"
                "- Preços de produtos\n"
                "- Verificação de disponibilidade em estoque\n"
                "- Horários de funcionamento\n"
                "- Localização da farmácia\n"
                "- Recomendações para sintomas\n\n"
                "Como posso te ajudar hoje?"
            )
        
        elif intent == 'falar_humano':
            return (
                "Entendo que você prefere falar com um atendente humano. "
                "Para isso, você pode ligar para nossa central de atendimento no número (XX) XXXX-XXXX "
                "ou enviar um e-mail para atendimento@farmaciavirtual.com.br.\n\n"
                "Nosso horário de atendimento humano é de segunda a sexta, das 8h às 18h."
            )
        
        else:  # intent == 'desconhecido' ou qualquer outro não tratado
            # Verificar se há sintomas mencionados
            sintomas = entities.get('sintomas', [])
            if sintomas:
                symptom = sintomas[0]
                
                # Definir contexto para esperar mais detalhes sobre o sintoma
                ContextManager.set_context(
                    user_id, 
                    platform, 
                    ContextManager.CONTEXT_TYPES['WAITING_SYMPTOM'],
                    {'symptom': symptom}
                )
                
                return (
                    f"Entendi que você está com {symptom}. "
                    f"Pode me dar mais detalhes sobre esse sintoma? "
                    f"Por exemplo, há quanto tempo está sentindo, se há outros sintomas associados, etc."
                )
            
            # Resposta padrão para intenções não reconhecidas
            return (
                "Desculpe, não entendi completamente sua solicitação. "
                "Posso ajudar com informações sobre medicamentos, preços, disponibilidade, "
                "horários de funcionamento ou localização da farmácia. "
                "Como posso te ajudar?"
            )


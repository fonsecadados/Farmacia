from nlp_processor import NLPProcessor
from context_manager import ContextManager
from models import Product, FAQ, Conversation

class ResponseGenerator:
    """Gerador de respostas para o bot de farmácia"""
    
    @staticmethod
    def generate_response(user_id, platform, message_text):
        """Gera uma resposta com base na mensagem do usuário e no contexto"""
        # Salvar a mensagem do usuário
        Conversation.save_message(user_id, platform, message_text, is_from_user=True)
        
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


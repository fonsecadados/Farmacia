from models import Conversation, Product

class ContextManager:
    """Gerenciador de contexto para fluxos de conversação"""
    
    # Tipos de contexto
    CONTEXT_TYPES = {
        'NONE': 'none',                       # Sem contexto específico
        'ASKING_MEDICINE_INFO': 'asking_medicine_info',  # Perguntando sobre um medicamento
        'CHECKING_STOCK': 'checking_stock',    # Verificando disponibilidade de produto
        'WAITING_SYMPTOM': 'waiting_symptom',  # Esperando descrição de sintoma
        'CONFIRMING_ORDER': 'confirming_order' # Confirmando um pedido
    }
    
    @staticmethod
    def get_current_context(user_id, platform):
        """Obtém o contexto atual da conversa"""
        context = Conversation.get_context(user_id, platform)
        if not context:
            return {
                'type': ContextManager.CONTEXT_TYPES['NONE'],
                'data': {}
            }
        return context
    
    @staticmethod
    def set_context(user_id, platform, context_type, context_data=None):
        """Define o contexto da conversa"""
        if context_type not in ContextManager.CONTEXT_TYPES.values():
            raise ValueError(f"Tipo de contexto inválido: {context_type}")
        
        Conversation.set_context(user_id, platform, context_type, context_data or {})
    
    @staticmethod
    def clear_context(user_id, platform):
        """Limpa o contexto da conversa"""
        Conversation.clear_context(user_id, platform)
    
    @staticmethod
    def process_in_context(user_id, platform, message_text, nlp_result):
        """
        Processa a mensagem considerando o contexto atual
        Retorna uma tupla (resposta, novo_contexto, dados_contexto)
        """
        current_context = ContextManager.get_current_context(user_id, platform)
        context_type = current_context.get('type', ContextManager.CONTEXT_TYPES['NONE'])
        context_data = current_context.get('data', {})
        
        # Se não há contexto específico, retorna None para processamento normal
        if context_type == ContextManager.CONTEXT_TYPES['NONE']:
            return None, None, None
        
        # Processamento baseado no tipo de contexto
        if context_type == ContextManager.CONTEXT_TYPES['ASKING_MEDICINE_INFO']:
            medicine_name = context_data.get('medicine_name')
            
            # Se a intenção for de despedida ou ajuda, limpar o contexto
            if nlp_result['intent'] in ['despedida', 'ajuda']:
                return None, ContextManager.CONTEXT_TYPES['NONE'], None
            
            response = Product.find_by_name(medicine_name)

            # Aqui seria implementada a lógica para buscar informações do medicamento
            # Por enquanto, apenas simulamos uma resposta
            response = f"Aqui estão as informações sobre {medicine_name}:\n\n"
            response += "- Indicação: [informações de indicação]\n"
            response += "- Posologia: [informações de posologia]\n"
            response += "- Efeitos colaterais: [informações de efeitos colaterais]\n"
            response += "- Contraindicações: [informações de contraindicações]\n\n"
            response += "Posso ajudar com mais alguma informação sobre este medicamento?"
            
            # Manter o mesmo contexto para continuar falando sobre o medicamento
            return response, context_type, context_data
        
        elif context_type == ContextManager.CONTEXT_TYPES['CHECKING_STOCK']:
            product_name = context_data.get('product_name')
            
            # Se a intenção for de despedida ou ajuda, limpar o contexto
            if nlp_result['intent'] in ['despedida', 'ajuda']:
                ContextManager.clear_context(user_id, platform)
                return None, ContextManager.CONTEXT_TYPES['NONE'], None
            
            # Aqui seria implementada a lógica para verificar o estoque
            # Por enquanto, apenas simulamos uma resposta
            response = f"Verificamos e temos {product_name} disponível em estoque!\n"
            response += "Deseja saber o preço ou mais informações sobre este produto?"
            
            # Manter o mesmo contexto para continuar falando sobre o produto
            return response, context_type, context_data
        
        elif context_type == ContextManager.CONTEXT_TYPES['WAITING_SYMPTOM']:
            # Processar a descrição do sintoma
            symptom = message_text.strip()
            
            # Aqui seria implementada a lógica para recomendar medicamentos
            # Por enquanto, apenas simulamos uma resposta
            response = f"Para sintomas como '{symptom}', posso recomendar:\n\n"
            response += "1. [Medicamento 1] - [breve descrição]\n"
            response += "2. [Medicamento 2] - [breve descrição]\n"
            response += "3. [Medicamento 3] - [breve descrição]\n\n"
            response += "Lembre-se que esta é apenas uma sugestão inicial. Para um diagnóstico preciso, consulte um médico ou farmacêutico."
            
            # Limpar o contexto após fornecer recomendações
            return response, ContextManager.CONTEXT_TYPES['NONE'], None
        
        # Para outros tipos de contexto não implementados
        return None, None, None


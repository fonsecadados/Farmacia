from pymongo import MongoClient
from datetime import datetime
from config import MONGODB_URI, DB_NAME

# Conexão com o MongoDB
client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

# Coleções
users = db.users
conversations = db.conversations
products_collection = db.products
faqs = db.faqs

class User:
    """Modelo para usuários do bot"""
    
    @staticmethod
    def create_or_update(user_id, platform, first_name=None, last_name=None, username=None):
        """Cria ou atualiza um usuário no banco de dados"""
        user_data = {
            'user_id': user_id,
            'platform': platform,  # 'telegram' ou 'whatsapp'#
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'last_interaction': datetime.now(),
            'updated_at': datetime.now()
        }
        
        # Verifica se o usuário já existe
        existing_user = users.find_one({'user_id': user_id, 'platform': platform})
        
        if existing_user:
            # Atualiza o usuário existente
            users.update_one(
                {'_id': existing_user['_id']},
                {'$set': user_data}
            )
            return existing_user['_id']
        else:
            # Cria um novo usuário
            user_data['created_at'] = datetime.now()
            result = users.insert_one(user_data)
            return result.inserted_id
    
    @staticmethod
    def get_user(user_id, platform):
        """Obtém um usuário pelo ID e plataforma"""
        return users.find_one({'user_id': user_id, 'platform': platform})


class Conversation:
    """Modelo para gerenciar conversas e contexto"""
    
    @staticmethod
    def save_message(user_id, platform, message_text, is_from_user=True):
        """Salva uma mensagem na conversa"""
        message = {
            'user_id': user_id,
            'platform': platform,
            'text': message_text,
            'is_from_user': is_from_user,
            'timestamp': datetime.now()
        }
        conversations.insert_one(message)
    
    @staticmethod
    def get_recent_messages(user_id, platform, limit=5):
        """Obtém as mensagens recentes de um usuário"""
        return list(conversations.find(
            {'user_id': user_id, 'platform': platform},
            {'_id': 0, 'text': 1, 'is_from_user': 1, 'timestamp': 1}
        ).sort('timestamp', -1).limit(limit))
    
    @staticmethod
    def set_context(user_id, platform, context_type, context_data=None):
        """Define o contexto da conversa para um usuário"""
        users.update_one(
            {'user_id': user_id, 'platform': platform},
            {'$set': {
                'context': {
                    'type': context_type,
                    'data': context_data or {},
                    'created_at': datetime.now()
                },
                'last_interaction': datetime.now()
            }}
        )
    
    @staticmethod
    def get_context(user_id, platform):
        """Obtém o contexto atual da conversa de um usuário"""
        user = users.find_one(
            {'user_id': user_id, 'platform': platform},
            {'context': 1}
        )
        return user.get('context') if user and 'context' in user else None
    
    @staticmethod
    def clear_context(user_id, platform):
        """Limpa o contexto da conversa de um usuário"""
        users.update_one(
            {'user_id': user_id, 'platform': platform},
            {'$unset': {'context': ''}, '$set': {'last_interaction': datetime.now()}}
        )


class Product:
        """Modelo para produtos/medicamentos"""
        
        @staticmethod
        def add_product(name, description, category, manufacturer, dosage_form, administration_route, principio_ativo, link_bula, indicacao):
            product = {
                'name': name,
                'principio_ativo' : principio_ativo,
                'description': description,
                'category': category,
                'manufacturer': manufacturer,
                'dosage_form' : dosage_form,
                'administration_route' : administration_route,
                'link_bula' : link_bula,
                'indicacao' : indicacao,
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }
            products_collection.insert_one(product)
        
        @staticmethod
        def search_products(query, limit=5):    
            return list(products_collection.find({
                '$or': [
                    {'name': {'$regex': query, '$options': 'i'}},
                    {'description': {'$regex': query, '$options': 'i'}},
                    {'manufacturer': {'$regex': query, '$options': 'i'}},
                    {'principio_ativo': {'$regex': query, '$options': 'i'}},
                ]
            }).limit(limit))
        
        @staticmethod
        def get_product_by_name(name):
            name = name.strip().lower()
            return products_collection.find_one({
                'name': {'$regex': name, '$options': 'i'}
            })

        @staticmethod
        def get_all():
            """Retorna todos os produtos do banco"""
            return list(products_collection.find())


class FAQ:
    """Modelo para perguntas frequentes"""
    @staticmethod
    def get_all():
        # Retorna todas as FAQs como uma lista de dicionários ordenada
        return list(db.faqs.find())  #
    
    @staticmethod
    def add_faq(question, answer, category=None):
        """Adiciona uma nova pergunta frequente"""
        faq = {
            'question': question,
            'answer': answer,
            'category': category,
            'created_at': datetime.now(),
            'updated_at': datetime.now()
        }
        faqs.insert_one(faq)
    
    @staticmethod
    def search_faqs(query, limit=3):
        """Busca perguntas frequentes pela pergunta"""
        return list(faqs.find({
            'question': {'$regex': query, '$options': 'i'}
        }).limit(limit))
    
    @staticmethod
    def get_all_faqs():
        """Obtém todas as perguntas frequentes"""
        return list(faqs.find())


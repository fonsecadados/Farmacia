import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do bot
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN', 'seu_token_aqui')
WHATSAPP_TOKEN = os.getenv('WHATSAPP_TOKEN', 'seu_token_aqui')
WHATSAPP_PHONE_ID = os.getenv('WHATSAPP_PHONE_ID', 'seu_phone_id_aqui')

# Configurações do banco de dados
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
DB_NAME = os.getenv('DB_NAME', 'farmacia_bot')

# Configurações da aplicação
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
PORT = int(os.getenv('PORT', 5000))


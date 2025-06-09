import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from response_generator import ResponseGenerator
from context_manager import ContextManager
from models import User

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Carregar variáveis de ambiente
load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Verificar se o token está configurado
if not TELEGRAM_TOKEN:
    logger.error("Token do Telegram não configurado. Configure a variável TELEGRAM_TOKEN no arquivo .env")
    exit(1)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /start para iniciar a conversa com o bot"""
    user = update.effective_user
    
    # Registrar ou atualizar o usuário no banco de dados
    try:
        User.create_or_update(
            user_id=str(user.id),
            platform="telegram",
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username
        )
    except Exception as e:
        logger.error(f"Erro ao registrar usuário: {e}")
    
    # Obter mensagem de boas-vindas do ResponseGenerator
    welcome_message = ResponseGenerator.get_welcome_message(user.first_name)
    
    # Definir contexto de menu principal
    ContextManager.set_context(str(user.id), "telegram", ContextManager.CONTEXT_TYPES['MAIN_MENU'], {})
    
    await update.message.reply_text(welcome_message)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Manipulador para mensagens de texto"""
    user = update.effective_user
    message_text = update.message.text

    # Registrar ou atualizar o usuário no banco de dados (caso ainda não tenha sido registrado)
    try:
        User.create_or_update(
            user_id=str(user.id),
            platform="telegram",
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username
        )
    except Exception as e:
        logger.error(f"Erro ao registrar usuário: {e}")
        # Continuar mesmo com erro no banco de dados

    try:
        # Gerar resposta usando o ResponseGenerator
        response = ResponseGenerator.generate_response(str(user.id), "telegram", message_text)

        # Enviar a resposta
        if response and response.strip():
            await update.message.reply_text(response)
        else:
            await update.message.reply_text(
                "Desculpe, não entendi sua mensagem. Por favor, tente reformular ou escolher uma das opções do menu."
            )
    except Exception as e:
        logger.error(f"Erro ao processar mensagem: {e}")
        await update.message.reply_text(
            "Desculpe, ocorreu um erro ao processar sua mensagem. Por favor, tente novamente."
        )
def main() -> None:
    """Função principal para iniciar o bot"""
    # Criar o aplicativo
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Adicionar handlers
    application.add_handler(CommandHandler("start", start))
    # Handler para mensagens de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Iniciar o bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()


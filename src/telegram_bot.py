import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from response_generator import ResponseGenerator
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
    
    # Mensagem de boas-vindas 
    num_loja = 27999999999
    welcome_message = (
        f"👋 Olá, {user.first_name}! 👋\n\n"
        "📍 Bem-vindo(a) ao Atendimento Virtual📍\n🔹 Rede FARMES - Colina de Laranjeiras 🔹\n\n" 
        "Nosso atendimento é HUMANIZADO e estamos aqui para otimizar o seu tempo, por isso escreva o medicamento ou o produto você procura para consultar disponibilidade\n\n\n "
        "OU digite o número da opção:\n\n"
        "1️⃣ Conheça nossa loja e os horários de funcionamento 🏥\n\n"
        "2️⃣ Fazer cadastro na loja 🕜\n\n"
        "3️⃣ Fique por dentro das PROMOÇÔES 💯\n\n"
        "4️⃣ Tenho sintomas, preciso de recomendações 💊\n\n"
        "5️⃣ Perguntas Frequentes ❔\n\n"
        "6️⃣ Sugestões/Reclamações 	📢\n\n\n"
        f"Esse é um canal de atendimento automatizado, para falar com vendedor ligue para nossa loja:\n\n"
        f"{num_loja}\n\n"
        "💟 Como podemos te ajudar hoje? 💟"
    )
    
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /help para exibir ajuda"""
    help_message = (
        "Aqui estão os comandos disponíveis:\n\n"
        "/start - Iniciar ou reiniciar a conversa\n"
        "/help - Exibir esta mensagem de ajuda\n"
        "/horario - Verificar horário de funcionamento\n"
        "/localizacao - Ver a localização da farmácia\n"
        "/falar_humano - Solicitar atendimento humano\n\n"
        "Você também pode simplesmente enviar mensagens normais para perguntar sobre medicamentos, "
        "verificar disponibilidade de produtos ou descrever sintomas."
    )
    #
    await update.message.reply_text(help_message)

async def horario_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /horario para verificar horário de funcionamento"""
    horario_message = (
        "Nossa farmácia está aberta nos seguintes horários:\n\n"
        "Segunda a Sexta: 08:00 às 20:00\n"
        "Sábados: 08:00 às 18:00\n"
        "Domingos e Feriados: 09:00 às 13:00\n\n"
        "Posso ajudar com mais alguma informação?"
    )
    
    await update.message.reply_text(horario_message)

async def localizacao_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /localizacao para ver a localização da farmácia"""
    localizacao_message = (
        "Nossa farmácia está localizada na Av. Principal, 123 - Centro.\n\n"
        "Referência: Próximo ao Banco do Brasil.\n\n"
        "Você pode nos encontrar facilmente pelo Google Maps pesquisando por 'Farmácia Virtual'."
    )
    
    await update.message.reply_text(localizacao_message)

async def falar_humano_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /falar_humano para solicitar atendimento humano"""
    falar_humano_message = (
        "Entendo que você prefere falar com um atendente humano.\n\n"
        "Para isso, você pode ligar para nossa central de atendimento no número (XX) XXXX-XXXX "
        "ou enviar um e-mail para atendimento@farmaciavirtual.com.br.\n\n"
        "Nosso horário de atendimento humano é de segunda a sexta, das 8h às 18h."
    )
    
    await update.message.reply_text(falar_humano_message)

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
        await update.message.reply_text(response)
    except Exception as e:
        logger.error(f"Erro ao processar mensagem: {e}")
        await update.message.reply_text(
            "Desculpe, ocorreu um erro ao processar sua mensagem. Por favor, tente novamente mais tarde."
        )

def main() -> None:
    """Função principal para iniciar o bot"""
    # Criar o aplicativo
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Adicionar handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("horario", horario_command))
    application.add_handler(CommandHandler("localizacao", localizacao_command))
    application.add_handler(CommandHandler("falar_humano", falar_humano_command))
    
    # Handler para mensagens de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Iniciar o bot
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()


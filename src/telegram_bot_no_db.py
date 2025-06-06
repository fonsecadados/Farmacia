import logging
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from nlp_processor import NLPProcessor

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

# Dicionário para armazenar contextos de conversa (simulando banco de dados)
user_contexts = {}

# Respostas pré-definidas para cada intenção
RESPONSES = {
    'saudacao': (
        "Olá! Bem-vindo à Farmácia Virtual. Como posso ajudar você hoje? 😊\n\n"
        "Posso fornecer informações sobre medicamentos, verificar disponibilidade de produtos, "
        "informar horários de funcionamento e muito mais."
    ),
    'despedida': (
        "Obrigado por entrar em contato! Estamos sempre à disposição para ajudar. "
        "Tenha um ótimo dia! 👋"
    ),
    'agradecimento': (
        "Por nada! Estou aqui para ajudar. Precisa de mais alguma coisa?"
    ),
    'info_medicamento': (
        "Você gostaria de informações sobre um medicamento específico. "
        "Por favor, informe o nome do medicamento para que eu possa buscar os detalhes para você."
    ),
    'preco': (
        "Para verificar o preço de um produto específico, por favor informe o nome do medicamento ou produto."
    ),
    'disponibilidade': (
        "Para verificar a disponibilidade de um produto, por favor informe o nome do medicamento ou produto."
    ),
    'horario': (
        "Nossa farmácia está aberta nos seguintes horários:\n\n"
        "Segunda a Sexta: 08:00 às 20:00\n"
        "Sábados: 08:00 às 18:00\n"
        "Domingos e Feriados: 09:00 às 13:00\n\n"
        "Posso ajudar com mais alguma informação?"
    ),
    'localizacao': (
        "Nossa farmácia está localizada na Av. Principal, 123 - Centro. \n\n"
        "Referência: Próximo ao Banco do Brasil.\n\n"
        "Você pode nos encontrar facilmente pelo Google Maps pesquisando por 'Farmácia Virtual'."
    ),
    'ajuda': (
        "Posso ajudar você com:\n\n"
        "- Informações sobre medicamentos\n"
        "- Preços de produtos\n"
        "- Verificação de disponibilidade em estoque\n"
        "- Horários de funcionamento\n"
        "- Localização da farmácia\n"
        "- Recomendações para sintomas\n\n"
        "Como posso te ajudar hoje?"
    ),
    'falar_humano': (
        "Entendo que você prefere falar com um atendente humano. "
        "Para isso, você pode ligar para nossa central de atendimento no número (XX) XXXX-XXXX "
        "ou enviar um e-mail para atendimento@farmaciavirtual.com.br.\n\n"
        "Nosso horário de atendimento humano é de segunda a sexta, das 8h às 18h."
    ),
    'desconhecido': (
        "Desculpe, não entendi completamente sua solicitação. "
        "Posso ajudar com informações sobre medicamentos, preços, disponibilidade, "
        "horários de funcionamento ou localização da farmácia. "
        "Como posso te ajudar?"
    )
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /start para iniciar a conversa com o bot"""
    user = update.effective_user
    
    # Mensagem de boas-vindas
    welcome_message = (
        f"Olá, {user.first_name}! 👋\n\n"
        "Bem-vindo(a) ao Bot da Farmácia Virtual. Estou aqui para ajudar você com:\n\n"
        "• Informações sobre medicamentos\n"
        "• Verificação de disponibilidade de produtos\n"
        "• Horários de funcionamento\n"
        "• Localização da farmácia\n"
        "• Recomendações para sintomas\n\n"
        "Como posso te ajudar hoje?"
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
    
    await update.message.reply_text(help_message)

async def horario_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /horario para verificar horário de funcionamento"""
    await update.message.reply_text(RESPONSES['horario'])

async def localizacao_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /localizacao para ver a localização da farmácia"""
    await update.message.reply_text(RESPONSES['localizacao'])

async def falar_humano_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Comando /falar_humano para solicitar atendimento humano"""
    await update.message.reply_text(RESPONSES['falar_humano'])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Manipulador para mensagens de texto"""
    user = update.effective_user
    message_text = update.message.text
    user_id = str(user.id)
    
    # Analisar o texto com NLP
    nlp_result = NLPProcessor.analyze_text(message_text)
    intent = nlp_result['intent']
    entities = nlp_result['entities']
    
    # Log para depuração
    logger.info(f"Usuário: {user_id}, Mensagem: {message_text}")
    logger.info(f"Intenção detectada: {intent}")
    logger.info(f"Entidades detectadas: {entities}")
    
    # Verificar se há medicamentos mencionados
    medicamentos = entities.get('medicamentos', [])
    
    # Personalizar resposta com base na intenção e entidades
    if intent in RESPONSES:
        response = RESPONSES[intent]
        
        # Personalizar resposta para medicamentos específicos
        if intent == 'info_medicamento' and medicamentos:
            medicine_name = medicamentos[0]
            response = (
                f"Aqui estão as informações sobre {medicine_name}:\n\n"
                "- Indicação: [informações de indicação]\n"
                "- Posologia: [informações de posologia]\n"
                "- Efeitos colaterais: [informações de efeitos colaterais]\n"
                "- Contraindicações: [informações de contraindicações]\n\n"
                "Posso ajudar com mais alguma informação sobre este medicamento?"
            )
        elif intent == 'preco' and medicamentos:
            medicine_name = medicamentos[0]
            response = f"O preço atual de {medicine_name} é R$ XX,XX. Posso ajudar com mais alguma informação?"
        elif intent == 'disponibilidade' and medicamentos:
            medicine_name = medicamentos[0]
            response = f"Verificamos e temos {medicine_name} disponível em estoque! Deseja saber o preço ou mais informações sobre este produto?"
    else:
        # Verificar se há sintomas mencionados
        sintomas = entities.get('sintomas', [])
        if sintomas:
            symptom = sintomas[0]
            response = (
                f"Entendi que você está com {symptom}. Para sintomas como este, posso recomendar:\n\n"
                "1. [Medicamento 1] - [breve descrição]\n"
                "2. [Medicamento 2] - [breve descrição]\n"
                "3. [Medicamento 3] - [breve descrição]\n\n"
                "Lembre-se que esta é apenas uma sugestão inicial. Para um diagnóstico preciso, consulte um médico ou farmacêutico."
            )
        else:
            response = RESPONSES['desconhecido']
    
    # Enviar a resposta
    await update.message.reply_text(response)

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


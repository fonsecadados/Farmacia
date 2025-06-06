import logging
import os
import json
import requests
from flask import Flask, request, jsonify
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
WHATSAPP_TOKEN = os.getenv('WHATSAPP_TOKEN')
WHATSAPP_PHONE_ID = os.getenv('WHATSAPP_PHONE_ID')
VERIFY_TOKEN = os.getenv('VERIFY_TOKEN', 'farmacia_bot_verify_token')
PORT = int(os.getenv('PORT', 5000))

# Verificar se os tokens estão configurados
if not WHATSAPP_TOKEN or not WHATSAPP_PHONE_ID:
    logger.error("Token do WhatsApp ou Phone ID não configurados. Configure as variáveis WHATSAPP_TOKEN e WHATSAPP_PHONE_ID no arquivo .env")
    exit(1)

# Criar aplicação Flask
app = Flask(__name__)

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

def send_whatsapp_message(phone_number, message_text):
    """Envia uma mensagem para o WhatsApp"""
    url = f"https://graph.facebook.com/v17.0/{WHATSAPP_PHONE_ID}/messages"
    
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    
    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": message_text
        }
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao enviar mensagem para o WhatsApp: {e}")
        return None

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    """Endpoint para verificação do webhook do WhatsApp"""
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    
    if mode and token:
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            logger.info("Webhook verificado com sucesso!")
            return challenge, 200
        else:
            logger.warning("Falha na verificação do webhook")
            return "Falha na verificação", 403
    
    return "Parâmetros inválidos", 400

@app.route('/webhook', methods=['POST'])
def webhook():
    """Endpoint para receber mensagens do WhatsApp"""
    data = request.json
    
    # Log para depuração
    logger.info(f"Webhook recebido: {json.dumps(data, indent=2)}")
    
    # Verificar se é uma mensagem do WhatsApp
    if 'object' in data and data['object'] == 'whatsapp_business_account':
        if 'entry' in data and data['entry']:
            for entry in data['entry']:
                if 'changes' in entry and entry['changes']:
                    for change in entry['changes']:
                        if 'value' in change and 'messages' in change['value']:
                            for message in change['value']['messages']:
                                if message['type'] == 'text':
                                    # Extrair informações da mensagem
                                    phone_number = message['from']
                                    message_text = message['text']['body']
                                    message_id = message['id']
                                    
                                    # Log para depuração
                                    logger.info(f"Mensagem recebida de {phone_number}: {message_text}")
                                    
                                    # Analisar o texto com NLP
                                    nlp_result = NLPProcessor.analyze_text(message_text)
                                    intent = nlp_result['intent']
                                    entities = nlp_result['entities']
                                    
                                    # Log para depuração
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
                                    send_whatsapp_message(phone_number, response)
        
        return jsonify({"status": "success"}), 200
    
    return jsonify({"status": "error", "message": "Formato inválido"}), 400

@app.route('/', methods=['GET'])
def index():
    """Endpoint raiz para verificar se o servidor está em execução"""
    return "WhatsApp Bot para Farmácia está em execução!", 200

def main():
    """Função principal para iniciar o servidor Flask"""
    app.run(host='0.0.0.0', port=PORT, debug=False)

if __name__ == '__main__':
    main()


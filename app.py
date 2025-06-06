import os
import logging
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
from whatsapp_bot_no_db import webhook as whatsapp_webhook
from whatsapp_bot_no_db import verify_webhook as whatsapp_verify_webhook

# Configurar logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Carregar variáveis de ambiente
load_dotenv()
PORT = int(os.getenv('PORT', 5000))

# Criar aplicação Flask
app = Flask(__name__)

# Criar pasta templates se não existir
os.makedirs('templates', exist_ok=True)

# Criar um template HTML simples para a página inicial
with open('templates/index.html', 'w') as f:
    f.write("""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farmácia Bot - Agente de IA para Atendimento</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            color: #0066cc;
            border-bottom: 2px solid #0066cc;
            padding-bottom: 10px;
        }
        h2 {
            color: #0066cc;
            margin-top: 30px;
        }
        .container {
            background-color: #f9f9f9;
            border-radius: 5px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .status {
            background-color: #e6f7ff;
            border-left: 4px solid #0066cc;
            padding: 10px;
            margin: 20px 0;
        }
        code {
            background-color: #f1f1f1;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: monospace;
        }
        ul {
            margin-left: 20px;
        }
        footer {
            margin-top: 50px;
            text-align: center;
            font-size: 0.8em;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Farmácia Bot - Agente de IA para Atendimento</h1>
    
    <div class="status">
        <strong>Status:</strong> Servidor em execução
    </div>
    
    <div class="container">
        <h2>Sobre o Bot</h2>
        <p>Este é um Agente de IA para atendimento de farmácia, com integração para teste no Telegram e integração profissional para WhatsApp.</p>
        
        <h2>Funcionalidades</h2>
        <ul>
            <li>Responder a perguntas frequentes sobre a farmácia</li>
            <li>Fornecer informações sobre medicamentos</li>
            <li>Verificar disponibilidade de produtos</li>
            <li>Informar horários de funcionamento e localização</li>
            <li>Recomendar medicamentos com base em sintomas</li>
            <li>Direcionar o usuário para um atendente humano quando necessário</li>
        </ul>
        
        <h2>Integrações</h2>
        <ul>
            <li><strong>Telegram:</strong> Para testes e demonstração</li>
            <li><strong>WhatsApp:</strong> Para uso profissional</li>
        </ul>
    </div>
    
    <footer>
        &copy; 2025 Farmácia Virtual - Todos os direitos reservados
    </footer>
</body>
</html>
    """)

@app.route('/', methods=['GET'])
def index():
    """Endpoint raiz para verificar se o servidor está em execução"""
    return render_template('index.html')

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    """Endpoint para verificação do webhook do WhatsApp"""
    return whatsapp_verify_webhook()

@app.route('/webhook', methods=['POST'])
def webhook():
    """Endpoint para receber mensagens do WhatsApp"""
    return whatsapp_webhook()

@app.route('/health', methods=['GET'])
def health_check():
    """Endpoint para verificar a saúde do servidor"""
    return jsonify({"status": "healthy"}), 200

def main():
    """Função principal para iniciar o servidor Flask"""
    app.run(host='0.0.0.0', port=PORT, debug=False)

if __name__ == '__main__':
    main()


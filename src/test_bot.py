from response_generator import ResponseGenerator
from models import User
import time

def test_bot():
    """Função para testar o bot com diferentes cenários de atendimento"""
    
    # Criar um usuário de teste
    user_id = "test_user_123"
    platform = "test"
    User.create_or_update(user_id, platform, "Usuário", "Teste")
    
    # Cenários de teste
    test_scenarios = [
        {
            "name": "Saudação",
            "messages": [
                "Olá",
                "Oi, tudo bem?",
                "Bom dia"
            ]
        },
        {
            "name": "Informações sobre medicamentos",
            "messages": [
                "Quero informações sobre Paracetamol",
                "Para que serve Dipirona?",
                "Qual a dosagem de Ibuprofeno?"
            ]
        },
        {
            "name": "Verificação de disponibilidade",
            "messages": [
                "Vocês têm Omeprazol?",
                "Tem Amoxicilina disponível?",
                "Quero saber se tem Dipirona em estoque"
            ]
        },
        {
            "name": "Horário de funcionamento",
            "messages": [
                "Qual o horário de funcionamento?",
                "Que horas vocês fecham?",
                "Vocês abrem aos domingos?"
            ]
        },
        {
            "name": "Localização",
            "messages": [
                "Onde fica a farmácia?",
                "Qual o endereço?",
                "Como faço para chegar aí?"
            ]
        },
        {
            "name": "Sintomas",
            "messages": [
                "Estou com dor de cabeça",
                "Tenho febre alta",
                "Estou com tosse seca"
            ]
        },
        {
            "name": "Falar com humano",
            "messages": [
                "Quero falar com um atendente",
                "Preciso falar com um farmacêutico",
                "Tem alguém que possa me ajudar?"
            ]
        },
        {
            "name": "Despedida",
            "messages": [
                "Obrigado, tchau",
                "Até mais",
                "Valeu, até a próxima"
            ]
        }
    ]
    
    # Executar os testes
    for scenario in test_scenarios:
        print(f"\n\n=== Testando cenário: {scenario['name']} ===\n")
        
        for message in scenario['messages']:
            print(f"Usuário: {message}")
            
            # Gerar resposta
            response = ResponseGenerator.generate_response(user_id, platform, message)
            
            print(f"Bot: {response}")
            print("-" * 50)
            
            # Pequena pausa para simular uma conversa real
            time.sleep(1)

if __name__ == "__main__":
    test_bot()


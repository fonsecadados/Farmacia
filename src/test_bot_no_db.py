from nlp_processor import NLPProcessor
import time

def test_bot_no_db():
    """Função para testar o processador de linguagem natural sem dependência do banco de dados"""
    
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
            
            # Analisar o texto com NLP
            nlp_result = NLPProcessor.analyze_text(message)
            
            print(f"Intenção detectada: {nlp_result['intent']}")
            print(f"Entidades detectadas: {nlp_result['entities']}")
            print("-" * 50)
            
            # Pequena pausa para simular uma conversa real
            time.sleep(1)

if __name__ == "__main__":
    test_bot_no_db()


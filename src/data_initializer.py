from models import Product, FAQ

def initialize_sample_data():
    """Inicializa dados de exemplo para o bot"""
    
    # Adicionar produtos de exemplo
    products = [
        {
            'name': 'Paracetamol',
            'description': 'Analgésico e antitérmico indicado para dores leves a moderadas e febre.',
            'price': 5.99,
            'stock': 100,
            'category': 'Analgésico',
            'prescription_required': False
        },
        {
            'name': 'Dipirona',
            'description': 'Analgésico, antitérmico e antiespasmódico indicado para dores e febre.',
            'price': 4.50,
            'stock': 80,
            'category': 'Analgésico',
            'prescription_required': False
        },
        {
            'name': 'Ibuprofeno',
            'description': 'Anti-inflamatório não esteroidal (AINE) indicado para dores e inflamações.',
            'price': 8.75,
            'stock': 65,
            'category': 'Anti-inflamatório',
            'prescription_required': False
        },
        {
            'name': 'Amoxicilina',
            'description': 'Antibiótico de amplo espectro indicado para infecções bacterianas.',
            'price': 25.90,
            'stock': 40,
            'category': 'Antibiótico',
            'prescription_required': True
        },
        {
            'name': 'Omeprazol',
            'description': 'Inibidor da bomba de prótons indicado para problemas gástricos.',
            'price': 12.30,
            'stock': 55,
            'category': 'Antiácido',
            'prescription_required': False
        }
    ]
    
    for product in products:
        Product.add_product(
            name=product['name'],
            description=product['description'],
            price=product['price'],
            stock=product['stock'],
            category=product['category'],
            prescription_required=product['prescription_required']
        )
    
    # Adicionar FAQs de exemplo
    faqs = [
        {
            'question': 'Qual o horário de funcionamento da farmácia?',
            'answer': 'Nossa farmácia está aberta de segunda a sexta das 8h às 20h, aos sábados das 8h às 18h, e aos domingos e feriados das 9h às 13h.',
            'category': 'Horário'
        },
        {
            'question': 'Vocês aceitam receitas digitais?',
            'answer': 'Sim, aceitamos receitas digitais desde que estejam dentro da validade e contenham todas as informações necessárias, incluindo assinatura digital do médico.',
            'category': 'Receitas'
        },
        {
            'question': 'Quais formas de pagamento são aceitas?',
            'answer': 'Aceitamos dinheiro, cartões de crédito e débito de todas as bandeiras, PIX e vale-farmácia.',
            'category': 'Pagamento'
        },
        {
            'question': 'Vocês fazem entrega?',
            'answer': 'Sim, realizamos entregas em toda a cidade. Para pedidos acima de R$ 50,00, a entrega é gratuita. Para valores menores, é cobrada uma taxa que varia conforme a região.',
            'category': 'Entrega'
        },
        {
            'question': 'Como posso falar com um farmacêutico?',
            'answer': 'Você pode falar com um farmacêutico visitando nossa loja física ou ligando para (XX) XXXX-XXXX durante o horário de funcionamento.',
            'category': 'Atendimento'
        }
    ]
    #
    for faq in faqs:
        FAQ.add_faq(
            question=faq['question'],
            answer=faq['answer'],
            category=faq['category']
        )
    
    print("Dados de exemplo inicializados com sucesso!")

if __name__ == "__main__":
    initialize_sample_data()


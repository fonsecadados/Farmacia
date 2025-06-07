from models import Product, FAQ

def initialize_sample_data():
    """Inicializa dados de exemplo para o bot"""
    
    # Adicionar produtos de exemplo
    products = [
    {
        'name': 'Loratadina',
        'description': 'Antialérgico utilizado para o alívio de sintomas de rinite e urticária. Não causa sonolência.',
        'price': 7.50,
        'stock': 75,
        'category': 'Antialérgico',
        'prescription_required': False,
        'manufacturer': 'Neo Química',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Omeprazol',
        'description': 'Inibidor de bomba de prótons utilizado no tratamento de gastrite e refluxo. Substituto da Ranitidina.',
        'price': 9.80,
        'stock': 80,
        'category': 'Antiácido',
        'prescription_required': False,
        'manufacturer': 'Medley',
        'dosage_form': 'Cápsula',
        'administration_route': 'Oral'
    },
    {
        'name': 'Sal de Fruta ENO',
        'description': 'Antiácido efervescente para alívio imediato da azia e má digestão.',
        'price': 5.90,
        'stock': 100,
        'category': 'Antiácido',
        'prescription_required': False,
        'manufacturer': 'GSK',
        'dosage_form': 'Pó efervescente',
        'administration_route': 'Oral'
    },
    {
        'name': 'Neosaldina',
        'description': 'Analgésico para dores de cabeça, incluindo enxaquecas leves.',
        'price': 6.40,
        'stock': 70,
        'category': 'Analgésico',
        'prescription_required': False,
        'manufacturer': 'Takeda',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Engov',
        'description': 'Medicamento para alívio de sintomas após ingestão de álcool, como dor de cabeça e náuseas.',
        'price': 4.90,
        'stock': 90,
        'category': 'Combinado',
        'prescription_required': False,
        'manufacturer': 'Cellera Farma',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Multigrip',
        'description': 'Medicamento combinado para o alívio dos sintomas da gripe.',
        'price': 5.60,
        'stock': 95,
        'category': 'Antigripal',
        'prescription_required': False,
        'manufacturer': 'Cimed',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Benegrip',
        'description': 'Combinado para alívio da gripe e resfriado, com cafeína para reduzir sonolência.',
        'price': 6.20,
        'stock': 85,
        'category': 'Antigripal',
        'prescription_required': False,
        'manufacturer': 'Hypera Pharma',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Tylenol',
        'description': 'Versão de marca do paracetamol, usado para dor e febre.',
        'price': 7.90,
        'stock': 70,
        'category': 'Analgésico',
        'prescription_required': False,
        'manufacturer': 'Janssen',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Doril',
        'description': 'Analgésico e antitérmico usado para dores leves e moderadas, incluindo dor de cabeça.',
        'price': 6.60,
        'stock': 60,
        'category': 'Analgésico',
        'prescription_required': False,
        'manufacturer': 'Hypera Pharma',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Aspirina',
        'description': 'Analgésico e anti-inflamatório leve utilizado para dor, febre e prevenção cardiovascular.',
        'price': 6.30,
        'stock': 90,
        'category': 'Analgésico',
        'prescription_required': False,
        'manufacturer': 'Bayer',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Airon',
        'description': 'Suplemento de ferro usado em casos de anemia leve e prevenção. Isento de prescrição.',
        'price': 10.90,
        'stock': 50,
        'category': 'Suplemento',
        'prescription_required': False,
        'manufacturer': 'EMS',
        'dosage_form': 'Cápsula',
        'administration_route': 'Oral'
    },
    {
        'name': 'Lavitan',
        'description': 'Polivitamínico para suporte nutricional e bem-estar geral.',
        'price': 18.50,
        'stock': 100,
        'category': 'Vitaminas',
        'prescription_required': False,
        'manufacturer': 'Cimed',
        'dosage_form': 'Comprimido revestido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Cimegripe',
        'description': 'Analgésico e descongestionante para alívio dos sintomas da gripe.',
        'price': 5.50,
        'stock': 80,
        'category': 'Antigripal',
        'prescription_required': False,
        'manufacturer': 'Cimed',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Redoxon',
        'description': 'Vitamina C efervescente para reforço da imunidade.',
        'price': 14.90,
        'stock': 40,
        'category': 'Vitaminas',
        'prescription_required': False,
        'manufacturer': 'Bayer',
        'dosage_form': 'Comprimido efervescente',
        'administration_route': 'Oral'
    },
    {
        'name': 'ENO Frutas Cítricas',
        'description': 'Antiácido com sabor para alívio rápido da má digestão e queimação.',
        'price': 6.10,
        'stock': 65,
        'category': 'Antiácido',
        'prescription_required': False,
        'manufacturer': 'GSK',
        'dosage_form': 'Pó efervescente',
        'administration_route': 'Oral'
    },
    {
        'name': 'Sonridor',
        'description': 'Analgésico e antitérmico com ação rápida. Indicado para dor de cabeça e febre.',
        'price': 5.80,
        'stock': 60,
        'category': 'Analgésico',
        'prescription_required': False,
        'manufacturer': 'Hypermarcas',
        'dosage_form': 'Comprimido efervescente',
        'administration_route': 'Oral'
    },
    {
        'name': 'Doralgina',
        'description': 'Analgésico indicado para dor de cabeça e dores musculares.',
        'price': 6.75,
        'stock': 50,
        'category': 'Analgésico',
        'prescription_required': False,
        'manufacturer': 'Sanofi',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Xantinon B12',
        'description': 'Suplemento vitamínico hepático, usado para suporte ao fígado.',
        'price': 19.90,
        'stock': 30,
        'category': 'Vitaminas',
        'prescription_required': False,
        'manufacturer': 'EMS',
        'dosage_form': 'Cápsula',
        'administration_route': 'Oral'
    },
    {
        'name': 'Pastilhas Valda',
        'description': 'Pastilhas refrescantes com ação expectorante suave e descongestionante. Uso comum em gripes.',
        'price': 3.40,
        'stock': 90,
        'category': 'Pastilha',
        'prescription_required': False,
        'manufacturer': 'Valda',
        'dosage_form': 'Pastilha',
        'administration_route': 'Oral'
    },
    {
        'name': 'Maxalgina',
        'description': 'Analgésico e antitérmico, indicado para dor moderada e febre persistente.',
        'price': 7.20,
        'stock': 45,
        'category': 'Analgésico',
        'prescription_required': False,
        'manufacturer': 'Aché',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Dipirona',
        'description': 'Analgésico, antitérmico e antiespasmódico indicado para dores e febre.',
        'price': 4.50,
        'stock': 80,
        'category': 'Analgésico',
        'prescription_required': False,
        'manufacturer': 'Sanofi',
        'dosage_form': 'Gotas',
        'administration_route': 'Oral'
    },
    {
        'name': 'Ibuprofeno',
        'description': 'Anti-inflamatório não esteroidal (AINE) indicado para dores e inflamações.',
        'price': 8.75,
        'stock': 65,
        'category': 'Anti-inflamatório',
        'prescription_required': False,
        'manufacturer': 'Abbott',
        'dosage_form': 'Comprimido revestido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Bromexina',
        'description': 'Expectorante indicado para eliminar secreções em doenças respiratórias.',
        'price': 9.40,
        'stock': 50,
        'category': 'Expectorante',
        'prescription_required': False,
        'manufacturer': 'EMS',
        'dosage_form': 'Xarope',
        'administration_route': 'Oral'
    },
    {
        'name': 'Clobutinol',
        'description': 'Antitussígeno para tosse seca e irritativa.',
        'price': 7.80,
        'stock': 45,
        'category': 'Antitussígeno',
        'prescription_required': False,
        'manufacturer': 'Aché',
        'dosage_form': 'Xarope',
        'administration_route': 'Oral'
    },
    {
        'name': 'Dorflex',
        'description': 'Analgésico e relaxante muscular para dores em geral.',
        'price': 6.90,
        'stock': 60,
        'category': 'Relaxante muscular',
        'prescription_required': False,
        'manufacturer': 'Sanofi',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Dramin',
        'description': 'Antiemético indicado para enjoo e náuseas.',
        'price': 4.25,
        'stock': 70,
        'category': 'Antiemético',
        'prescription_required': False,
        'manufacturer': 'Teuto',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Plasil',
        'description': 'Antiemético para náuseas e vômitos intensos.',
        'price': 6.10,
        'stock': 55,
        'category': 'Antiemético',
        'prescription_required': True,
        'manufacturer': 'Sanofi',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Antigripal',
        'description': 'Medicamento combinado para sintomas gripais.',
        'price': 8.50,
        'stock': 90,
        'category': 'Combinado',
        'prescription_required': False,
        'manufacturer': 'Cimed',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Descongex',
        'description': 'Descongestionante nasal para alívio de nariz entupido.',
        'price': 5.70,
        'stock': 40,
        'category': 'Descongestionante',
        'prescription_required': False,
        'manufacturer': 'Neo Química',
        'dosage_form': 'Spray nasal',
        'administration_route': 'Nasal'
    },
    {
        'name': 'Sorine',
        'description': 'Solução nasal para congestão e rinite.',
        'price': 4.95,
        'stock': 85,
        'category': 'Descongestionante',
        'prescription_required': False,
        'manufacturer': 'Boehringer',
        'dosage_form': 'Spray nasal',
        'administration_route': 'Nasal'
    },
    {
        'name': 'Benalet',
        'description': 'Pastilha para alívio de dores de garganta.',
        'price': 3.80,
        'stock': 100,
        'category': 'Analgésico para garganta',
        'prescription_required': False,
        'manufacturer': 'Aché',
        'dosage_form': 'Pastilha',
        'administration_route': 'Oral'
    },
    {
        'name': 'Melhorex',
        'description': 'Antisséptico para garganta com efeito analgésico.',
        'price': 4.60,
        'stock': 75,
        'category': 'Antisséptico bucal',
        'prescription_required': False,
        'manufacturer': 'EMS',
        'dosage_form': 'Spray bucal',
        'administration_route': 'Oral'
    },
    {
        'name': 'Imosec',
        'description': 'Antidiarreico para controle de evacuações frequentes.',
        'price': 6.35,
        'stock': 30,
        'category': 'Antidiarreico',
        'prescription_required': False,
        'manufacturer': 'Janssen',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Floratil',
        'description': 'Probiótico para equilíbrio da flora intestinal.',
        'price': 11.20,
        'stock': 35,
        'category': 'Probiótico',
        'prescription_required': False,
        'manufacturer': 'Merck',
        'dosage_form': 'Pó oral',
        'administration_route': 'Oral'
    },
    {
        'name': 'Neosoro',
        'description': 'Descongestionante nasal com ação rápida.',
        'price': 5.10,
        'stock': 60,
        'category': 'Descongestionante',
        'prescription_required': False,
        'manufacturer': 'Neo Química',
        'dosage_form': 'Solução nasal',
        'administration_route': 'Nasal'
    },
    {
        'name': 'Buscopan',
        'description': 'Antiespasmódico indicado para cólicas intestinais e abdominais.',
        'price': 9.90,
        'stock': 50,
        'category': 'Antiespasmódico',
        'prescription_required': False,
        'manufacturer': 'Sanofi',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    },
    {
        'name': 'Ranitidina',
        'description': 'Bloqueador da acidez gástrica usado em refluxos e úlceras.',
        'price': 13.00,
        'stock': 45,
        'category': 'Antiácido',
        'prescription_required': True,
        'manufacturer': 'Medley',
        'dosage_form': 'Comprimido',
        'administration_route': 'Oral'
    }
]

    
    for product in products:
        Product.add_product(
            name=product['name'],
            description=product['description'],
            price=product['price'],
            stock=product['stock'],
            category=product['category'],
            prescription_required=product['prescription_required'],
            manufacturer=product['manufacturer'],
            dosage_form=product['dosage_form'],
            administration_route=product['administration_route']
        )
    
    # Adicionar FAQs de exemplo
    faqs = [
        {
            'question': 'Preciso de receita para comprar antibióticos?',
            'answer': 'Sim, a venda de antibióticos só pode ser realizada mediante apresentação de receita médica, conforme legislação da Anvisa.',
            'category': 'Receitas'
        },
        {
            'question': 'Vocês aplicam vacinas na farmácia?',
            'answer': 'Sim, aplicamos algumas vacinas na farmácia. Consulte a disponibilidade e agende previamente.',
            'category': 'Serviços'
        },
        {
            'question': 'Vocês medem pressão arterial e glicose?',
            'answer': 'Sim, oferecemos serviços de aferição de pressão arterial e teste de glicose. Consulte nossa equipe para mais informações.',
            'category': 'Serviços'
        },
        {
            'question': 'É possível fazer cadastro para receber promoções?',
            'answer': 'Sim, você pode se cadastrar em nossa loja ou pelo site para receber promoções e ofertas exclusivas.',
            'category': 'Promoções'
        },
        {
            'question': 'Como funciona o programa de fidelidade da farmácia?',
            'answer': 'Nosso programa de fidelidade oferece pontos a cada compra, que podem ser trocados por descontos em produtos selecionados.',
            'category': 'Fidelidade'
        },
        {
            'question': 'Vocês vendem medicamentos manipulados?',
            'answer': 'Atualmente não trabalhamos com manipulação de medicamentos, apenas com produtos industrializados.',
            'category': 'Medicamentos'
        },
        {
            'question': 'Posso trocar um produto comprado na farmácia?',
            'answer': 'Sim, produtos podem ser trocados em até 7 dias com nota fiscal, desde que estejam lacrados e sem uso.',
            'category': 'Trocas e Devoluções'
        },
        {
            'question': 'Vocês possuem estacionamento para clientes?',
            'answer': 'Sim, temos estacionamento gratuito disponível para nossos clientes.',
            'category': 'Infraestrutura'
        },
        {
            'question': 'Tem desconto para convênios ou planos de saúde?',
            'answer': 'Sim, trabalhamos com diversos convênios e planos de desconto. Consulte nossa equipe para verificar elegibilidade.',
            'category': 'Descontos'
        },
        {
            'question': 'Quais são os canais de atendimento da farmácia?',
            'answer': 'Você pode nos contatar pelo telefone, WhatsApp, redes sociais ou diretamente em nossa loja física.',
            'category': 'Atendimento'
        },
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
            'question': 'Conhecer Loja',
            'answer': 'Nossa Loja fica em Colina de Laranjeiras, 123 - Serra. Venha nos fazer uma visita, será um prazer ter você aqui!',
            'category': 'Introdução'
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


from models import Product, FAQ


def initialize_sample_data():
    """Inicializa dados de exemplo para o bot"""
    
    # Adicionar produtos de exemplo
    products = [
    {
        "name": "AAS (Ácido Acetilsalicílico)",
        "principio_ativo": "Ácido Acetilsalicílico",
        "description": "Analgésico, antitérmico e antiagregante plaquetário, usado para dores leves e prevenção cardiovascular.",
        "category": "Analgésico/Antitérmico",
        "manufacturer": "Bayer",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/acido-acetilsalicilico/bula",
        "indicacao": ["dor", "febre", "cefaleia", "prevenção cardiovascular", "antiagregante plaquetário", "dores leves"]
    },
    {
        "name": "Advil (Ibuprofeno)",
        "principio_ativo": "Ibuprofeno",
        "description": "Anti-inflamatório não esteroidal para alívio de dores, inflamações e febre.",
        "category": "Analgésico/Anti-inflamatório",
        "manufacturer": "Pfizer",
        "dosage_form": "Comprimido revestido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/advil-400mg/bula",
        "indicacao": ["inflamação", "dor muscular", "artralgia", "febre", "cólica menstrual", "dor de dente"]
    },
    {
        "name": "Alivium (Paracetamol)",
        "principio_ativo": "Paracetamol",
        "description": "Analgésico e antitérmico para alívio de dores e febre, com versão pediátrica em gotas.",
        "category": "Analgésico/Antitérmico",
        "manufacturer": "Mantecorp",
        "dosage_form": "Gotas/Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/alivium/bula",
        "indicacao": ["febre", "dor leve", "dor moderada", "cefaleia", "estado febril", "mal-estar"]
    },
    {
        "name": "Benegrip",
        "principio_ativo": "Paracetamol + Maleato de clorfeniramina + Cloridrato de fenilefrina",
        "description": "Combinação antigripal com analgésico, antialérgico e descongestionante para sintomas de gripe.",
        "category": "Antigripal",
        "manufacturer": "Hypera Pharma",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/benegrip-multi-dia/bula",
        "indicacao": ["gripe", "resfriado", "coriza", "congestão nasal", "espirros", "febre", "dor de garganta"]
    },
    {
        "name": "Bepantol",
        "principio_ativo": "Dexpantenol",
        "description": "Pomada dermatológica para prevenção e tratamento de assaduras e irritações cutâneas.",
        "category": "Cicatrizante/Dermatológico",
        "manufacturer": "Bayer",
        "dosage_form": "Creme",
        "administration_route": "Tópico",
        "link_bula": "https://www.dormaissaude.com.br/bulario/bepantol",
        "indicacao": ["assadura", "irritação cutânea", "pele ressecada", "cicatrização", "dermatite", "queimadura leve"]
    },
    {
        "name": "Buscopan",
        "principio_ativo": "Butilescopolamina",
        "description": "Antiespasmódico para alívio de cólicas intestinais e abdominais.",
        "category": "Antiespasmódico",
        "manufacturer": "Sanofi",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/buscopan/bula",
        "indicacao": ["cólica intestinal", "dor abdominal", "espasmo gastrointestinal", "cólica menstrual", "dores abdominais"]
    },
    {
        "name": "Cimegripe",
        "principio_ativo": "Paracetamol + Maleato de clorfeniramina + Cloridrato de fenilefrina",
        "description": "Medicamento combinado para alívio dos sintomas de gripes e resfriados.",
        "category": "Antigripal",
        "manufacturer": "Cimed",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/cimegripe/bula",
        "indicacao": ["gripe", "resfriado", "febre", "coriza", "congestão nasal", "dor no corpo"]
    },
    {
        "name": "Citoneurin",
        "principio_ativo": "Vitamina B1 + B6 + B12",
        "description": "Complexo vitamínico B para complementação nutricional e apoio ao sistema nervoso.",
        "category": "Vitamina B",
        "manufacturer": "Apsen",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/citoneurin/bula",
        "indicacao": ["deficiência vitamínica", "neuropatia", "cãibra", "formigamento", "suplementação vitamínica"]
    },
    {
        "name": "Coristina D",
        "principio_ativo": "Paracetamol + Maleato de clorfeniramina + Cloridrato de fenilefrina",
        "description": "Antigripal com ação analgésica, antialérgica e descongestionante.",
        "category": "Antigripal",
        "manufacturer": "GSK",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/coristina-d-pro/bula",
        "indicacao": ["gripe", "resfriado", "rinite alérgica", "obstrução nasal", "espirros", "prurido nasal"]
    },
    {
        "name": "Dexametasona",
        "principio_ativo": "Dexametasona",
        "description": "Corticoide com ação anti-inflamatória e antialérgica em baixas dosagens.",
        "category": "Anti-inflamatório",
        "manufacturer": "EMS",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/dexametasona/bula",
        "indicacao": ["inflamação", "alergia", "reação alérgica", "processos inflamatórios", "edema"]
    },
    {
        "name": "Dipirona Sódica",
        "principio_ativo": "Dipirona monoidratada",
        "description": "Analgésico, antitérmico e antiespasmódico para dores diversas e febre.",
        "category": "Analgésico/Antitérmico",
        "manufacturer": "Sanofi",
        "dosage_form": "Gotas/Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/dipirona-monoidratada/bula",
        "indicacao": ["febre", "dor", "cólica", "cefaleia", "dor de dente", "mal-estar"]
    },
    {
        "name": "Dorflex",
        "principio_ativo": "Dipirona sódica + Citrato de orfenadrina",
        "description": "Associação analgésica com relaxante muscular para dores musculares e cefaleias.",
        "category": "Relaxante Muscular",
        "manufacturer": "Sanofi",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/dorflex/bula",
        "indicacao": ["contratura muscular", "dor nas costas", "tensão muscular", "cefaleia tensional", "lombalgia"]
    },
    {
        "name": "Doralgina",
        "principio_ativo": "Dipirona sódica + Cafeína",
        "description": "Analgésico composto para alívio de dores de cabeça e musculares.",
        "category": "Analgésico",
        "manufacturer": "Sanofi",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/doralgina/bula",
        "indicacao": ["enxaqueca", "cefaleia", "dor muscular", "fadiga", "estado gripal"]
    },
    {
        "name": "Dramin",
        "principio_ativo": "Dimenidrinato",
        "description": "Antiemético para prevenção e tratamento de náuseas e vômitos, incluindo enjoo de movimento.",
        "category": "Antiemético",
        "manufacturer": "Hypera Pharma",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/dramin/bula",
        "indicacao": ["náusea", "vômito", "enjoo de viagem", "vertigem", "labirintite", "cinetose"]
    },
    {
        "name": "Engov",
        "principio_ativo": "Ácido acetilsalicílico + Citrato de cafeína + Hidróxido de alumínio",
        "description": "Medicamento para alívio dos sintomas da ressaca, incluindo dor de cabeça e desconforto gástrico.",
        "category": "Antiressaca",
        "manufacturer": "Hypera Pharma",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/engov/bula",
        "indicacao": ["ressaca", "cefaleia", "azia", "mal-estar gástrico", "indigestão", "queimação"]
    },
    {
        "name": "ENO",
        "principio_ativo": "Bicarbonato de sódio + Carbonato de sódio + Ácido cítrico",
        "description": "Antiácido efervescente para alívio rápido da azia e má digestão.",
        "category": "Antiácido",
        "manufacturer": "GSK",
        "dosage_form": "Pó efervescente",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/sal-de-frutas-eno/bula",
        "indicacao": ["azia", "queimação", "má digestão", "dispepsia", "pirose", "estômago pesado"]
    },
    {
        "name": "Epocler",
        "principio_ativo": "Ácido cítrico + Bicarbonato de sódio + Sulfato de sódio",
        "description": "Digestivo e desintoxicante hepático para alívio de desconfortos digestivos.",
        "category": "Digestivo",
        "manufacturer": "Sanofi",
        "dosage_form": "Solução oral",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/epocler/bula",
        "indicacao": ["má digestão", "desconforto abdominal", "excesso alimentar", "desintoxicação hepática", "empachamento"]
    },
    {
        "name": "Estomazil",
        "principio_ativo": "Hidróxido de alumínio + Hidróxido de magnésio + Dimeticona",
        "description": "Antiácido e antiflatulento para alívio de queimação e desconforto estomacal.",
        "category": "Antiácido",
        "manufacturer": "Hypera Pharma",
        "dosage_form": "Suspensão oral",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/estomazil/bula",
        "indicacao": ["azia", "gastrite", "queimação", "gases", "eructação", "dispepsia"]
    },
    {
        "name": "Flanax",
        "principio_ativo": "Naproxeno sódico",
        "description": "Anti-inflamatório não esteroidal para dores musculares e articulares.",
        "category": "Anti-inflamatório",
        "manufacturer": "Bayer",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/flanax/bula",
        "indicacao": ["artrite", "artralgia", "dor nas costas", "dor muscular", "inflamação", "tendinite"]
    },
    {
        "name": "Gastrol",
        "principio_ativo": "Hidróxido de alumínio + Hidróxido de magnésio",
        "description": "Antiácido para alívio da azia e má digestão.",
        "category": "Antiácido",
        "manufacturer": "Neo Química",
        "dosage_form": "Suspensão oral",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/gastrol/bula",
        "indicacao": ["azia", "queimação", "gastrite", "refluxo", "pirose", "dispepsia"]
    },
    {
        "name": "Hixizine",
        "principio_ativo": "Cloridrato de hidroxizina",
        "description": "Antialérgico para tratamento de urticárias e reações alérgicas cutâneas.",
        "category": "Antialérgico",
        "manufacturer": "Aché",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/hixizine/bula",
        "indicacao": ["urticária", "prurido", "alergia cutânea", "dermatite alérgica", "coceira", "reação alérgica"]
    },
    {
        "name": "Ibupril (Ibuprofeno)",
        "principio_ativo": "Ibuprofeno",
        "description": "Anti-inflamatório para dores leves a moderadas e processos inflamatórios.",
        "category": "Anti-inflamatório",
        "manufacturer": "Hypera Pharma",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/ibupril-comprimido/bula",
        "indicacao": ["dor de garganta", "dor de ouvido", "dor muscular", "artrite", "inflamação", "febre"]
    },
    {
        "name": "Loratadina",
        "principio_ativo": "Loratadina",
        "description": "Antialérgico de segunda geração para rinite alérgica e urticária, sem sonolência.",
        "category": "Antialérgico",
        "manufacturer": "EMS",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/loratadina/bula",
        "indicacao": ["rinite alérgica", "urticária", "alergia respiratória", "espirros", "prurido", "conjuntivite alérgica"]
    },
    {
        "name": "Losartana Potássica",
        "principio_ativo": "Losartana potássica",
        "description": "Anti-hipertensivo em baixas dosagens para controle da pressão arterial.",
        "category": "Anti-hipertensivo",
        "manufacturer": "EMS",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/losartana-potassica/bula",
        "indicacao": ["hipertensão", "pressão alta", "proteção cardiovascular", "doença renal diabética"]
    },
    {
        "name": "Maracugina",
        "principio_ativo": "Passiflora incarnata",
        "description": "Ansiolítico natural à base de passiflora para quadros leves de ansiedade.",
        "category": "Calmante Natural",
        "manufacturer": "Aché",
        "dosage_form": "Solução oral",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/maracugina/bula",
        "indicacao": ["ansieade", "ansiedade leve", "agitação", "nervosismo", "irritabilidade", "distúrbios do sono"]
    },
    {
        "name": "Maxalgina",
        "principio_ativo": "Dipirona sódica",
        "description": "Analgésico e antitérmico para dores moderadas e febre.",
        "category": "Analgésico",
        "manufacturer": "Aché",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/maxalgina-solucao-oral/bula",
        "indicacao": ["dor aguda", "febre", "cólica renal", "dor pós-operatória", "dor de cabeça"]
    },
    {
        "name": "Melhoral",
        "principio_ativo": "Ácido acetilsalicílico + Cafeína",
        "description": "Analgésico composto para alívio de dores leves e febre.",
        "category": "Analgésico",
        "manufacturer": "Hypera Pharma",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/melhoral/bula",
        "indicacao": ["dor leve", "febre", "mal-estar", "cefaleia", "dor de dente", "estado gripal"]
    },
    {
        "name": "Mioflex",
        "principio_ativo": "Carisoprodol + Paracetamol + Cafeína",
        "description": "Relaxante muscular para contraturas e dores musculares leves.",
        "category": "Relaxante Muscular",
        "manufacturer": "Aché",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/mioflex/bula",
        "indicacao": ["contratura muscular", "tensão muscular", "torcicolo", "lombalgia", "distensão muscular"]
    },
    {
        "name": "Multigrip",
        "principio_ativo": "Paracetamol + Maleato de clorfeniramina + Cloridrato de fenilefrina",
        "description": "Associação de fármacos para tratamento sintomático de gripes e resfriados.",
        "category": "Antigripal",
        "manufacturer": "Cimed",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/multigrip/bula",
        "indicacao": ["gripe", "resfriado", "coriza", "obstrução nasal", "espirros", "febre"]
    },
    {
        "name": "Neosaldina",
        "principio_ativo": "Dipirona sódica + Mucato de isometepteno + Cafeína",
        "description": "Analgésico combinado para dores de cabeça, incluindo enxaquecas leves.",
        "category": "Analgésico",
        "manufacturer": "Takeda",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/neosaldina/bula",
        "indicacao": ["enxaqueca", "cefaleia tensional", "dor de cabeça", "migrânea", "cefaleia vascular"]
    },
    {
        "name": "Neosoro",
        "principio_ativo": "Cloreto de sódio",
        "description": "Descongestionante nasal para alívio da congestão em rinites e resfriados.",
        "category": "Descongestionante Nasal",
        "manufacturer": "Neo Química",
        "dosage_form": "Solução nasal",
        "administration_route": "Nasal",
        "link_bula": "https://consultaremedios.com.br/neosoro/bula",
        "indicacao": ["congestão nasal", "rinite", "resfriado", "sinusite", "obstrução nasal", "secreção nasal"]
    },
    {
        "name": "Nervocalm",
        "principio_ativo": "Passiflora incarnata + Crataegus oxyacantha + Valeriana officinalis",
        "description": "Fitoterápico com ação calmante para quadros leves de ansiedade e irritabilidade.",
        "category": "Ansiolítico Natural",
        "manufacturer": "Aché",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/nervocalm/bula",
        "indicacao": ["ansiedade leve", "irritabilidade", "agitação nervosa", "distúrbios do sono", "estresse"]
    },
    {
        "name": "Nimesulida",
        "principio_ativo": "Nimesulida",
        "description": "Anti-inflamatório não esteroidal para dores agudas e processos inflamatórios.",
        "category": "Anti-inflamatório",
        "manufacturer": "EMS",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/nimesulida/bula",
        "indicacao": ["dor articular", "tendinite", "bursite", "dor pós-operatória", "inflamação", "artrose"]
    },
    {
        "name": "Omeprazol",
        "principio_ativo": "Omeprazol",
        "description": "Inibidor da bomba de prótons para azia e desconfortos gástricos.",
        "category": "Antiácido",
        "manufacturer": "EMS",
        "dosage_form": "Cápsula",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/omeprazol/bula",
        "indicacao": ["azia", "gastrite", "refluxo gastroesofágico", "úlcera gástrica", "dispepsia", "queimação"]
    },
    {
        "name": "Paracetamol",
        "principio_ativo": "Paracetamol",
        "description": "Analgésico e antitérmico para dores leves e moderadas e controle da febre.",
        "category": "Analgésico/Antitérmico",
        "manufacturer": "EMS",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/paracetamol/bula",
        "indicacao": ["febre", "dor de cabeça", "dor de dente", "dor muscular", "mal-estar", "estado gripal"]
    },
    {
        "name": "Polaramine",
        "principio_ativo": "Maleato de dexclorfeniramina",
        "description": "Antialérgico para tratamento de alergias e reações alérgicas cutâneas.",
        "category": "Antialérgico",
        "manufacturer": "GSK",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/polaramine/bula",
        "indicacao": ["urticária", "rinite alérgica", "conjuntivite alérgica", "prurido", "alergia cutânea", "picada de inseto"]
    },
    {
        "name": "Puran T4",
        "principio_ativo": "Levotiroxina sódica",
        "description": "Hormônio tireoidiano em dosagens baixas para reposição hormonal leve.",
        "category": "Hormônio Tireoidiano",
        "manufacturer": "Sanofi",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/puran-t4/bula",
        "indicacao": ["hipotireoidismo", "reposição hormonal", "bócio", "deficiência de tireoide"]
    },
    {
        "name": "Resfenol",
        "principio_ativo": "Paracetamol + Maleato de clorfeniramina + Cloridrato de fenilefrina",
        "description": "Antigripal para alívio dos sintomas de gripes e resfriados.",
        "category": "Antigripal",
        "manufacturer": "Hypera Pharma",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/resfenol/bula",
        "indicacao": ["gripe", "resfriado", "febre", "dor no corpo", "coriza", "congestão nasal"]
    },
    {
        "name": "Rinosoro",
        "principio_ativo": "Cloreto de sódio",
        "description": "Solução nasal isotônica para higiene e hidratação das vias nasais.",
        "category": "Solução Nasal",
        "manufacturer": "Aché",
        "dosage_form": "Spray nasal",
        "administration_route": "Nasal",
        "link_bula": "https://consultaremedios.com.br/rinosoro/bula",
        "indicacao": ["higiene nasal", "rinite", "ressecamento nasal", "sinusite", "obstrução nasal", "alergia respiratória"]
    },
    {
        "name": "Sal de Fruta ENO",
        "principio_ativo": "Bicarbonato de sódio + Carbonato de sódio + Ácido cítrico",
        "description": "Antiácido efervescente para alívio rápido da azia e má digestão.",
        "category": "Antiácido",
        "manufacturer": "GSK",
        "dosage_form": "Pó efervescente",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/sal-de-frutas-eno/bula",
        "indicacao": ["azia", "queimação", "má digestão", "dispepsia", "estômago pesado", "excesso alimentar"]
    },
    {
        "name": "Simeco Plus",
        "principio_ativo": "Hidróxido de alumínio + Hidróxido de magnésio + Dimeticona",
        "description": "Antiácido e antiflatulento para alívio de queimação e gases intestinais.",
        "category": "Antiácido",
        "manufacturer": "Hypera Pharma",
        "dosage_form": "Suspensão oral",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/simeco-plus/bula",
        "indicacao": ["azia", "gases", "flatulência", "eructação", "distensão abdominal", "dispepsia"]
    },
    {
        "name": "Torsilax",
        "principio_ativo": "Paracetamol + Carisoprodol + Cafeína",
        "description": "Associação analgésica com relaxante muscular para dores musculares intensas.",
        "category": "Relaxante Muscular",
        "manufacturer": "Aché",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/torsilax/bula",
        "indicacao": ["contratura muscular", "lombalgia", "tensão muscular", "torcicolo", "dor nas costas", "espasmo muscular"]
    },
    {
        "name": "Tylenol (Paracetamol)",
        "principio_ativo": "Paracetamol",
        "description": "Analgésico e antitérmico para dores leves a moderadas e controle da febre.",
        "category": "Analgésico/Antitérmico",
        "manufacturer": "Janssen",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/tylenol-comprimido/bula",
        "indicacao": ["febre", "dor de cabeça", "dor muscular", "dor de dente", "mal-estar", "estado gripal"]
    },
    {
        "name": "Valda",
        "principio_ativo": "Levomentol + Óleo essencial de eucalipto",
        "description": "Xarope para alívio sintomático de irritações na garganta.",
        "category": "Pastilha Garganta",
        "manufacturer": "GSK",
        "dosage_form": "Xarope",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/valda-xarope-adulto/bula",
        "indicacao": ["irritação na garganta", "tosse", "rouquidão", "inflamação na garganta", "resfriado"]
    },
    {
        "name": "Vick Pyrena",
        "principio_ativo": "Paracetamol + Maleato de clorfeniramina + Cloridrato de fenilefrina",
        "description": "Analgésico e antitérmico para dores e febre associadas a gripes.",
        "category": "Analgésico",
        "manufacturer": "GSK",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/vick-pyrena/bula",
        "indicacao": ["gripe", "resfriado", "febre", "dor no corpo", "coriza", "congestão nasal"]
    },
    {
        "name": "Vick Vaporub",
        "principio_ativo": "Óleo de terebintina + Mentol + Cânfora + Óleo de eucalipto",
        "description": "Descongestionante tópico para alívio de congestão nasal e tosse.",
        "category": "Descongestionante Tópico",
        "manufacturer": "GSK",
        "dosage_form": "Pomada",
        "administration_route": "Tópico",
        "link_bula": "https://consultaremedios.com.br/vick-vaporub/bula",
        "indicacao": ["congestão nasal", "tosse", "resfriado", "bronquite", "irritação nasal", "descongestionante"]
    },
    {
        "name": "Vitamina C",
        "principio_ativo": "Ácido ascórbico",
        "description": "Suplemento vitamínico para auxílio na imunidade e prevenção de deficiências.",
        "category": "Suplemento Vitamínico",
        "manufacturer": "EMS",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/acido-ascorbico-vitamina-c/bula",
        "indicacao": ["deficiência de vitamina C", "imunidade baixa", "prevenção de resfriados", "cicatrização", "antioxidante"]
    },
    {
        "name": "Xantinon B12",
        "principio_ativo": "Cianocobalamina + Nicotinamida + Cloridrato de piridoxina",
        "description": "Complexo vitamínico hepático com ação desintoxicante e energética.",
        "category": "Vitamina B",
        "manufacturer": "EMS",
        "dosage_form": "Cápsula",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/xantinon/bula",
        "indicacao": ["deficiência vitamínica", "fraqueza", "fadiga", "desintoxicação hepática", "suplementação"]
    },
    {
        "name": "Zina",
        "principio_ativo": "Desloratadina",
        "description": "Antialérgico para tratamento de alergias respiratórias e cutâneas.",
        "category": "Antialérgico",
        "manufacturer": "Aché",
        "dosage_form": "Comprimido",
        "administration_route": "Oral",
        "link_bula": "https://consultaremedios.com.br/zina/bula",
        "indicacao": ["rinite alérgica", "urticária", "prurido", "conjuntivite alérgica", "alergia cutânea", "espirros"]
    }
    ]
    
    for product in products:
        Product.add_product(
            name=product['name'],
            principio_ativo=product['principio_ativo'],
            description=product['description'],
            category=product['category'],
            manufacturer=product['manufacturer'],
            dosage_form=product['dosage_form'],
            administration_route=product['administration_route'],
            link_bula=product['link_bula'],
            indicacao=product['indicacao']
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


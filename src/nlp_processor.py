import spacy
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import json
from models import Product

# Inicializa conjuntos para evitar duplicatas


# Baixar recursos do NLTK (se necessário)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

# Carregar o modelo spaCy para português
nlp = spacy.load('pt_core_news_sm')

# Stopwords em português
try:
    stop_words = set(stopwords.words('portuguese'))
except LookupError:
    nltk.download('stopwords')
    stop_words = set(stopwords.words('portuguese'))

class NLPProcessor:
    """Processador de linguagem natural para o bot de farmácia"""
    
    # Intenções possíveis
    INTENTS = {
    'saudacao': [
        'oi', 'olá', 'ola', 'bom dia', 'boa tarde', 'boa noite',
        'e aí', 'eai', 'fala', 'tudo bem', 'como vai', 'como você está', 'como vc está', 'beleza', 'suave'
    ],
    'despedida': [
        'tchau', 'adeus', 'até logo', 'até mais', 'até amanhã', 'até breve', 'xau',
        'falou', 'fui', 'até', 'nos vemos', 'até a próxima'
    ],
    'agradecimento': [
        'obrigado', 'obrigada', 'valeu', 'agradeço', 'grato', 'grata',
        'muito obrigado', 'muito obrigada', 'brigado', 'brigada', 'thanks', 'vlw'
    ],
    'info_medicamento': [
        'remédio', 'remedio', 'medicamento', 'bula', 'para que serve', 'como tomar',
        'posologia', 'dosagem', 'efeitos colaterais', 'indicações', 'indicação',
        'contraindicação', 'funciona pra quê', 'tem genérico', 'como funciona o remédio'
    ],
    'preco': [
        'preço', 'preco', 'valor', 'custo', 'quanto custa', 'quanto é',
        'qual o preço', 'qual valor', 'caro', 'barato', 'tem promoção', 'tem desconto'
    ],
    'disponibilidade': [
        'tem', 'tem aí', 'disponível', 'disponivel', 'estoque', 'vocês têm', 'voces tem',
        'ainda tem', 'tem disponível', 'encontrei', 'acham fácil', 'tem na loja'
    ],
    'horario': [
        'horário', 'horario', 'funcionamento', 'aberto', 'fechado',
        'abre que horas', 'fecha que horas', 'quando abre', 'quando fecha',
        'qual o horário', 'horário de funcionamento', 'abre hoje', 'tá aberto'
    ],
    'localizacao': [
        'onde', 'endereço', 'endereco', 'localização', 'localizacao',
        'como chegar', 'qual o endereço', 'ponto de referência', 'perto de onde',
        'tem farmácia perto', 'como eu chego aí', 'onde fica'
    ],
    'ajuda': [
        'ajuda', 'help', 'socorro', 'não entendi', 'nao entendi',
        'como funciona', 'o que você faz', 'o que voce faz', 'voltar', 'tô perdido',
        'explica', 'me ajuda', 'como usar o bot', 'o que dá pra fazer'
    ],
    'falar_humano': [
        'atendente', 'humano', 'pessoa', 'farmacêutico', 'farmaceutico', 'gerente',
        'falar com alguém', 'falar com alguem', 'posso falar com alguém?',
        'quero atendimento humano', 'me transfere', 'tem alguém aí?', 'quero ajuda de pessoa'
    ]
}
  

    @staticmethod
    def get_entities_from_products():
        """Extrai entidades dinamicamente dos produtos no banco"""
        produtos = Product.get_all()
        medicamentos = set()
        sintomas = set()
        categorias = set()

        for p in produtos:
            if 'name' in p:
                medicamentos.add(p['name'].lower())
            if 'indicacao' in p:
                sintomas.update([s.lower() for s in p['indicacao']])
            if 'category' in p:
                categorias.add(p['category'].lower())

        return {
            'medicamentos': list(medicamentos),
            'sintomas': list(sintomas),
            'categorias': list(categorias)
        }

    @staticmethod
    def preprocess_text(text):
        """Pré-processa o texto para análise"""
        # Converter para minúsculas
        text = text.lower()
        #
        # Remover caracteres especiais e números
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        
        # Tokenização
        tokens = word_tokenize(text, language='portuguese')
        
        # Remover stopwords
        tokens = [word for word in tokens if word not in stop_words]
        
        return ' '.join(tokens)
    
    @staticmethod
    def identify_intent(text):
        """Identifica a intenção do usuário com base no texto"""
        preprocessed_text = NLPProcessor.preprocess_text(text)
        
        # Pontuação para cada intenção
        intent_scores = {}
        
        for intent, keywords in NLPProcessor.INTENTS.items():
            score = 0
            for keyword in keywords:
                if keyword in preprocessed_text or keyword in text.lower():
                    score += 1
                    # Palavras exatas têm peso maior
                    if keyword == text.lower().strip():
                        score += 2
            
            intent_scores[intent] = score
        
        # Encontrar a intenção com maior pontuação
        max_score = max(intent_scores.values()) if intent_scores else 0
        
        # Se a pontuação máxima for 0, não foi possível identificar a intenção
        if max_score == 0:
            return 'desconhecido'
        
        # Retornar a intenção com maior pontuação
        for intent, score in intent_scores.items():
            if score == max_score:
                return intent
        
    @staticmethod
    def extract_entities(text):
        """Extrai entidades do texto usando spaCy e regras personalizadas"""
        doc = nlp(text.lower())
        extracted_entities = {}

        # spaCy entities (se desejar manter)
        for ent in doc.ents:
            if ent.label_ not in extracted_entities:
                extracted_entities[ent.label_] = []
            extracted_entities[ent.label_].append(ent.text)

        # Entidades do banco de dados
        dynamic_entities = NLPProcessor.get_entities_from_products()
        for entity_type, keywords in dynamic_entities.items():
            if entity_type not in extracted_entities:
                extracted_entities[entity_type] = []

            for keyword in keywords:
                pattern = r'\b' + re.escape(keyword) + r'\b'  # palavra inteira
                if re.search(pattern, text.lower()) and keyword not in extracted_entities[entity_type]:
                    extracted_entities[entity_type].append(keyword)

        return extracted_entities
    
    @staticmethod
    def analyze_text(text):
        """Analisa o texto para identificar intenção e entidades"""
        intent = NLPProcessor.identify_intent(text)
        entities = NLPProcessor.extract_entities(text)
        
        return {
            'intent': intent,
            'entities': entities,
            'original_text': text
        }

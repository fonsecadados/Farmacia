import spacy
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

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
        'saudacao': ['oi', 'olá', 'ola', 'bom dia', 'boa tarde', 'boa noite', 'e aí', 'tudo bem', 'como vai'],
        'despedida': ['tchau', 'adeus', 'até logo', 'até mais', 'até amanhã', 'até breve', 'xau'],
        'agradecimento': ['obrigado', 'obrigada', 'valeu', 'agradeço', 'grato', 'grata', 'thanks'],
        'info_medicamento': ['remédio', 'remedio', 'medicamento', 'bula', 'para que serve', 'como tomar', 'posologia', 'dosagem'],
        'preco': ['preço', 'preco', 'valor', 'custo', 'quanto custa', 'quanto é'],
        'disponibilidade': ['tem', 'disponível', 'disponivel', 'estoque', 'vocês têm', 'voces tem'],
        'horario': ['horário', 'horario', 'funcionamento', 'aberto', 'fechado', 'abre', 'fecha'],
        'localizacao': ['onde', 'endereço', 'endereco', 'localização', 'localizacao', 'como chegar'],
        'ajuda': ['ajuda', 'help', 'socorro', 'não entendi', 'nao entendi', 'como funciona', 'o que você faz', 'o que voce faz', 'voltar'],
        'falar_humano': ['atendente', 'humano', 'pessoa', 'farmacêutico', 'farmaceutico', 'gerente', 'falar com alguém', 'falar com alguem']
    }
    
    # Entidades comuns em farmácias
    ENTITIES = {
        'medicamentos': ['dipirona', 'paracetamol', 'ibuprofeno', 'amoxicilina', 'omeprazol', 'losartana', 'atenolol', 'rivotril', 'neosaldina', 'dorflex'],
        'sintomas': ['dor', 'febre', 'tosse', 'gripe', 'resfriado', 'alergia', 'coceira', 'náusea', 'nausea', 'vômito', 'vomito', 'diarreia'],
        'categorias': ['antibiótico', 'antibiotico', 'analgésico', 'analgesico', 'anti-inflamatório', 'anti-inflamatorio', 'antialérgico', 'antialergico', 'vitamina']
    }
    
    @staticmethod
    def preprocess_text(text):
        """Pré-processa o texto para análise"""
        # Converter para minúsculas
        text = text.lower()
        
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
        entities = {}
        
        # Extrair entidades do spaCy
        for ent in doc.ents:
            if ent.label_ not in entities:
                entities[ent.label_] = []
            entities[ent.label_].append(ent.text)
        
        # Verificar entidades personalizadas
        for entity_type, keywords in NLPProcessor.ENTITIES.items():
            if entity_type not in entities:
                entities[entity_type] = []
            
            for keyword in keywords:
                if keyword in text.lower():
                    entities[entity_type].append(keyword)
        
        return entities
    
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


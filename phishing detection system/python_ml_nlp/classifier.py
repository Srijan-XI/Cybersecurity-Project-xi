import pickle
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class PhishingClassifier:
    def __init__(self, model_path):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
        self.stop_words = set(stopwords.words('english'))
    
    def preprocess(self, url: str):
        # Simple text normalization & feature extraction
        url = url.lower()
        tokens = word_tokenize(url)
        filtered = [w for w in tokens if w.isalnum() and w not in self.stop_words]
        return ' '.join(filtered)
    
    def predict(self, url: str):
        processed = self.preprocess(url)
        features = [processed]  # Extend with vectorizer for real use
        # Here assume model expects pre-processed text features vectorized externally
        prediction = self.model.predict(features)
        probability = self.model.predict_proba(features)[0][1]  # Phishing prob
        return prediction[0], probability

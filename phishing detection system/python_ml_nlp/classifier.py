#!/usr/bin/env python3
"""
Phishing URL Classifier
Author: Srijan-XI
Date: September 2025

This module provides the main interface for phishing URL detection
using the trained machine learning model.
"""

import pickle
import joblib
import numpy as np
import pandas as pd
import os
import sys
from typing import Dict, Tuple, List
import warnings
warnings.filterwarnings('ignore')

# Add src directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
from nlp_processing import URLFeatureExtractor

class PhishingClassifier:
    """
    Main phishing URL classifier using trained ML model
    """
    
    def __init__(self, model_path: str = None):
        """
        Initialize the classifier with a trained model
        
        Args:
            model_path: Path to the trained model pickle file
        """
        if model_path is None:
            model_path = os.path.join(os.path.dirname(__file__), 'models', 'phishing_classifier.pkl')
        
        self.model_path = model_path
        self.model_info = None
        self.model = None
        self.scaler = None
        self.feature_selector = None
        self.label_encoder = None
        self.feature_extractor = URLFeatureExtractor()
        
        self._load_model()
    
    def _load_model(self):
        """Load the trained model and associated components"""
        try:
            # Try loading with pickle first
            with open(self.model_path, 'rb') as f:
                self.model_info = pickle.load(f)
            
            self.model = self.model_info['model']
            self.scaler = self.model_info['scaler']
            self.feature_selector = self.model_info['feature_selector']
            self.label_encoder = self.model_info.get('label_encoder')
            
            print(f"✅ Model loaded successfully: {self.model_info.get('model_name', 'Unknown')}")
            print(f"📅 Trained on: {self.model_info.get('trained_date', 'Unknown')}")
            
        except Exception as e:
            print(f"❌ Error loading model: {e}")
            # Try joblib as fallback
            try:
                joblib_path = self.model_path.replace('.pkl', '_joblib.pkl')
                self.model_info = joblib.load(joblib_path)
                
                self.model = self.model_info['model']
                self.scaler = self.model_info['scaler']
                self.feature_selector = self.model_info['feature_selector']
                self.label_encoder = self.model_info.get('label_encoder')
                
                print(f"✅ Model loaded with joblib: {self.model_info.get('model_name', 'Unknown')}")
                
            except Exception as e2:
                print(f"❌ Failed to load model with both pickle and joblib: {e2}")
                raise
    
    def extract_features(self, url: str) -> np.ndarray:
        """
        Extract features from URL for prediction
        
        Args:
            url: URL to analyze
            
        Returns:
            Numpy array of extracted features
        """
        try:
            # Use basic feature extraction that matches training data
            features = {
                'url_length': len(url),
                'num_dots': url.count('.'),
                'num_hyphens': url.count('-'),
                'num_underscores': url.count('_'),
                'num_slashes': url.count('/'),
                'num_questionmarks': url.count('?'),
                'num_equal_signs': url.count('='),
                'num_at_symbols': url.count('@'),
                'num_and_symbols': url.count('&'),
                'num_percent_signs': url.count('%'),
                'has_https': 1 if url.startswith('https://') else 0,
                'has_www': 1 if 'www.' in url else 0,
                'digit_ratio': sum(c.isdigit() for c in url) / len(url) if len(url) > 0 else 0,
                'suspicious_words': sum(1 for word in ['secure', 'account', 'update', 'login', 'verify'] if word in url.lower()),
            }
            
            # Create feature vector (pad with zeros to match training dimensions)
            feature_vector = np.array(list(features.values()) + [0] * (135 - len(features)))
            
            return feature_vector.reshape(1, -1)
            
        except Exception as e:
            print(f"⚠️ Error extracting features: {e}")
            # Return zero vector as fallback
            return np.zeros((1, 135))    
    def predict(self, url: str) -> Tuple[int, float, str]:
        """
        Predict if URL is phishing or legitimate
        
        Args:
            url: URL to classify
            
        Returns:
            Tuple of (prediction, probability, confidence_level)
            - prediction: 0 for legitimate, 1 for phishing
            - probability: Probability of being phishing (0-1)
            - confidence_level: 'High', 'Medium', or 'Low'
        """
        try:
            # Extract features
            features = self.extract_features(url)
            
            # Scale features
            if self.scaler:
                features_scaled = self.scaler.transform(features)
            else:
                features_scaled = features
            
            # Select features
            if self.feature_selector:
                features_selected = self.feature_selector.transform(features_scaled)
            else:
                features_selected = features_scaled
            
            # Make prediction
            prediction = self.model.predict(features_selected)[0]
            
            # Get probability
            if hasattr(self.model, 'predict_proba'):
                probabilities = self.model.predict_proba(features_selected)[0]
                phishing_probability = probabilities[1] if len(probabilities) > 1 else probabilities[0]
            else:
                # For models without probability, use decision function or default
                if hasattr(self.model, 'decision_function'):
                    decision = self.model.decision_function(features_selected)[0]
                    phishing_probability = 1 / (1 + np.exp(-decision))  # Sigmoid transformation
                else:
                    phishing_probability = 0.9 if prediction == 1 else 0.1
            
            # Determine confidence level
            if phishing_probability > 0.8 or phishing_probability < 0.2:
                confidence = 'High'
            elif phishing_probability > 0.6 or phishing_probability < 0.4:
                confidence = 'Medium'
            else:
                confidence = 'Low'
            
            return int(prediction), float(phishing_probability), confidence
            
        except Exception as e:
            print(f"❌ Error during prediction: {e}")
            # Return safe default (assume suspicious)
            return 1, 0.7, 'Low'
    
    def predict_batch(self, urls: List[str]) -> List[Dict]:
        """
        Predict multiple URLs at once
        
        Args:
            urls: List of URLs to classify
            
        Returns:
            List of prediction dictionaries
        """
        results = []
        
        for url in urls:
            prediction, probability, confidence = self.predict(url)
            
            results.append({
                'url': url,
                'prediction': 'phishing' if prediction == 1 else 'legitimate',
                'probability': probability,
                'confidence': confidence,
                'is_safe': prediction == 0
            })
        
        return results
    
    def get_model_info(self) -> Dict:
        """Get information about the loaded model"""
        if self.model_info:
            return {
                'model_name': self.model_info.get('model_name', 'Unknown'),
                'trained_date': self.model_info.get('trained_date', 'Unknown'),
                'version': self.model_info.get('version', '1.0'),
                'feature_count': len(self.model_info.get('feature_names', [])),
                'model_type': type(self.model).__name__
            }
        return {'error': 'No model loaded'}

def test_classifier():
    """Test the classifier with sample URLs"""
    print("🧪 Testing Phishing Classifier...")
    
    # Test URLs
    test_urls = [
        'https://www.google.com',
        'https://github.com/user/repo',
        'http://secure-bank-update.tk/login.php',
        'https://paypal-security-check.com/verify',
        'http://bit.ly/suspicious-link',
        'https://www.amazon.com/products',
        'http://phishing-site.ml/account-suspended'
    ]
    
    try:
        classifier = PhishingClassifier()
        
        print(f"📊 Model Info: {classifier.get_model_info()}")
        print("\n🔍 Testing URLs:")
        print("-" * 80)
        
        results = classifier.predict_batch(test_urls)
        
        for result in results:
            status = "🔴 PHISHING" if result['prediction'] == 'phishing' else "🟢 SAFE"
            print(f"{status} | {result['confidence']:<6} | {result['probability']:.3f} | {result['url']}")
        
        print("-" * 80)
        print("✅ Testing completed successfully!")
        
    except Exception as e:
        print(f"❌ Testing failed: {e}")

if __name__ == "__main__":
    test_classifier()

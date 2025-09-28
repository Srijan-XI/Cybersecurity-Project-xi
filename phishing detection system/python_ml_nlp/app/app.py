#!/usr/bin/env python3
"""
Flask API for Phishing URL Detection
Author: Cybersecurity Project XI
Date: September 2025

This Flask application provides a REST API for phishing URL detection
using the trained machine learning model.
"""

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sys
import os
import traceback
import logging
from datetime import datetime

# Add parent directory to path to import classifier
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from classifier import PhishingClassifier
except ImportError as e:
    print(f"Error importing classifier: {e}")
    print("Please make sure the classifier module is in the correct location")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Initialize the classifier
try:
    model_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'models', 'phishing_classifier.pkl')
    classifier = PhishingClassifier(model_path)
    logger.info("✅ Phishing classifier loaded successfully")
except Exception as e:
    logger.error(f"❌ Failed to load phishing classifier: {e}")
    classifier = None

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'online',
        'service': 'Phishing Detection API',
        'version': '1.0',
        'timestamp': datetime.now().isoformat(),
        'model_loaded': classifier is not None
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Detailed health check"""
    health_status = {
        'status': 'healthy' if classifier else 'unhealthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'Phishing Detection API',
        'version': '1.0'
    }
    
    if classifier:
        try:
            model_info = classifier.get_model_info()
            health_status['model'] = model_info
        except Exception as e:
            health_status['model_error'] = str(e)
    
    return jsonify(health_status), 200 if classifier else 503

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict if a URL is phishing or legitimate
    
    Expected JSON payload:
    {
        "url": "https://example.com"
    }
    
    Returns:
    {
        "url": "https://example.com",
        "prediction": "phishing" | "legitimate",
        "probability": 0.85,
        "confidence": "High" | "Medium" | "Low",
        "is_safe": true | false,
        "timestamp": "2025-09-29T01:45:00"
    }
    """
    try:
        # Check if classifier is loaded
        if not classifier:
            return jsonify({
                'error': 'Model not loaded',
                'message': 'The phishing detection model could not be loaded'
            }), 503
        
        # Get JSON data
        if not request.is_json:
            return jsonify({
                'error': 'Invalid request',
                'message': 'Request must be JSON'
            }), 400
        
        data = request.get_json()
        
        # Validate URL parameter
        url = data.get('url', '').strip()
        if not url:
            return jsonify({
                'error': 'Missing URL',
                'message': 'URL parameter is required'
            }), 400
        
        # Basic URL validation
        if not (url.startswith('http://') or url.startswith('https://') or url.startswith('ftp://')):
            # Add http:// if no protocol specified
            url = 'http://' + url
        
        # Make prediction
        prediction, probability, confidence = classifier.predict(url)
        
        # Prepare response
        result = {
            'url': url,
            'prediction': 'phishing' if prediction == 1 else 'legitimate',
            'probability': round(float(probability), 4),
            'confidence': confidence,
            'is_safe': prediction == 0,
            'timestamp': datetime.now().isoformat()
        }
        
        # Log the prediction
        logger.info(f"Prediction for {url}: {result['prediction']} (prob: {result['probability']}, conf: {confidence})")
        
        return jsonify(result), 200
        
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        
        return jsonify({
            'error': 'Prediction failed',
            'message': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@app.route('/predict/batch', methods=['POST'])
def predict_batch():
    """
    Predict multiple URLs at once
    
    Expected JSON payload:
    {
        "urls": ["https://example1.com", "https://example2.com"]
    }
    """
    try:
        if not classifier:
            return jsonify({
                'error': 'Model not loaded',
                'message': 'The phishing detection model could not be loaded'
            }), 503
        
        if not request.is_json:
            return jsonify({
                'error': 'Invalid request',
                'message': 'Request must be JSON'
            }), 400
        
        data = request.get_json()
        urls = data.get('urls', [])
        
        if not urls or not isinstance(urls, list):
            return jsonify({
                'error': 'Invalid URLs',
                'message': 'URLs must be provided as a list'
            }), 400
        
        if len(urls) > 100:  # Limit batch size
            return jsonify({
                'error': 'Too many URLs',
                'message': 'Maximum 100 URLs per batch request'
            }), 400
        
        # Process URLs
        processed_urls = []
        for url in urls:
            url = str(url).strip()
            if url and not (url.startswith('http://') or url.startswith('https://')):
                url = 'http://' + url
            processed_urls.append(url)
        
        # Make batch prediction
        results = classifier.predict_batch(processed_urls)
        
        # Add timestamp to each result
        for result in results:
            result['timestamp'] = datetime.now().isoformat()
        
        return jsonify({
            'results': results,
            'total_count': len(results),
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"Error during batch prediction: {str(e)}")
        
        return jsonify({
            'error': 'Batch prediction failed',
            'message': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

@app.route('/model/info', methods=['GET'])
def model_info():
    """Get information about the loaded model"""
    try:
        if not classifier:
            return jsonify({
                'error': 'Model not loaded'
            }), 503
        
        info = classifier.get_model_info()
        info['timestamp'] = datetime.now().isoformat()
        
        return jsonify(info), 200
        
    except Exception as e:
        return jsonify({
            'error': 'Failed to get model info',
            'message': str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'message': 'The requested endpoint does not exist',
        'available_endpoints': [
            'GET /',
            'GET /health',
            'POST /predict',
            'POST /predict/batch',
            'GET /model/info'
        ]
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'message': 'An unexpected error occurred'
    }), 500

if __name__ == '__main__':
    print("\n🚀 Starting Phishing Detection API...")
    print("=" * 50)
    
    if classifier:
        model_info = classifier.get_model_info()
        print(f"📊 Model: {model_info.get('model_name', 'Unknown')}")
        print(f"📅 Trained: {model_info.get('trained_date', 'Unknown')}")
        print(f"🔧 Features: {model_info.get('feature_count', 'Unknown')}")
    else:
        print("❌ No model loaded - API will return errors")
    
    print(f"🌐 API will run on: http://localhost:5000")
    print(f"📋 Available endpoints:")
    print(f"  - GET  /         - Health check")
    print(f"  - GET  /health   - Detailed health status")
    print(f"  - POST /predict  - Single URL prediction")
    print(f"  - POST /predict/batch - Batch URL prediction")
    print(f"  - GET  /model/info - Model information")
    print("=" * 50)
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
        threaded=True
    )

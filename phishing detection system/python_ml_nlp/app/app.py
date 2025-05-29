from flask import Flask, request, jsonify
from classifier import PhishingClassifier
import nltk

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)
model = PhishingClassifier('models/phishing_classifier.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    url = data.get('url', '')
    if not url:
        return jsonify({'error': 'URL missing'}), 400
    
    prediction, prob = model.predict(url)
    result = 'phishing' if prediction == 1 else 'legitimate'
    return jsonify({'result': result, 'probability': prob})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

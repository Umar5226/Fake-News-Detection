from flask import Flask, request, jsonify, render_template
import torch
from transformers import BertTokenizer, BertForSequenceClassification

app = Flask(__name__)

# Load the fine-tuned model and tokenizer
model_path = 'fake_news_model'  # Path to your fine-tuned model
tokenizer_path = 'fake_news_tokenizer'  # Path to your tokenizer

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained("fake_news_tokenizer")

# Load the model
model = BertForSequenceClassification.from_pretrained("fake_news_model")

# Function to predict fake news
def predict_fake_news(text):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    
    # Perform prediction
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Get probabilities
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    prediction = torch.argmax(probs, dim=1).item()
    confidence = probs[0][prediction].item() * 100  # Convert to percentage
    
    return prediction, confidence

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    news_text = data['text']
    
    prediction, confidence = predict_fake_news(news_text)
    
    result = {
        'prediction': 'REAL' if prediction == 0 else 'FAKE',
        'confidence': round(confidence, 2),
        'status': 'success'
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

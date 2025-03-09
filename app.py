import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load the fine-tuned model and tokenizer
model_path = 'fake_news_model'  # Path to your fine-tuned model
tokenizer_path = 'fake_news_tokenizer'  # Path to your tokenizer

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained(tokenizer_path)

# Load the model
model = BertForSequenceClassification.from_pretrained(model_path)

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
    confidence = probs[0][prediction].item()
    
    return prediction, confidence

# Set the title of the app
st.title("Real-Time Fake News Detection App")

# Add a text area for user input
news_text = st.text_area("Enter the news article here:", "")

# Add a button to trigger the prediction
if st.button("Check"):
    if news_text:
        # Step 1: Use the fine-tuned model to predict
        prediction, confidence = predict_fake_news(news_text)
        if prediction == 0:
            st.success(f"This news is REAL. (Confidence: {confidence:.2f})")
        else:
            st.error(f"This news is FAKE. (Confidence: {confidence:.2f})")
    else:
        st.warning("Please enter some text to check.")
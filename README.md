# Real-Time Fake News Detection App

# Overview

This repository contains a Streamlit-based web application for detecting fake news in real-time using a fine-tuned BERT model. The application allows users to input a news article, and it will predict whether the article is real or fake with a confidence score. The model is trained on a dataset of fake and real news articles, and the app leverages the power of the Hugging Face Transformers library to perform the classification.

# Features

- Real-Time Prediction: Users can input a news article, and the app will instantly predict whether it is real or fake.
- Confidence Score: The app provides a confidence score for the prediction, giving users an idea of how certain the model is about its prediction.
- User-Friendly Interface: The app is built using Streamlit, making it easy to use and accessible to non-technical users.
- Fine-Tuned BERT Model: The model is fine-tuned on a dataset of fake and real news articles, ensuring high accuracy in predictions.

# Installation

To run this app locally, follow these steps:

1. Clone the Repository:
   ```bash
   git clone https://github.com/your-username/fake-news-detection-app.git
   cd fake-news-detection-app
   ```

2. Install Dependencies:
   Make sure you have Python 3.7 or higher installed. Then, install the required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the Model and Tokenizer:
   The app uses a pre-trained BERT model and tokenizer. Make sure to download them and place them in the appropriate directories:
   - `fake_news_model`: Directory containing the fine-tuned BERT model.
   - `fake_news_tokenizer`: Directory containing the tokenizer.

4. Run the App:
   Start the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```

5. Access the App:
   Open your web browser and navigate to `http://localhost:8501` to access the app.

# Usage

1. Enter News Article: Paste the text of the news article you want to analyze into the text area provided.
2. Check for Fake News: Click the "Check" button to see the prediction.
3. View Results: The app will display whether the article is real or fake, along with a confidence score.

# Dataset

The model was trained on a combined dataset of fake and real news articles. The dataset includes the following columns:

- title: The title of the news article.
- text: The content of the news article.
- subject: The subject or category of the news article.
- date: The publication date of the article.
- label: A binary label indicating whether the article is fake (1) or real (0).

The dataset was preprocessed and split into training and testing sets before fine-tuning the BERT model.

# Model Training

The BERT model was fine-tuned using the Hugging Face Transformers library. The training process involved the following steps:

1. Tokenization: The text data was tokenized using the BERT tokenizer.
2. Model Training: The BERT model was fine-tuned on the tokenized dataset using the `Trainer` class from the Hugging Face library.
3. Evaluation: The model's performance was evaluated on a test set, and the best model was saved for deployment.

# Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

# Acknowledgments

- Hugging Face: For providing the Transformers library and pre-trained BERT models.
- Streamlit: For making it easy to build and deploy web applications.
- Dataset Providers: For providing the fake and real news datasets used to train the model.

# Contact

For any questions or feedback, feel free to reach out to Muhammad Umer at malikumar4462@gmail.com.

---

Thank you for using the Real-Time Fake News Detection App! We hope it helps you in identifying fake news and promoting factual information.

# Sentiment Analysis API with BentoML

This is a simple machine learning API for sentiment analysis built using Python and BentoML. It predicts whether the given text is **positive** or **negative**.

## 🚀 Features

- Built with Python and BentoML
- Deployed as a REST API
- Supports local and Docker deployment
- Fast inference with adaptive batching

## 🛠️ Tech Stack

- Python 3.11
- BentoML
- scikit-learn
- Docker (for containerization)

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/yourusername/sentiment-api.git
cd sentiment-api

2 . Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

3 . Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt

4 . Save your model using BentoML (if not already done):
python save_model.py

Running the API Locally
To serve the API locally:

bash
Copy
Edit
bentoml serve service:svc
Test using curl:

bash
Copy
Edit
curl -X POST http://localhost:3000/predict -H "Content-Type: application/json" -d '{"text": "I love this product!"}'
🐳 Docker Deployment (Optional)
Containerize the app:

bash
Copy
Edit
bentoml containerize sentiment_service:latest
Run with Docker:

bash
Copy
Edit
docker run -p 3000:3000 sentiment_service:latest


bash
Copy
Edit
python save_model.py


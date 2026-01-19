from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Crear la app
app = FastAPI(title="News Headline Classification API")

# Cargar modelo y vectorizador
model = joblib.load("news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Esquema de entrada
class HeadlineRequest(BaseModel):
    headline: str

# Endpoint principal
@app.post("/predict")
def predict_category(request: HeadlineRequest):
    text_vectorized = vectorizer.transform([request.headline])
    prediction = model.predict(text_vectorized)[0]

    return {
        "headline": request.headline,
        "predicted_category": prediction
    }
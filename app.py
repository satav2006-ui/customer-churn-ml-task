
from pathlib import Path
from typing import List

import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

MODEL_PATH = Path(__file__).parent / "model" / "text_classifier.joblib"

if not MODEL_PATH.exists():
    raise RuntimeError(f"Model file not found: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Real-Time ML Inference API",
    description="FastAPI service for text classification with prediction probabilities.",
    version="1.0.0",
)

class PredictionRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text to classify")

class BatchPredictionRequest(BaseModel):
    texts: List[str] = Field(..., min_length=1)

class PredictionResponse(BaseModel):
    prediction: str
    probability: float
    probabilities: dict[str, float]

@app.get("/")
def root():
    return {
        "service": "Real-Time ML Inference API",
        "status": "running",
        "docs": "/docs",
        "health": "/health",
    }

@app.get("/health")
def health():
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict", response_model=PredictionResponse)
def predict(payload: PredictionRequest):
    text = payload.text.strip()
    if not text:
        raise HTTPException(status_code=422, detail="text must not be empty")

    probabilities = model.predict_proba([text])[0]
    classes = model.classes_
    best_index = int(probabilities.argmax())

    probability_map = {
        str(cls): round(float(prob), 6)
        for cls, prob in zip(classes, probabilities)
    }

    return PredictionResponse(
        prediction=str(classes[best_index]),
        probability=round(float(probabilities[best_index]), 6),
        probabilities=probability_map,
    )

@app.post("/predict/batch")
def predict_batch(payload: BatchPredictionRequest):
    cleaned = [text.strip() for text in payload.texts]
    if any(not text for text in cleaned):
        raise HTTPException(status_code=422, detail="texts must not contain empty strings")

    probabilities = model.predict_proba(cleaned)
    classes = model.classes_

    results = []
    for probs in probabilities:
        best_index = int(probs.argmax())
        results.append({
            "prediction": str(classes[best_index]),
            "probability": round(float(probs[best_index]), 6),
            "probabilities": {
                str(cls): round(float(prob), 6)
                for cls, prob in zip(classes, probs)
            },
        })
    return {"results": results}

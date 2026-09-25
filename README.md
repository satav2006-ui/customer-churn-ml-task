# Task 6: Real-Time ML Inference REST API & Capstone

This repository packages a trained text-classification model behind a production-style FastAPI REST API.

## Task requirements covered

- FastAPI microservice with `/predict`
- JSON request payload
- Prediction probabilities in the response
- Dockerfile for containerization
- Pinned dependencies
- Unit tests for response schema, health check, validation, and batch inference
- End-to-end architecture documentation

## Project structure

```text
task6_ml_inference_api/
├── app.py
├── train_model.py
├── requirements.txt
├── Dockerfile
├── README.md
├── test_api.py
└── model/
    └── text_classifier.joblib
```

## API

### Health check

`GET /health`

### Single prediction

`POST /predict`

Example JSON:

```json
{
  "text": "The spacecraft entered orbit around the planet."
}
```

Example response shape:

```json
{
  "prediction": "sci.space",
  "probability": 0.91,
  "probabilities": {
    "rec.sport.baseball": 0.09,
    "sci.space": 0.91
  }
}
```

### Batch prediction

`POST /predict/batch`

```json
{
  "texts": [
    "The rocket launched into orbit.",
    "The pitcher struck out the batter."
  ]
}
```

## Run locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Open Swagger documentation:

`http://127.0.0.1:8000/docs`

## Run tests

```bash
pytest -q
```

## Run with Docker

```bash
docker build -t task6-ml-api .
docker run -p 8000:8000 task6-ml-api
```

Then open `/docs`.

## Architecture

```text
Client
  |
  | JSON POST /predict
  v
FastAPI application
  |
  v
Input validation
  |
  v
TF-IDF + Logistic Regression model
  |
  v
Prediction + class probabilities
  |
  v
JSON response
```

## Model note

The repository includes a small serialized text-classification model so the API is immediately runnable and self-contained. The same API structure can also load a larger champion model artifact from a previous training task by replacing `model/text_classifier.joblib`, provided its input/output interface remains compatible.

## Certification checklist

- [x] FastAPI service
- [x] `/predict` JSON endpoint
- [x] Prediction probabilities
- [x] Dockerfile
- [x] Pinned dependencies
- [x] Unit tests
- [x] README architecture documentation
- [x] Serialized model artifact

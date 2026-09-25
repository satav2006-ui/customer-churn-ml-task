
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_predict_schema():
    response = client.post(
        "/predict",
        json={"text": "The spacecraft entered orbit around the planet."}
    )
    assert response.status_code == 200
    body = response.json()
    assert "prediction" in body
    assert "probability" in body
    assert "probabilities" in body
    assert isinstance(body["probabilities"], dict)

def test_empty_text_rejected():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422

def test_batch_prediction():
    response = client.post(
        "/predict/batch",
        json={"texts": [
            "The rocket launched into orbit.",
            "The pitcher struck out the batter."
        ]}
    )
    assert response.status_code == 200
    assert len(response.json()["results"]) == 2

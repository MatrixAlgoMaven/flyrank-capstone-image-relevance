from fastapi.testclient import TestClient

from src.app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_validate_metadata_endpoint():
    data = {
        "subject": "red fox",
        "category": "animal",
        "attributes": ["red fur", "pointed ears"],
        "caption": "A red fox standing in grass",
        "confidence": 0.95,
    }

    response = client.post("/metadata/validate", json=data)

    assert response.status_code == 200
    assert response.json()["subject"] == "red fox"
    assert response.json()["confidence"] == 0.95

def test_validate_metadata_rejects_invalid_confidence():
    data = {
        "subject": "red fox",
        "category": "animal",
        "attributes": ["red fur"],
        "caption": "A fox in grass",
        "confidence": 1.5,
    }

    response = client.post("/metadata/validate", json=data)

    assert response.status_code == 422
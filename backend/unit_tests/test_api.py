from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_success():
    response = client.post("/generate", json={"text": "Sam"})
    assert response.status_code == 200 # standard http status - OK

def test_generate_empty_text():
    response = client.post("/generate", json={"text": ""})
    assert response.status_code == 400 # standard http status - BAD
    assert response.json()["detail"] == "Text input is empty"

def test_generate_spacy_text():
    response = client.post("/generate", json={"text": " "})
    assert response.status_code == 400 # standard http status - BAD
    assert response.json()["detail"] == "Text input is empty"

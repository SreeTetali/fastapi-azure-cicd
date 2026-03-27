from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_visitors():
    response = client.get("/api/visitors/")
    assert response.status_code == 200
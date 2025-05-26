from fastapi.testclient import TestClient

from src.main import app


def test_create_initiative_api():
    client = TestClient(app)
    payload = {
        "name": "DSO MVP",
        "description": "Khởi tạo hệ thống",
        "quarter": "Q3/2025",
        "owner_unit": "DSO",
        "expected_outcome": "Hoàn thành dashboard",
    }
    response = client.post("/initiative", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert "id" in data
    assert data["status"] == "draft"
    assert "created_at" in data

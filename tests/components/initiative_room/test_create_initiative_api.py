import pytest
from fastapi.testclient import TestClient
from src.main import app

def test_create_initiative_missing_name():
    client = TestClient(app)
    payload = {
        "description": "Thiếu name",
        "quarter": "Q2/2025",
        "owner_unit": "DSO",
        "expected_outcome": "Test fail case"
    }
    response = client.post("/initiative", json=payload)
    assert response.status_code == 422

def test_create_initiative_invalid_quarter():
    client = TestClient(app)
    payload = {
        "name": "Invalid Quarter",
        "description": "Quý không đúng định dạng",
        "quarter": "2025-Q3",
        "owner_unit": "DSO",
        "expected_outcome": "Test fail case"
    }
    response = client.post("/initiative", json=payload)
    assert response.status_code == 422

def test_create_initiative_null_field():
    client = TestClient(app)
    payload = {
        "name": None,
        "description": "Null name",
        "quarter": "Q2/2025",
        "owner_unit": "DSO",
        "expected_outcome": "Test fail case"
    }
    response = client.post("/initiative", json=payload)
    assert response.status_code == 422
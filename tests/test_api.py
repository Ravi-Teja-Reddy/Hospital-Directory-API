from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_hospital():
    response = client.post("/hospitals", json={
        "name": "Test Hospital",
        "address": "Test Address",
        "phone": "1234567890"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Hospital"
    assert data["address"] == "Test Address"
    assert data["phone"] == "1234567890"
    assert "id" in data

def test_get_all_hospitals():
    response = client.get("/hospitals")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_hospital_by_id():
    response = client.get("/hospitals/1")
    if response.status_code == 200:
        data = response.json()
        assert data["id"] == 1
    else:
        assert response.status_code == 404

def test_update_hospital():
    response = client.put("/hospitals/1", json={
        "name": "Updated Hospital",
        "address": "Updated Address",
        "phone": "9999999999"
    })
    if response.status_code == 200:
        data = response.json()
        assert data["address"] == "Updated Address"
    else:
        assert response.status_code == 404

def test_delete_hospital():
    response = client.delete("/hospitals/1")
    assert response.status_code in (200, 404)  # it may already be deleted

def test_get_invalid_hospital():
    response = client.get("/hospitals/9999")
    assert response.status_code == 404


def test_pagination():
    # Create 5 hospitals
    for i in range(5):
        client.post("/hospitals", json={
            "name": f"Hospital {i}",
            "address": f"Address {i}"
        })

    response = client.get("/hospitals?skip=2&limit=2")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["name"] == "Hospital 2"
    assert data[1]["name"] == "Hospital 3"
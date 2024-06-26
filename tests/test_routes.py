# Built-in modules

# PyPi modules
from fastapi.testclient import TestClient

# Local modules
from surehub_api.main import app

client = TestClient(app)

# Global variables
HOUSEHOLD_ID = 94058
DEVICE_ID = 517977
PET_ID = 169577


def test_dashboard():
    response = client.get("/dashboard")
    assert response.status_code == 200


def test_devices():
    response = client.get("/devices")
    assert response.status_code == 200


def test_devices_id():
    response = client.get(f"/devices/{DEVICE_ID}")
    assert response.status_code == 200


def test_households():
    response = client.get("/households")
    assert response.status_code == 200


def test_households_id():
    response = client.get(f"/households/{HOUSEHOLD_ID}")
    assert response.status_code == 200


def test_households_id_pets():
    response = client.get(f"/households/{HOUSEHOLD_ID}/pets")
    assert response.status_code == 200


def test_households_id_pets_id():
    response = client.get(f"/households/{HOUSEHOLD_ID}/pets/{PET_ID}")
    assert response.status_code == 200


def test_households_id_pets_id_location():
    response = client.get(f"/households/{HOUSEHOLD_ID}/pets/{PET_ID}/location")
    assert response.status_code == 200


def test_households_id_pets_location():
    response = client.get(f"/households/{HOUSEHOLD_ID}/pets/location")
    assert response.status_code == 200


def test_households_id_users():
    response = client.get(f"/households/{HOUSEHOLD_ID}/users")
    assert response.status_code == 200

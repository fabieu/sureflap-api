# Built-in modules

# PyPi modules
from fastapi.testclient import TestClient

# Local modules
from sureflap_api.main import app

client = TestClient(app)


def test_main():
    response = client.get("/")
    assert response.status_code == 200


def test_docs_swagger():
    response = client.get("/docs")
    assert response.status_code == 200


def test_docs_redoc():
    response = client.get("/redoc")
    assert response.status_code == 200

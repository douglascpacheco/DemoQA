import pytest
import time
from utils.api_client import APIClient

# Dados dinâmicos para não ter conflito entre testes
USERNAME = f"testuser_{int(time.time())}"
PASSWORD = "Test@1234"

# --------- Fixtures ---------
@pytest.fixture(scope="module")
def api_client():
    return APIClient()

@pytest.fixture(scope="module")
def create_user(api_client):
    # gera username único a cada execução
    username = f"testuser_{int(time.time())}"
    password = "Test@1234"
    
    response = api_client.create_user(username, password)
    assert response.status_code == 201
    
    return username, password

@pytest.fixture(scope="module")
def auth_token(api_client, create_user):
    username, password = create_user
    response = api_client.generate_token(username, password)
    assert response.status_code == 200

    token = response.json().get("token")
    assert token is not None
    return token

# --------- Testes ---------
def test_create_user(api_client):
    response = api_client.create_user(USERNAME, PASSWORD)
    assert response.status_code == 201
    body = response.json()
    assert body["username"] == USERNAME
    assert "userID" in body

def test_generate_token(api_client, create_user):
    username, password = create_user
    response = api_client.generate_token(username, password)
    assert response.status_code == 200
    body = response.json()
    assert "token" in body
    assert body["token"] is not None

def test_authenticate_user(api_client, create_user, auth_token):
    username, password = create_user
    token = auth_token
    response = api_client.authenticate_user(username, password, token)
    assert response.status_code == 200
    body = response.json()
    assert body is True

def test_authenticate_user_invalid_token(api_client, create_user):
    username, password = create_user
    invalid_token = "invalidtoken123"
    response = api_client.authenticate_user(username, password, invalid_token)
    assert response.status_code == 401
    body = response.json()
    assert body["message"] == "User not authorized!"
    assert body["code"] == "1207"

def test_username_invalid(api_client):
    invalid_username = "nonexistentuser"
    token = auth_token
    response = api_client.authenticate_user(invalid_username, PASSWORD, token)
    assert response.status_code == 404
    body = response.json()
    assert body["message"] == "User not found!"
    assert body["code"] == "1207"
    
def test_create_existing_user(api_client, create_user):
    username, password = create_user
    response = api_client.create_user(username, password)
    assert response.status_code == 406
    body = response.json()
    assert body["message"] == "User exists!"
    assert body["code"] == "1204"


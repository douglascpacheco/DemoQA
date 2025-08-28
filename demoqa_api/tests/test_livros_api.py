import pytest
import time
from utils.api_client import APIClient


# --------- Fixtures ---------
@pytest.fixture(scope="module")
def api_client():
    return APIClient()

@pytest.fixture(scope="module")
def created_user(api_client):
    username = f"testuser_{int(time.time())}"
    password = "Test@1234"
    response = api_client.create_user(username, password)
    assert response.status_code == 201
    user_id = response.json()["userID"]
    return user_id, username, password

@pytest.fixture(scope="module")
def auth_token(api_client, created_user):
    user_id, username, password = created_user
    response = api_client.generate_token(username, password)
    assert response.status_code == 200
    token = response.json()["token"]
    return token

#--------- Testes ---------
def test_livros_api(api_client):
    response = api_client.listar_livros()
    assert response.status_code == 200
    body = response.json()
    assert "books" in body
    assert isinstance(body["books"], list)
    assert len(body["books"]) > 0

def test_alugar_livros_api(api_client, created_user, auth_token):
    # --------- Teste de alugar livros ---------
    user_id, username, password = created_user
    token = auth_token
    # Pega 2 livros para alugar
    livros = api_client.listar_livros().json()["books"][:2]
    isbns = [livro["isbn"] for livro in livros]
    # Aluga os livros
    response = api_client.alugar_livros(user_id, isbns, token)
    assert response.status_code == 201
    # Valida que os livros aparecem no usuário
    usuario = api_client.buscar_usuario(user_id, token).json()
    alugados = [l["isbn"] for l in usuario.get("books", [])]
    for isbn in isbns:
        assert isbn in alugados

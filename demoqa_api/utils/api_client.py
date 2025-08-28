import requests

BASE_ACCOUNT = "https://demoqa.com/Account/v1"
BASE_BOOKS = "https://demoqa.com/BookStore/v1"
    
class APIClient:
      
    # Buscar usuário
    def buscar_usuario(self, user_id, token):
        url = f"{BASE_ACCOUNT}/User/{user_id}"
        headers = {"Authorization": f"Bearer {token}"}
        return requests.get(url, headers=headers)
    
    # Listar livros
    def listar_livros(self):
        return requests.get(f"{BASE_BOOKS}/Books")
    
    # Criar usuário
    def create_user(self, username, password):
        payload = {"userName": username, "password": password}
        return requests.post(f"{BASE_ACCOUNT}/User", json=payload)
    
    # Gerar token
    def generate_token(self, username, password):
        payload = {"userName": username, "password": password}
        return requests.post(f"{BASE_ACCOUNT}/GenerateToken", json=payload)
    
    # Autenticar usuário
    def authenticate_user(self, username, password, token):
        payload = {"userName": username, "password": password}
        headers = {"Authorization": f"Bearer {token}"}
        return requests.post(f"{BASE_ACCOUNT}/Authorized", json=payload, headers=headers)
    
    # Alugar livros
    def alugar_livros(self, user_id, isbns, token):
        url = f"{BASE_BOOKS}/Books"
        payload = {
            "userId": user_id,
            "collectionOfIsbns": [{"isbn": isbn} for isbn in isbns]
        }
        headers = {"Authorization": f"Bearer {token}"}
        return requests.post(url, json=payload, headers=headers)
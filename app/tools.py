import requests
from langchain_core.tools import tool
from langchain_core.pydantic_v1 import BaseModel, Field

API_URL = "http://localhost:5000"  # Ajuste conforme necessário

@tool
def fetch_categories() -> str:
    """
    Busca todas as categorias de produtos.

    Returns:
        str: Lista de categorias ou mensagem de erro.
    """
    response = requests.get(f"{API_URL}/categories")
    if response.status_code == 200:
        return response.json()
    return "Falha ao buscar categorias"

@tool
def fetch_products() -> str:
    """
    Busca a lista de todos os produtos.

    Returns:
        str: Lista de produtos ou mensagem de erro.
    """
    response = requests.get(f"{API_URL}/products")
    if response.status_code == 200:
        return response.json()
    return "Falha ao buscar produtos"

@tool
def fetch_product_description(sku: str) -> str:
    """
    Busca a descrição de um produto pelo SKU.

    Args:
        sku (str): SKU do produto.

    Returns:
        str: Descrição do produto ou mensagem de erro.
    """
    response = requests.get(f"{API_URL}/products/{sku}/description")
    if response.status_code == 200:
        return response.json()
    return f"Falha ao buscar descrição para o SKU {sku}"

@tool
def fetch_product_price(sku: str) -> str:
    """
    Busca o preço de um produto pelo SKU.

    Args:
        sku (str): SKU do produto.

    Returns:
        str: Preço do produto ou mensagem de erro.
    """
    response = requests.get(f"{API_URL}/products/{sku}/price")
    if response.status_code == 200:
        return response.json()['price']
    return f"Falha ao buscar preço para o SKU {sku}"

@tool
def fetch_product_link(sku: str) -> str:
    """
    Busca o link de um produto pelo SKU.

    Args:
        sku (str): SKU do produto.

    Returns:
        str: Link do produto ou mensagem de erro.
    """
    response = requests.get(f"{API_URL}/products/{sku}/link")
    if response.status_code == 200:
        return response.json()
    return f"Falha ao buscar link para o SKU {sku}"

@tool
def add_usuario(nome: str, email: str, telefone: str) -> str:
    """
    Cadastra um novo usuário.

    Args:
        nome (str): Nome do usuário.
        email (str): Email do usuário.
        telefone (str): Telefone do usuário.

    Returns:
        str: Mensagem de sucesso ou erro.
    """
    payload = {"nome": nome, "email": email, "telefone": telefone}
    response = requests.post(f"{API_URL}/usuarios", json=payload)
    if response.status_code == 201:
        return response.json()
    return f"Falha ao cadastrar usuário: {response.json().get('error')}"

@tool
def fetch_usuario(email: str) -> str:
    """
    Busca um usuário pelo email.

    Args:
        email (str): Email do usuário.

    Returns:
        str: Detalhes do usuário ou mensagem de erro.
    """
    response = requests.get(f"{API_URL}/usuarios/{email}")
    if response.status_code == 200:
        return response.json()
    return f"Falha ao buscar usuário com o email {email}"

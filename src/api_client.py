import requests

BASE_URL = "https://dummyjson.com"


def buscar_produtos(limite=30):
    """Busca produtos na API e retorna uma lista de dicionarios."""
    url = f"{BASE_URL}/products"
    parametros = {"limit": limite}

    resposta = requests.get(url, params=parametros, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    return dados.get("products", [])


def buscar_produto_por_id(produto_id):
    """Busca um produto especifico pelo ID."""
    url = f"{BASE_URL}/products/{produto_id}"

    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    return resposta.json()


def buscar_produtos_por_nome(nome):
    """Pesquisa produtos pelo nome."""
    url = f"{BASE_URL}/products/search"
    parametros = {"q": nome}

    resposta = requests.get(url, params=parametros, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    return dados.get("products", [])


def buscar_categorias():
    """Busca as categorias disponiveis."""
    url = f"{BASE_URL}/products/categories"

    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    return resposta.json()

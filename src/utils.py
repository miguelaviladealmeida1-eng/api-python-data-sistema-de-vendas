import json
from pathlib import Path


def salvar_json(dados, nome_arquivo="produtos.json"):
    """Salva dados em JSON dentro da pasta data."""
    pasta = Path("data")
    pasta.mkdir(exist_ok=True)

    caminho = pasta / nome_arquivo

    with caminho.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    return caminho

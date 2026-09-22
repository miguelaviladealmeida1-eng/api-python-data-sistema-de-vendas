from api_client import (
    buscar_categorias,
    buscar_produto_por_id,
    buscar_produtos,
    buscar_produtos_por_nome,
)
from utils import salvar_json


def mostrar_produtos(produtos):
    if not produtos:
        print("\nNenhum produto encontrado.")
        return

    print("\n--- PRODUTOS ---")
    for produto in produtos:
        print(
            f"ID: {produto['id']} | "
            f"{produto['title']} | "
            f"Categoria: {produto['category']} | "
            f"Preco: US$ {produto['price']}"
        )


def menu():
    while True:
        print("\n=== API PYTHON - SISTEMA DE VENDAS ===")
        print("1 - Listar produtos")
        print("2 - Buscar produto por ID")
        print("3 - Pesquisar produto por nome")
        print("4 - Listar categorias")
        print("5 - Salvar produtos em JSON")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ").strip()

        try:
            if opcao == "1":
                produtos = buscar_produtos()
                mostrar_produtos(produtos)

            elif opcao == "2":
                produto_id = int(input("Digite o ID do produto: "))
                produto = buscar_produto_por_id(produto_id)
                mostrar_produtos([produto])

            elif opcao == "3":
                nome = input("Digite o nome do produto: ").strip()
                produtos = buscar_produtos_por_nome(nome)
                mostrar_produtos(produtos)

            elif opcao == "4":
                categorias = buscar_categorias()
                print("\n--- CATEGORIAS ---")
                for categoria in categorias:
                    print(f"- {categoria}")

            elif opcao == "5":
                produtos = buscar_produtos()
                caminho = salvar_json(produtos)
                print(f"\nDados salvos em: {caminho}")

            elif opcao == "0":
                print("Encerrando...")
                break

            else:
                print("Opcao invalida.")

        except ValueError:
            print("Digite um valor numerico valido.")
        except Exception as erro:
            print(f"Erro ao acessar a API: {erro}")


if __name__ == "__main__":
    menu()

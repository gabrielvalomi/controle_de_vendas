from utils import carregar_dados, salvar_dados, gerar_id


def cadastrar_produto():
    dados = carregar_dados()

    try:
        nome = input("Nome do produto: ").strip()
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade em estoque: "))

        produto = {
            "id": gerar_id(dados["produtos"]),
            "nome": nome,
            "preco": preco,
            "quantidade": quantidade
        }

        dados["produtos"].append(produto)
        salvar_dados(dados)

        print("Produto cadastrado com sucesso!")

    except ValueError:
        print("Erro: preço ou quantidade inválidos.")


def listar_produtos():
    dados = carregar_dados()

    if not dados["produtos"]:
        print("Nenhum produto cadastrado.")
        return

    for p in dados["produtos"]:
        print(f'ID: {p["id"]} | {p["nome"]} | R$ {p["preco"]:.2f} | Estoque: {p["quantidade"]}')

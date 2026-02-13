from utils import carregar_dados, salvar_dados, gerar_id


def cadastrar_cliente():
    dados = carregar_dados()

    nome = input("Nome do cliente: ").strip()
    email = input("Email: ").strip()

    cliente = {
        "id": gerar_id(dados["clientes"]),
        "nome": nome,
        "email": email
    }

    dados["clientes"].append(cliente)
    salvar_dados(dados)

    print("Cliente cadastrado com sucesso!")


def listar_clientes():
    dados = carregar_dados()

    if not dados["clientes"]:
        print("Nenhum cliente cadastrado.")
        return

    for c in dados["clientes"]:
        print(f'ID: {c["id"]} | {c["nome"]} | {c["email"]}')

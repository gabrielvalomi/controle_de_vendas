from produtos import cadastrar_produto, listar_produtos
from clientes import cadastrar_cliente, listar_clientes
from vendas import registrar_venda, listar_vendas, relatorio_total_vendido


def menu():
    while True:
        print("\n=== SISTEMA DE CONTROLE DE VENDAS ===")
        print("1 - Cadastrar Produto")
        print("2 - Listar Produtos")
        print("3 - Cadastrar Cliente")
        print("4 - Listar Clientes")
        print("5 - Registrar Venda")
        print("6 - Listar Vendas")
        print("7 - Relatório Total Vendido")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            cadastrar_cliente()
        elif opcao == "4":
            listar_clientes()
        elif opcao == "5":
            registrar_venda()
        elif opcao == "6":
            listar_vendas()
        elif opcao == "7":
            relatorio_total_vendido()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()

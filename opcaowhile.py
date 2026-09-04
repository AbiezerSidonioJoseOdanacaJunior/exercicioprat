opcao = ""

while opcao != "0":
    print("\n1 - Cadastrar equipamento")
    print("2 - Consultar equipamento")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Cadastrando equipamento...")
    elif opcao == "2":
        print("Consultando equipamento...")
    elif opcao == "0":
        print("Programa encerrado.")
    else:
        print("Opção inválida.")
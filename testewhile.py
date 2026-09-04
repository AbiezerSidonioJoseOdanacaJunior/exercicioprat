for teste in range(1, 6):
    print(f"\nTeste {teste} de 5")

    equipamento = input("Nome do equipamento: ")
    funcionamento = input("Está funcionando? (sim/não): ").lower()

    if funcionamento == "sim":
        print(f"{equipamento}: teste aprovado.")
    elif funcionamento == "não":
        print(f"{equipamento}: necessita de manutenção.")
    else:
        print("Resposta inválida.")
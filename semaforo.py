cor = input("Digite uma cor: Verde, amarelo, vermelho: ")

cor = cor.lower()

if cor == "verde":
    print("Sinal aberto pode passar: ")
elif cor == "amarelo":
    print("Sinal está quase fechando, CUIDADO!!!")
elif cor == "vermelho":
    print("Sinal fechado, não pode passar.")
else:
    print("Cor INVALIDO!")
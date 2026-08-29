nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

if imc > 25:
    massa_muscular = int(input("Digite sua massa muscular: "))
    if massa_muscular >= 5:
        print("Pesno Normal: ")
    else:
        print("Acima do peso: ")
elif imc > 18 and imc < 25:
    print("Peso normal")
else:
    print("Voce está muito fraco, procure ajuda!")

print(f"Olá {nome} o seu IMC é: {imc:.2f} ")


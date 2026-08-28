nome = input("Digite o seu nome: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3 ) / 3

if media > 7:
    print("Voce foi aprovado")
elif media > 5 and media < 7:
    print("Recuperação")
else:
    print("Reprovado")
    
print(f"O/a aluno/a {nome} sua media é {media}")
    
#Sistema de Boletim Escolar

LIMITE_ALUNOS = 3
alunos = []

print("=" * 100)
print("SISTEMA DE BOLETIM ESCOLAR")
print("=" * 100)

#Cadastro dos alunos
while len(alunos) < LIMITE_ALUNOS:
    print(f"\nCadastro do aluno {len(alunos) + 1} de {LIMITE_ALUNOS}")

    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    matricula = input("Matrícula: ").strip()

    #Entrada e validação das três notas
    notas = []

    for numero_nota in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a nota {numero_nota}: "))

                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("A nota deve estar entre 0 e 10.")

            except ValueError:
                print("Digite somente números.")

    #Cálculo da média
    media = sum(notas) / len(notas)

    # Classificação do aluno
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    #Dicionário contendo os dados do aluno
    aluno = {
        "nome": nome,
        "email": email,
        "matricula": matricula,
        "nota1": notas[0],
        "nota2": notas[1],
        "nota3": notas[2],
        "media": media,
        "situacao": situacao
    }

    #Adiciona o aluno à lista
    alunos.append(aluno)

    print("Aluno cadastrado com sucesso!")
    print(f"Total cadastrado: {len(alunos)} de {LIMITE_ALUNOS}")


#Contadores das situações
aprovados = 0
recuperacao = 0
reprovados = 0

#Cabeçalho da tabela
print("\n")
print("=" * 125)
print("BOLETIM ESCOLAR")
print("=" * 125)

print(
    f"{'MATRÍCULA':<12}"
    f"{'NOME':<25}"
    f"{'E-MAIL':<30}"
    f"{'NOTA 1':>8}"
    f"{'NOTA 2':>8}"
    f"{'NOTA 3':>8}"
    f"{'MÉDIA':>8}"
    f"{'SITUAÇÃO':>15}"
)

print("-" * 125)

#Exibição dos alunos
for aluno in alunos:
    print(
        f"{aluno['matricula']:<12}"
        f"{aluno['nome'][:24]:<25}"
        f"{aluno['email'][:29]:<30}"
        f"{aluno['nota1']:>8.1f}"
        f"{aluno['nota2']:>8.1f}"
        f"{aluno['nota3']:>8.1f}"
        f"{aluno['media']:>8.1f}"
        f"{aluno['situacao']:>15}"
    )

    if aluno["situacao"] == "Aprovado":
        aprovados += 1
    elif aluno["situacao"] == "Recuperação":
        recuperacao += 1
    else:
        reprovados += 1

print("=" * 125)

#Resumo final
print("\nRESUMO DA TURMA")
print("-" * 30)
print(f"Total de alunos: {len(alunos)}")
print(f"Aprovados: {aprovados}")
print(f"Em recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")
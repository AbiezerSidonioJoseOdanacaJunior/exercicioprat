#Sistema de Boletim Escolar

dados_alunos = [
    ["A001", "Ana Souza", "ana.souza@email.com", 8.0, 7.5, 9.0],
    ["A002", "Bruno Lima", "bruno.lima@email.com", 5.0, 6.0, 5.5],
    ["A003", "Carla Mendes", "carla.mendes@email.com", 3.0, 4.5, 4.0],
    ["A004", "Daniel Alves", "daniel.alves@email.com", 7.0, 8.0, 7.5],
    ["A005", "Eduarda Rocha", "eduarda.rocha@email.com", 6.0, 5.5, 6.5],
    ["A006", "Felipe Martins", "felipe.martins@email.com", 9.0, 8.5, 10.0],
    ["A007", "Gabriela Santos", "gabriela.santos@email.com", 4.0, 3.5, 5.0],
    ["A008", "Henrique Costa", "henrique.costa@email.com", 7.0, 6.5, 8.0],
    ["A009", "Isabela Ribeiro", "isabela.ribeiro@email.com", 5.0, 5.5, 6.0],
    ["A010", "João Oliveira", "joao.oliveira@email.com", 8.0, 9.0, 7.0],

    ["A011", "Karen Fernandes", "karen.fernandes@email.com", 2.0, 4.0, 3.5],
    ["A012", "Lucas Gomes", "lucas.gomes@email.com", 6.0, 7.0, 8.0],
    ["A013", "Mariana Silva", "mariana.silva@email.com", 9.5, 8.0, 9.0],
    ["A014", "Nicolas Pereira", "nicolas.pereira@email.com", 5.0, 6.5, 5.5],
    ["A015", "Olívia Barbosa", "olivia.barbosa@email.com", 4.0, 5.0, 3.0],
    ["A016", "Pedro Henrique", "pedro.henrique@email.com", 7.5, 7.0, 8.5],
    ["A017", "Queila Cardoso", "queila.cardoso@email.com", 6.0, 5.0, 6.5],
    ["A018", "Rafael Teixeira", "rafael.teixeira@email.com", 8.0, 8.0, 9.0],
    ["A019", "Sabrina Freitas", "sabrina.freitas@email.com", 3.5, 4.0, 2.5],
    ["A020", "Thiago Monteiro", "thiago.monteiro@email.com", 7.0, 7.0, 7.0],

    ["A021", "Amanda Nunes", "amanda.nunes@email.com", 5.5, 6.0, 5.0],
    ["A022", "Bernardo Castro", "bernardo.castro@email.com", 9.0, 9.5, 8.5],
    ["A023", "Camila Moura", "camila.moura@email.com", 4.0, 4.5, 5.0],
    ["A024", "Diego Ramos", "diego.ramos@email.com", 6.5, 7.5, 7.0],
    ["A025", "Elisa Moreira", "elisa.moreira@email.com", 5.0, 5.0, 5.0],
    ["A026", "Fernando Melo", "fernando.melo@email.com", 8.0, 7.0, 9.0],
    ["A027", "Giovana Lopes", "giovana.lopes@email.com", 2.5, 3.0, 4.0],
    ["A028", "Heitor Correia", "heitor.correia@email.com", 7.0, 8.5, 8.0],
    ["A029", "Ingrid Araújo", "ingrid.araujo@email.com", 6.0, 5.5, 5.0],
    ["A030", "José Almeida", "jose.almeida@email.com", 9.0, 8.0, 7.5],

    ["A031", "Larissa Vieira", "larissa.vieira@email.com", 4.0, 3.0, 4.5],
    ["A032", "Mateus Dias", "mateus.dias@email.com", 7.5, 6.5, 8.0],
    ["A033", "Natália Borges", "natalia.borges@email.com", 5.0, 6.0, 6.0],
    ["A034", "Otávio Rezende", "otavio.rezende@email.com", 8.5, 9.0, 8.0],
    ["A035", "Paula Carvalho", "paula.carvalho@email.com", 3.0, 5.0, 4.0],
    ["A036", "Renato Marques", "renato.marques@email.com", 7.0, 7.5, 8.0],
    ["A037", "Sara Fonseca", "sara.fonseca@email.com", 6.0, 6.5, 5.5],
    ["A038", "Vinícius Duarte", "vinicius.duarte@email.com", 10.0, 9.0, 9.5],
    ["A039", "Yasmin Campos", "yasmin.campos@email.com", 4.5, 4.0, 3.5],
    ["A040", "Alexandre Pinto", "alexandre.pinto@email.com", 7.0, 6.0, 8.0],

    ["A041", "Beatriz Leal", "beatriz.leal@email.com", 5.5, 5.0, 6.0],
    ["A042", "Caio Moraes", "caio.moraes@email.com", 8.0, 9.0, 8.5],
    ["A043", "Débora Andrade", "debora.andrade@email.com", 3.0, 4.0, 5.0],
    ["A044", "Enzo Neves", "enzo.neves@email.com", 7.0, 7.0, 8.0],
    ["A045", "Flávia Tavares", "flavia.tavares@email.com", 6.0, 5.0, 5.5],
    ["A046", "Gustavo Cunha", "gustavo.cunha@email.com", 9.0, 8.5, 8.0],
    ["A047", "Heloísa Machado", "heloisa.machado@email.com", 4.0, 3.0, 2.5],
    ["A048", "Igor Batista", "igor.batista@email.com", 7.5, 8.0, 7.0],
    ["A049", "Júlia Farias", "julia.farias@email.com", 5.0, 6.0, 5.0],
    ["A050", "Leandro Xavier", "leandro.xavier@email.com", 8.0, 7.0, 9.0]
]


#Lista que receberá os alunos processados
alunos = []


#Cálculo das médias e situações
for dados in dados_alunos:
    matricula = dados[0]
    nome = dados[1]
    email = dados[2]
    nota1 = dados[3]
    nota2 = dados[4]
    nota3 = dados[5]

    notas = [nota1, nota2, nota3]

    #Len(notas) retorna 3
    media = sum(notas) / len(notas)

    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    aluno = {
        "matricula": matricula,
        "nome": nome,
        "email": email,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "situacao": situacao
    }

    alunos.append(aluno)


#Contadores
aprovados = 0
recuperacao = 0
reprovados = 0


#Cabeçalho da tabela
print("=" * 125)
print("BOLETIM ESCOLAR".center(125))
print("=" * 125)

print(
    f"{'MATRÍCULA':<12}"
    f"{'NOME':<25}"
    f"{'E-MAIL':<30}"
    f"{'N1':>7}"
    f"{'N2':>7}"
    f"{'N3':>7}"
    f"{'MÉDIA':>9}"
    f"{'SITUAÇÃO':>18}"
)

print("-" * 125)


#Exibição dos registros
for aluno in alunos:
    print(
        f"{aluno['matricula']:<12}"
        f"{aluno['nome'][:24]:<25}"
        f"{aluno['email'][:29]:<30}"
        f"{aluno['nota1']:>7.1f}"
        f"{aluno['nota2']:>7.1f}"
        f"{aluno['nota3']:>7.1f}"
        f"{aluno['media']:>9.1f}"
        f"{aluno['situacao']:>18}"
    )

    if aluno["situacao"] == "Aprovado":
        aprovados += 1
    elif aluno["situacao"] == "Recuperação":
        recuperacao += 1
    else:
        reprovados += 1


#Resumo
print("=" * 125)
print("RESUMO DA TURMA")
print("-" * 40)

print(f"Total de alunos: {len(alunos)}")
print(f"Alunos aprovados: {aprovados}")
print(f"Alunos em recuperação: {recuperacao}")
print(f"Alunos reprovados: {reprovados}")
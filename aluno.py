class Aluno:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        
    def apresentar(self):
        return f"Eu sou {self.nome} matricula {self.matricula} eu curso {self.curso}"
aluno1 = Aluno("Abiezer", 100, "Analise de DS")
aluno2 = Aluno("Pedro", 200, "Eng. Software")

print(aluno1.apresentar())
print(aluno2.apresentar())
        
class Equipamento:
    def __init__(self, nome, patrimonio):
        self.nome = nome
        self.patrimonio = patrimonio
        self.disponivel = True
        
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f"{self.nome} emprestado com sucesso."
        return f"O equipamento já está esmprestado."
    
    def devolver(self):
        self.disponivel = True
        return f"O {self.nome} devolvido com sucesso."
    
    def exibir_dados(self):
        status = "Disponivel" if self.disponivel else "Emprestado"
        return f"{self.patrimonio} - {self.nome} - {status}"
    
notebook = Equipamento("Notebook Dell", "PAT-001")

print(notebook.exibir_dados())
print(notebook.emprestar())
print(notebook.exibir_dados())
print(notebook.emprestar())
print(notebook.devolver())

        
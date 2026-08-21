class Equipamento:
    def __init__(self, nome, patrimonio):
        self.nome = nome
        self.patrimonio = patrimonio
        self.disponivel = True
        
    def exibir_dados(self):
        status = "Disponivel" if self.disponivel else "Esprestado"
        return f"{self.patrimonio} - {self.nome} - {status}"
    
notebook = Equipamento("Notebook Dell", "PAT-001")
projetor = Equipamento("Projetor Epson", "PAT-002")
    
print(notebook.exibir_dados())
print(projetor.exibir_dados())
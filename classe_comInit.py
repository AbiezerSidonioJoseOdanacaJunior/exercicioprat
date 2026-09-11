class Equipamento:
    def __init__(self, nome, patrimonio):
        self.nome = nome
        self.patrimonio = patrimonio

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Patrimônio: {self.patrimonio}")


# Instanciação com argumentos
notebook = Equipamento("Notebook Dell", "PAT-001")

notebook.exibir_dados()
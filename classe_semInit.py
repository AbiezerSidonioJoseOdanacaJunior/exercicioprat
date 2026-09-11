class Equipamento:
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Patrimônio: {self.patrimonio}")


# Instanciação sem argumentos
notebook = Equipamento()

# Os atributos são adicionados depois
notebook.nome = "Notebook Dell"
notebook.patrimonio = "PAT-001"

notebook.exibir_dados()
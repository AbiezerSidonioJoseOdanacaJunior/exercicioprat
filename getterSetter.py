class Equipamento:
    def __init__(self, nome, custo):
        self.nome = nome
        self.custo = custo  

    # Getter: retornar ou consultar o valor do custo
    @property
    def custo(self):
        return self.__custo

    # Setter: permite alterar e validar o valor do custo
    @custo.setter
    def custo(self, novo_custo):
        if novo_custo < 0:
            print("Erro: o custo não pode ser negativo.")
            return

        self.__custo = novo_custo
        print("Custo cadastrado/alterado com sucesso.")

    def exibir_dados(self):
        print("\nDADOS DO EQUIPAMENTO")
        print(f"Nome: {self.nome}")
        print(f"Custo: R$ {self.custo:.2f}")


# Criando o equipamento e passar o valor do custo
equipamento = Equipamento("Notebook Dell", 3500)

# Exibindo o valor inicial
equipamento.exibir_dados()

# Alterando para um valor válido
print("\nTentando alterar o custo para R$ 4.000,00...")
equipamento.custo = 4000
equipamento.exibir_dados()

# Tentando alterar para um valor inválido
print("\nTentando alterar o custo para R$ -500,00...")
equipamento.custo = -500
equipamento.exibir_dados()
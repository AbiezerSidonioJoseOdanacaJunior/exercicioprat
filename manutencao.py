class Manutencao:
    STATUS_PERMITIDOS = ["Aberta", "Em andamento", "Concluída"]

    def __init__(self, descricao, responsavel, custo, status="Aberta"):
        self.descricao = descricao
        self.responsavel = responsavel
        self.custo = custo
        self.status = status

    # Getter e setter da descrição
    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if not isinstance(nova_descricao, str) or not nova_descricao.strip():
            raise ValueError("A descrição não pode ficar vazia.")

        self.__descricao = nova_descricao.strip()

    # Getter e setter do responsável
    @property
    def responsavel(self):
        return self.__responsavel

    @responsavel.setter
    def responsavel(self, novo_responsavel):
        if not isinstance(novo_responsavel, str) or not novo_responsavel.strip():
            raise ValueError("O responsável não pode ficar vazio.")

        self.__responsavel = novo_responsavel.strip()

    # Getter e setter do custo
    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, novo_custo):
        if not isinstance(novo_custo, (int, float)):
            raise ValueError("O custo deve ser um número.")

        if novo_custo < 0:
            raise ValueError("O custo deve ser maior ou igual a zero.")

        self.__custo = novo_custo

    # Getter e setter do status
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, novo_status):
        if novo_status not in self.STATUS_PERMITIDOS:
            raise ValueError(
                "Status inválido. Use: Aberta, Em andamento ou Concluída."
            )

        self.__status = novo_status

    # Inicia a manutenção
    def iniciar(self):
        if self.status != "Aberta":
            raise ValueError(
                "Somente uma manutenção aberta pode ser iniciada."
            )

        self.status = "Em andamento"
        print("Manutenção iniciada com sucesso.")

    # Conclui a manutenção
    def concluir(self):
        if self.status != "Em andamento":
            raise ValueError(
                "Somente uma manutenção em andamento pode ser concluída."
            )

        self.status = "Concluída"
        print("Manutenção concluída com sucesso.")

    # Exibe os dados
    def exibir_dados(self):
        print("\nDADOS DA MANUTENÇÃO")
        print(f"Descrição: {self.descricao}")
        print(f"Responsável: {self.responsavel}")
        print(f"Custo: R$ {self.custo:.2f}")
        print(f"Status: {self.status}")
class Equipamento:
    def __init__(self, nome, patrimonio, setor="Não informado"):
        nome = nome.strip()
        patrimonio = patrimonio.strip().upper()
        setor = setor.strip()

        if not nome:
            raise ValueError("O nome do equipamento é obrigatório.")

        if not patrimonio:
            raise ValueError("O patrimônio é obrigatório.")

        if not patrimonio.startswith("PAT-"):
            raise ValueError(
                "O patrimônio deve começar com PAT-. Exemplo: PAT-001"
            )

        if not setor:
            setor = "Não informado"

        self.nome = nome
        self.patrimonio = patrimonio
        self.setor = setor
        self.disponivel = True

    def exibir_dados(self):
        status = "Disponível" if self.disponivel else "Em manutenção"

        return (
            f"Nome: {self.nome}\n"
            f"Patrimônio: {self.patrimonio}\n"
            f"Setor: {self.setor}\n"
            f"Status: {status}"
        )


# Teste 1: Exibindo o - equipamento válido
try:
    notebook = Equipamento(
        "Notebook Dell",
        "PAT-001",
        "Laboratório"
    )

    print("\nTESTE 1")
    print(notebook.exibir_dados())

except ValueError as erro:
    print(f"Erro: {erro}")


# Teste 2: Exibindo o erro - nome inválido
try:
    projetor = Equipamento(
        "   ",
        "PAT-002",
        "Audiovisual"
    )

    print("\nTESTE 2")
    print(projetor.exibir_dados())

except ValueError as erro:
    print("\nTESTE 2")
    print(f"Erro: {erro}")


# Teste 3: Exibindo - patrimônio inválido
try:
    impressora = Equipamento(
        "Impressora Epson",
        "003",
        "Secretaria"
    )

    print("\nTESTE 3")
    print(impressora.exibir_dados())

except ValueError as erro:
    print("\nTESTE 3")
    print(f"Erro: {erro}")
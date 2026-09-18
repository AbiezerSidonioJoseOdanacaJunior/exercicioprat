class Loja:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
    @property
    def preco(self):
        return self.__preco
        
    @preco.setter
    def preco(self, novo_preco):
        if novo_preco < 0:
            raise ValueError("O preço tem que ser maior que 0")
        
        self.__preco = novo_preco
        print("Preço cadastrado/alterado com sucesso")
        
    def exibir_informacao(self):
        print("Nome do Produto: ", self.nome)
        print("Preço do produto: ", self.preco)

try:
    produto = Loja("Mouse", 50)
    produto.exibir_informacao()
    
except ValueError as erro:
    print("ERRO", erro)
    
# Testando a regra
print("\nTestando o valor inválido")
try:
    produto.preco = -500
    produto.exibir_informacao()
except ValueError as erro:
    print("ERRO: ", erro)
    
print("\nTestando com valor válido")
try:
    produto.preco = 100
    produto.nome = "----"
    produto.exibir_informacao()
except ValueError as erro:
    print("ERRO: ", erro)
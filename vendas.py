class Vendedor:
    def __init__(self, nome):
        self.nome = nome
        self.meta = 1000
    
    def vender(self):
        self.vendas = 10000
        
        if(self.vendas >= self.meta):
            print("O vendedor bateu a meta: ")
        else:
            print("Infelizmente não bateu a meta")
            
vendedor1 = Vendedor("Abiezer")

print(vendedor1.vender())
                
    
        
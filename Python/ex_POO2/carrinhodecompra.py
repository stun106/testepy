from supermercado import Systemercado
class CarrinhoDeCompras: 
    
    def __init__(self):
        self.Carrinho = []
        self.Mercadinho = Systemercado()
        self.valor = 0

    def addCarrinho(self,a:str)->list:
        print(self.Mercadinho.produtospreços)
        self.Carrinho.append(a)

    def Compra(self,a:str)->float:
      sum(self.Mercadinho.produtospreços.values(a))  
      return self.valor

        
        

    
        
        
        

        
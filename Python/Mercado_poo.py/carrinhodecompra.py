from supermercado import Systemercado
class CarrinhoDeCompras(): 
    
    def __init__(self):
        self.Carrinho = []
        self.item_valor = []
        self.valor = 0

    def addCarrinho(self,a:str)->list:
        self.Carrinho.append(a)
    
    def Desconto(self):
        self.valor -= (10/100)

    def Compra(self,a,y,x ='y'):
        if y == x:
            self.item_valor.append(self.produtospreços.pop(a))
            for x in self.item_valor:
                self.valor += x 
            self.Desconto()
            return self.valor
        else:
            self.item_valor.append(self.produtospreços.pop(a))
            for x in self.item_valor:
                self.valor += x 
            return self.valor


        




        
    

    
        
        
        

        
from cliente import Cliente
class Systemercado(Cliente):
    def __init__(self,Vip = False):
        Cliente. __init__(self,Vip)
        self.produtospreços = {
        'Feijão': 10,
            'Arroz': 5,
            'frango': 18
            }
        
    def Cadastro(self,n:str,c:str,en:str):
        self.pessoa['Nome: '] = n 
        self.pessoa['CPF: '] = c 
        self.pessoa['Endereço: '] = en
        return self.pessoa    

    def ClienteVip (self,a,b ='y')->bool:
        if a == b:
            return True
        else:
            return False

    def resetsystem(self):
        self.pessoa = {}
        self.produtospreços = {}
        self.Carrinho = []
        self.item_valor = []
        self.valor = 0   

        




            


    


        
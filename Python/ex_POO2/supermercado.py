from cliente import Cliente
class Systemercado:
    def __init__(self,Vip = False):
        self.produtospreços = {
            'Feijão': 10.50,
            'Arroz': 5.80,
            'frango': 18.80
            }
        self. Pessoa = Cliente(Vip)


    def Cadastro(self,n:str,c:str,en:str):
        self.Pessoa.pessoa['Nome: '] = n 
        self.Pessoa.pessoa['CPF: '] = c 
        self.Pessoa.pessoa['Endereço: '] = en
        return self.Pessoa.pessoa

    def ClienteVip (self,a, b='y'):
        if a == b:
            print('otimo, para clientes VIP a compra terá 10% de desconto.')
            return True
        else:
            return False

        
        

        
        




            


    


        
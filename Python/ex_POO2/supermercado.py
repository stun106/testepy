from ast import Pass
from Python.ex_POO_Encapsu.pessoa import Pessoa
from cliente import Cliente
class Supermercado:
    def __init__(self,Vip = False, produtos = ['feijão','arroz','cuscuz','frango','farinha'], precos = [10.0, 4.50, 2.50, 23.0, 6.80]) -> list:
        self.produtos = produtos 
        self.preços = precos 
        self. Pessoa = Cliente(Vip)

    @property
    def pessoa(self):
        return self.Pessoa._pessoa
    @pessoa.setter
    def pessoa(self):
        if self.Pessoa._pessoa == self.Pessoa._pessoa.keys(2):
            return self.Pessoa._pessoa
            #cliente vip 10% de desconto 
        else:
            print('você é de menor e não pode ter beneficios')
            #valor do produto sem desconto

    def Cadastro(self,n,c,s,e,en,ida):
        self.Pessoa._pessoa[n] = c
        self.Pessoa._pessoa[s] = ida
        self.Pessoa._pessoa[e] =en


            


    


        
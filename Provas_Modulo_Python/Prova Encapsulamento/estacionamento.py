from datetime import datetime
from Registro import Registro
class estacionamento(Registro):
    def __init__(self):
        Registro.__init__(self)
        self.__valorporHora = 5.0
        self.__Entrada = 0
        self.__Saida = 0
        self.__Dados = {}
        

    
    #metodo importar dados
    @property
    def Dados(self):
        return self.__Dados
    Dados.setter
    def Dados(self):
        self.__Dados[self.Name] = self.Cpf
        self.__Dados[self.Automovel] = self.Modelo
        self.__Dados['Placa'] = self.placa
        self.__Dados['Entrada'] = self.__Entrada
        self.__Dados['Saida'] = self.__Saida
        return self.__Dados
    
    
    #metodos para importar entrada e saida de automoveis
    def addEntrada(self,a:float) -> float:
        self.__Entrada += a
        return self.__Entrada
    
    def addSaida(self,b:float) -> float:
        self.__Saida += b
        return self.__Saida

    
    #Metodos valores
    @property
    def Entrada(self):
        return self.__Entrada
    @Entrada.setter
    def Entrada(self,a):
        self.verificador(a)
        return self.__Entrada

    @property
    def Saida(self):
        return self.__Saida
    @Saida.setter
    def Saida(self,a):
        self.verificador(a)
        return self.__Saida 

    


    
    

    
    
    

    

    

    



    
    



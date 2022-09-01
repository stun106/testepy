from Registro import Registro
class sysEstacionamento(Registro):
    def __init__(self):
        Registro.__init__(self)
        self.__valorporHora = 5.0
        self.__Entrada = []
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
        return self.__Dados
    
    
    #metodos para importar horarios de entrada e saida de automoveis
    def addEntrada(self,a:float) -> float:
        self.__Entrada.append(a)
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
        self.__verificador(a)
        return self.__Entrada

    @property
    def Saida(self):
        return self.__Saida
    @Saida.setter
    def Saida(self,a):
        self.__verificador(a)
        return self.__Saida 

    
    #metodo verificador do sistema de estacionamento
    def __verificador(self,a:bool,b = 'y') -> bool:
        if a == b: 
            return True
        else:
            return ('verifique seus dados!')
    
    

    
    
    

    

    

    



    
    



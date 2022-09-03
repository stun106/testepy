from Registro import Registro
class sysEstacionamento(Registro):
    def __init__(self,name,cpf,tipoauto,model,placa):
        Registro.__init__(self,name,cpf,tipoauto,model,placa)
        self.__Dados = {}
        self.__Entrada = []
        self.__Saida = 0
        self.__valorporHora = 5.0
        self.__valor = 0
        
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

     #Metodos valores
    @property
    def Entrada(self):
        return self.__Entrada
    @Entrada.setter
    def Entrada(self):
        if self.__Entrada[0] < self.__Saida:
            return self.__Entrada

    @property
    def Saida(self):
        return self.__Saida
    @Saida.setter
    def Saida(self,a,b ='y'):
        if a == b:
            return self.__Saida 

    #metodos para importar horarios de entrada e saida de automoveis
    def addEntrada(self,a:float) -> float:
        self.__Entrada.append(a)
        return self.__Entrada
    
    def addSaida(self,b:float) -> float:
        self.__Saida += b
        return self.__Saida

    #Metodos systema de cobrança
    def sysCobranca(self,a:float,b:float) -> int:
        if a < b:
            for i in (self.__Entrada):
                self.__Saida -= i
                self.__valor += self.__Saida
                return int(round(self.__valor* self.__valorporHora))
            self.__resetsys()
        else: 
            return('"Informação incoerente", verifique seus dados!')
        

    """metodos verificadores"""

    #metodo verificador do sistema de estacionamento
    def verificador(self,a:bool,b = 'y') -> bool:
        if a == b: 
            return True
        else:
            return False
    
    #reseta atributos para novos registros
    def __resetsys(self)-> None:
        self.__Dados = {}
        self.__Entrada = []
        self.__Saida = 0
        self.__valorporHora = 5.0
        self.__valor = 0

    
    
    

    

    

    



    
    



from sysRegistro import Registros
from Usefriend import Friends
from UseFamily import Families
from UseGuia import Guias

class Trilhas(Friends,Families,Guias,Registros):
    def __init__(self) -> None:
        self._Trilhas = {
                        'Trilha do Sossego': 12.9,
                        'Dificuldade': 'Moderado'
                        },{
                            'Trilha Rampa do Caim': 13.0,
                            'Dificuldade': 'Facil'
                        }
        self.UserTrilhas = {}
        self.grupo1 = []
        self.grupo2 = []
    
    @property
    def Trilhas(self):
        return self._Trilhas
    Trilhas.setter
    def Trilhas(self):
        self.Trilhas = dict()
        return self._Trilhas
    

    @property
    def selectTrilha1(self):
        return self._UserTrilhas
    selectTrilha1.setter
    def selectTrilha1(self,nome,conection):
        self.grupo1 = list()
        try: 
            if self._Name == nome and self.FriendConection == conection:
                self.grupo1.append(nome)
                for x in self.grupo1:
                    self.UserTrilhas['Trilha do Sussego'] = x
                    return self._UserTrilhas
        except:
            print('Verifique seus Dados')
        else: print('Dados Cadastrados')
    

    def selectTrilha2(self,nome,conection):
        try: 
            self.grupo2.append(nome)
            self.grupo2.append(conection)
            self.UserTrilhas['Trilha Rampa do Caim'] = self.grupo2
        except:
            print('Verifique seus Dados')
 

#teste
# trilha = Trilhas()
# usuario1 = Friends()
# nome = 'ruan'
# idade = 35
# endereco = '25 de março, salvador - ba'
# conection = 'amigo'
# trilha.selectTrilha2(nome,conection)


# usuario2 = Families()
# nome = 'Lailton'
# idade = 35
# endereco = 'Itinga, Lauro de freitas - Ba'
# conection = 'Familia'
# trilha.selectTrilha2(nome,conection)

# print(trilha.UserTrilhas)






    




    




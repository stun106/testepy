from Friend import Friends
from Family import Families
class Methods(Friends,Families):
    
#Encapsulamentos
    @property
    def Name(self):
        return self._Name
    Name.setter
    def Name(self,nome):
        self._Name = nome
        return self._Name
    
    @property
    def Idade(self):
        return self._Age
    Idade.setter
    def Idade(self,idade):
        self._Age = 0
        self._Age += idade
        return self._Age
    
    @property
    def Endereco(self):
        return self._Andress
    Endereco.setter
    def Endereco(self,endereco):
        self._Andress = endereco
        return self._Andress
    
    @property 
    def Rfriends(self):
        return self._FriendsRelation
    Rfriends.setter
    def Rfriends(self,friends):
        self._FriendsRelation = friends
        return self._FriendsRelation
    
    @property 
    def Score(self):
        return self._Pontos
    Score.setter
    def Score(self,pontos):
        self.Upontos += pontos
        return self.Upontos

    @property
    def Date(self):
        return self._Date
    Date.setter
    def Date(self):
        self._Date == dict()
        return self._Date

#Metodo para inserir dados
    def __Insert_Into(self,nome,idade,endereco,friends,pontos):
        self.Name(nome)
        self.Idade(idade)
        self.Endereco(endereco)
        self.Rfriends(friends)
        self.Score(pontos)

    def Select(self,nome,idade,endereco,friends,pontos):
        self.__Insert_Into(nome,idade,endereco,friends,pontos)
        self._Date['Nome'] = self._Name
        self._Date['Idade'] = self._Age
        self._Date['Endereço'] = self._Andress
        self._Date['Conecção'] = self._FriendsRelation
        self._Date['Score'] = self.Upontos
    
#---------------------------------------
#Registrando Trilhas   
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
    def selectTrilha1(self,nome,conection,idade):
        try: 
            self.grupo1.append(nome)
            self.grupo1.append(conection)
            self.listaAge1.append(idade)
            self.UserTrilhas['Trilha do Sossego'] = self.grupo1
            self.UserTrilhas['Adventurers Age: '] = self.listaAge1
        except:
            print('Verifique seus Dados')
    
    def selectTrilha2(self,nome,conection,idade):
        try: 
            self.grupo2.append(nome)
            self.grupo2.append(conection)
            self.listaAge2.append(idade)
            self.UserTrilhas['Trilha Rampa do Caim'] = self.grupo2
            self.UserTrilhas['Adventurers Age: '] = self.listaAge2
        except:
            print('Verifique seus Dados')    

#----------------------------------------------
#Gameficação

    def Game(self):
        for x in self.grupo1:
            if 'Familia' in x:
                self.Upontos +=20
            elif x == 'Amigo':
                self.Upontos += 15
            elif x == 'Guia':
                self.Upontos -= 5
        else:
            if len(self.grupo1) == 20 or len(self.grupo2) == 20:
                    self.Upontos -= 10
        for y in self.listaAge1:
            if y < 18:
                self.Upontos += 10

    def Game1(self):       
        for y in self.grupo2:
            if 'Familia' in y:
                self.Upontos +=20
            elif y == 'Amigo':
                self.Upontos += 15
            elif y == 'Guia':
                self.Upontos -= 5
        else:
            if len(self.grupo2) == 20:
                self.Upontos -= 10
        for e in self.listaAge2:
            if e < 18:
                self.Upontos += 10



            
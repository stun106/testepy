'''[PT-A02] A NASA (Agência Espacial dos Estados Unidos) mantém um registro de todos os asteroides e suas distâncias relativas à Terra. Você foi convidado para escrever um programa que leia o nome do asteroide e uma lista das suas últimas 5 distâncias da Terra. Armazene os dados em um dicionário, onde a chave é o nome do asteroide. Exiba no final a distância média de todos os asteroides registrados.'''
        

class Asteroides: 
    
    def __init__(self):
        self.Registro = ''
        self.distancia = [] 
        self.Media_D = 0
        self.DadosObj = {}
        
    def register(self):
        self.Registro = input('informe o nome de registro do asteroide: ')
        return self.Registro
    
  
    def Add_obj1(self):
        self.distancia.append(Distancia)
        self.DadosObj[self.Registro] = self.distancia
        return self.DadosObj
    
    def SomaparaMedia(self):
        self.Media_D += sum(self.distancia)
        return self.Media_D

    def verificador(self,a,b='y'):
        if a == b:
            return True
        else:
            return False


ProgrammingObj = Asteroides()

Question = 'y'
print('\033[1;42m A NASA (Agência Espacial dos Estados Unidos) \033[0;0m \n')
while True:
    ProgrammingObj.register()
    for Distancia in range(1,5+1):
        Distancia = float(input('Informe suas 5 distancias relativa individualmente sob a terra: '))
        ProgrammingObj.Add_obj1()
    Question = input('Deseja continuar registrando? [Y/N]: ')
    if ProgrammingObj.verificador(Question) == True:
       pass
    else:  
        ProgrammingObj.SomaparaMedia()
        print(f'{ProgrammingObj.DadosObj.keys()},{ProgrammingObj.distancia}, distância média de todos os asteroides registrados {ProgrammingObj.Media_D/len(ProgrammingObj.distancia)}')

        
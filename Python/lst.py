'''[PT-A02] A NASA (Agência Espacial dos Estados Unidos) mantém um registro de todos os asteroides e suas distâncias relativas à Terra. Você foi convidado para escrever um programa que leia o nome do asteroide e uma lista das suas últimas 5 distâncias da Terra. Armazene os dados em um dicionário, onde a chave é o nome do asteroide. Exiba no final a distância média de todos os asteroides registrados.'''
        

from tkinter import Y


class Asteroides: 
    
    def __init__(self):
        self.distancia1 = [] 
        self.distancia2 = []
        self.distancia3 = []
        self.distancia4 = []
        self.distancia5 = []
        self.DadosObj = {}
        self.Media_D = 0
        
    def Register(self,registro):
        return registro
        
  
    def Add_obj1(self):
        self.distancia1.append(Distancia1)
        self.DadosObj[Registro] = self.distancia1
        return self.DadosObj
    def Add_obj2(self):
        self.distancia2.append(Distancia2)
        self.DadosObj[Registro] = self.distancia2
        return self.DadosObj
    # def Add_obj3(self):
    #     self.distancia3.append(Distancia3)
    #     self.DadosObj[Registro] = self.distancia3       #<-- cada key com valores diferentes
    #     return self.DadosObj
    # def Add_obj4(self):
    #     self.distancia4.append(Distancia4)
    #     self.DadosObj[Registro] = self.distancia4
    #     return self.DadosObj
    # def Add_obj5(self):
    #     self.distancia5.append(Distancia5)
    #     self.DadosObj[Registro] = self.distancia5
    #     return self.DadosObj

    def MediaPart1(self):
        for x in self.distancias:
            self.Media_D += x
        return self.Media_D
    def MediaPart2(self):
            self.Media_D /= 2
            return self.Media_D


    def verificador(self,a,b='y'):
        if a == b:
            return True
        else:
            return False


ProgrammingObj = Asteroides()

Question = 'y'

while True:
    print('\033[1;42m A NASA (Agência Espacial dos Estados Unidos) \033[0;0m \n')

    Registro = input('informe o nome de registro do asteroide: ')
    for Distancia1 in range(1,2+1):
        Distancia1 = float(input('Informe informe suas distancias em ordem crescente e individual: '))
        ProgrammingObj.Add_obj1()
    Question = input('Deseja continuar registrando? [Y/N]: "')
    if ProgrammingObj.verificador(Question) == True:
        pass
    else:  
        print(ProgrammingObj.DadosObj)
        
    Registro = input('informe o nome de registro do asteroide: ')   
    for Distancia2 in range(1,2+1):
        Distancia2 = float(input('Informe informe suas distancias em ordem crescente e individual: '))
        ProgrammingObj.Add_obj2()
    Question = input('Deseja continuar registrando? [Y/N]: "')
    if ProgrammingObj.verificador(Question) == True:
        pass
    else:  
        print(f'{ProgrammingObj.DadosObj}, media: {ProgrammingObj.Media_D}')
    

    # Question = input('Deseja continuar registrando? [Y/N]: "')                       #<-- cada loop atribui valores as keys diferentes
    # if ProgrammingObj.verificador(Question) == True:
    #     print(f'{ProgrammingObj.DadosOb},media: {ProgrammingObj.Media_D}')
    #     pass

                                                       
    # for Distancia3 in range(1,2+1):
    #     Distancia3 = float(input('Informe informe suas distancias em ordem crescente e individual: '))
    #     ProgrammingObj.Add_obj3()
    # Question = input('Deseja continuar registrando? [Y/N]: "')

    
    # for Distancia4 in range(1,2+1):
    #     Distancia4 = float(input('Informe informe suas distancias em ordem crescente e individual: '))
    #     ProgrammingObj.Add_obj4()
    # Question = input('Deseja continuar registrando? [Y/N]: "')

    # for Distancia5 in range(1,2+1):
    #     Distancia5 = float(input('Informe informe suas distancias em ordem crescente e individual: '))
    #     ProgrammingObj.Add_obj5()
    # Question = input('Deseja continuar registrando? [Y/N]: "')

            

        

# if ProgrammingObj.verificador(Question1) == True:
#     ProgrammingObj.MediaPart1()
#     ProgrammingObj.MediaPart2()
#     print(f'{ProgrammingObj.DadosObj} segundo os dados a distância média de todos os asteroides registrados  é:\n \033[1;32m {ProgrammingObj.Media_D} \033[0;0m .')
# elif ProgrammingObj.verificador(Question) == False:
#     print('Siga as intruções a cima')

    


        



 
        
        
        


    
 
 





                
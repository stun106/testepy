'''[PT-A02] A NASA (Agência Espacial dos Estados Unidos) mantém um registro de todos os asteroides e suas distâncias relativas à Terra. Você foi convidado para escrever um programa que leia o nome do asteroide e uma lista das suas últimas 5 distâncias da Terra. Armazene os dados em um dicionário, onde a chave é o nome do asteroide. Exiba no final a distância média de todos os asteroides registrados.'''
        



class Asteroides: 
    
    def __init__(self):
        self.distancia1 = [] 
        self.distancia2 = []
        self.distancia3 = []
        self.distancia4 = []
        self.distancia5 = []
        self.contador_M = 0
        self.Media_D = 0
        self.DadosObj = {}
        

  
    def Add_obj1(self):
        self.distancia1.append(Distancia1)
        self.DadosObj[Registro] = self.distancia1
        return self.DadosObj
    def Add_obj2(self):
        self.distancia2.append(Distancia2)
        self.DadosObj[Registro] = self.distancia2
        return self.DadosObj
    def Add_obj3(self):
        self.distancia3.append(Distancia3)
        self.DadosObj[Registro] = self.distancia3       #<-- cada key com valores diferentes
        return self.DadosObj
    def Add_obj4(self):
        self.distancia4.append(Distancia4)
        self.DadosObj[Registro] = self.distancia4
        return self.DadosObj
    def Add_obj5(self):
        self.distancia5.append(Distancia5)
        self.DadosObj[Registro] = self.distancia5
        return self.DadosObj



    def MediaPart1(self)->float:
        self.Media_D += sum(self.distancia1)
        self.Media_D += sum(self.distancia2)
        self.Media_D += sum(self.distancia3)
        self.Media_D += sum(self.distancia4)
        self.Media_D += sum(self.distancia5)
        return self.Media_D

    def MediaPart2(self):
        self.Media_D /= len(self.DadosObj.values())
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
        Distancia1 = float(input('Informe suas 5 distancias relativa individualmente  sob a terra: '))
        ProgrammingObj.Add_obj1()
    Question = input('Deseja continuar registrando? [Y/N]: ')
    if ProgrammingObj.verificador(Question) == True:
       pass
    else:  
        print(ProgrammingObj.DadosObj)
        
        
    Registro = input('informe o nome de registro do asteroide: ') 
    for Distancia2 in range(1,2+1):
        Distancia2 = float(input('Informe suas 5 distancias relativa individualmente  sob a terra: '))
        ProgrammingObj.Add_obj2()
    Question = input('Deseja continuar registrando? [Y/N]: ')
    if ProgrammingObj.verificador(Question) == True:
        pass
    else:  
        ProgrammingObj.MediaPart1()
        ProgrammingObj.MediaPart2()
        print(f'{ProgrammingObj.DadosObj}\nA distância média de todos os asteroides registrados: {ProgrammingObj.Media_D}')
    
    Registro = input('informe o nome de registro do asteroide: ')                                                   
    for Distancia3 in range(1,5+1):
        Distancia3 = float(input('Informe suas 5 distancias relativa individualmente  sob a terra: '))
        ProgrammingObj.Add_obj3()
    Question = input('Deseja continuar registrando? [Y/N]: ')
    if ProgrammingObj.verificador(Question) == True:
        pass
    else:  
        ProgrammingObj.MediaPart1()
        ProgrammingObj.MediaPart2()
        print(f'{ProgrammingObj.DadosObj}\nA distância média de todos os asteroides registrados: {ProgrammingObj.Media_D}')
    
    Registro = input('informe o nome de registro do asteroide: ')     
    for Distancia4 in range(1,5+1):
        Distancia4 = float(input('Informe suas 5 distancias relativa individualmente  sob a terra: '))
        ProgrammingObj.Add_obj4()
    Question = input('Deseja continuar registrando? [Y/N]: ')
    if ProgrammingObj.verificador(Question) == True:
        pass
    else:  
        ProgrammingObj.MediaPart1()
        ProgrammingObj.MediaPart2()
        print(f'{ProgrammingObj.DadosObj}\nA distância média de todos os asteroides registrados: {ProgrammingObj.Media_D}')

    Registro = input('informe o nome de registro do asteroide: ')
    for Distancia5 in range(1,5+1):
        Distancia5 = float(input('Informe suas 5 distancias relativa individualmente  sob a terra: '))
        ProgrammingObj.Add_obj5()
    Question = input('Press "Y" para confirmar dados: ')
    if ProgrammingObj.verificador(Question) == True:
        ProgrammingObj.MediaPart1()
        ProgrammingObj.MediaPart2()
        print(f'{ProgrammingObj.DadosObj}\nA distância média de todos os asteroides registrados: {ProgrammingObj.Media_D}')
        break

    


            

        


    


        



 
        
        
        


    
 
 





                
''' [PT-A03] Crie uma classe para armazenar as informações de um computador. O computador deve ter os seguntes atributos:
-Modelo
-Fabricante
-Processador
-Tamanho do HD
Espaço ocupado do HD
Esta ligado?

Sua classe tambem deve ter os seguintes métodos:
-Liga() -> altes o status de esta ligado para true
-Desligar() -> altera o status de esta ligado para false
-LimparHD() -> recebe por paramentro o tamanho do espaço que deseja limpar o hd
-OcuparHD() -> recebe por paramentro o tamanho do espaço que deseja ocupar o hd
 '''


from time import sleep
from sys import exit

class Hardware:      
    Ocuped =[{'windows':5.000}] 
    def __init__(self,Modelo,Fabricante,Processador,diskc):
        self.Modelo = Modelo
        self.Fabricante = Fabricante
        self.Processador = Processador
        self.discorigido = float(diskc)
        self.Disk_user = int(5.000)#GB <--- Padrão de fabrica
        self.Ocuped

    def Ligar (self,a,b = 'y'):    
        if a == b:
            return True
        else:
            return False
    def Verificador (self, x,v = int(1)):
        if x == v:
            return True
        else:
            return False

    def Saudação (self):
        return ('''
            Loanding ...
        Welcome to the Jungle! ''')


    def Instalar (self,nome,tamanho):
        if self.discorigido >= tamanho:
           self.Disk_user += tamanho
           self.Ocuped += [{nome:tamanho}]
           return MyComputer.Disk_user
                          
model = input('Informe o modelo: ')
factory = input('Informe o fabricante ')
processor = input('informe o processador: ')
Disk = input('informorme a capacidade do hd: ')

MyComputer = Hardware(model,factory,processor,Disk)


Power = input('Deseja ligar o computador? [Y/N] Sim ou Nao: ')
if (MyComputer.Ligar(Power) == True): 
    print('='*50,MyComputer.Saudação())
    sleep(0.5)
    print('''      [1]        [2]        [3]
                  INSTALAR   REMOVER     DESLIGAR ''')
    sleep(0.5) 
else:
    print('usuario preferio nao ligar o computador')
    exit()
        
while True:
    question = int(input('informe oque deseja fazer: '))
    if (MyComputer.Verificador(question) == 1): 
        softwares = input('informe o nome do arquivo: ')
        t_Arquivo = float(input('informe o tamanho do arquivo: '))
        MyComputer.Instalar(softwares,t_Arquivo)
        print(f'O Software {softwares} foi instalado com sucesso!\n Disco Rigido > C: {MyComputer.Ocuped}')
 
        
        
        


    
 
 





                
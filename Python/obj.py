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





from multiprocessing.sharedctypes import Value
from time import sleep
from sys import exit

class Hardware:      
    Ocuped = {'windows': 5.0}
    def __init__(self,Modelo,Fabricante,Processador,diskc):
        self.Modelo = Modelo
        self.Fabricante = Fabricante
        self.Processador = Processador
        self.discorigido = diskc
        self._Disk_user =  5.0          #GB <--- Padrão de fabrica
        self.Ocuped

                # objetos e classes
#-----------------------------------------------------------------
    @property
    def Disk_user(self):
        return self._Disk_user
    #metodo para Instalar
    @Disk_user.setter
    def Disk_user (self,tamanho):
        if  self.discorigido >= tamanho:
            self._Disk_user += self.discorigido
            self._Disk_user -= tamanho
            return MyComputer._Disk_user
        else:
            return('verifique seus dados')

    #metodo para desistalar
    def Uninstaler(self,x):
        if x == softwares :
            del self.Ocuped[softwares]
            return self.Ocuped
        else: 
            return('Verifique seus Dados.')

    #metodo para verificar o disco rigido
    def Disk_Rigid (self,software,t_Arquivo):
            self.Ocuped[software] = t_Arquivo
            return self.Ocuped

    # metodos p/ verificar condições
    def Ligar (self,a,b = 'y'):    
        if a == b:
            return True
        else:
            return False
    def Verificador (self, a,b = int(1)):
        if a == b:
            return True
        else:
            return False
            # metodos
#-------------------------------------------------------------- 
                    
model = input('Informe o modelo: ')
factory = input('Informe o fabricante ')
processor = input('informe o processador: ')
Disk = float(input('informorme a capacidade do hd: '))

MyComputer = Hardware(model,factory,processor,Disk)


Power = input('Deseja ligar o computador? [Y/N] Sim ou Nao: ')

if (MyComputer.Ligar(Power) == True): 

    print('Loading...')
    sleep(0.5)
    print('Welcome to the Jungle!!!')
    sleep(0.5)
    print('    [1]INSTALAR\n\n    [2]DESISTALAR\n\n    [3]DESLIGAR')      
                    
     
else:
    print('usuario preferio nao ligar o computador')
    exit()
        
while True:

    question = int(input('informe oque deseja fazer: '))

    if (MyComputer.Verificador(question) == 1): 

        softwares = input('informe o nome do arquivo: ')
        t_Arquivo = float(input('informe o tamanho do arquivo: ')) 
        MyComputer.Disk_user += t_Arquivo
        MyComputer.Disk_Rigid(softwares,t_Arquivo)
        print(f'\033[1;32m{softwares}\033[0;0m foi instalado com sucesso!\nEspaço atual:\033[1;31m  {MyComputer.Disk_user} \033[0;0m GB')

    else:
        print(MyComputer.Ocuped)
        sleep(1.0)
        unis_arqv = input('Informe o item a ser Desistalado: ')
        MyComputer.Uninstaler(unis_arqv)
        print(f'\033[1;31m {unis_arqv} \033[0;0m Desinstalado com sucesso!\nDisco Local > C: {MyComputer.Ocuped}')
        
    




 
        
        
        


    
 
 





                
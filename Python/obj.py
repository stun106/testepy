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
    Ocuped = {}
    def __init__(self,Modelo,Fabricante,Processador,diskc):
        self.Modelo = Modelo
        self.Fabricante = Fabricante
        self.Processador = Processador
        self.discorigido = diskc
        self._Disk_user = 0        
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
            self._Disk_user += tamanho
            
            return self._Disk_user
            
    #metodo para desistalar
    def Uninstaler(self,unis_arqv):
            del self.Ocuped[unis_arqv]
            return self.Ocuped
            
    #metodo para verificar o disco rigido
    def Disk_Rigid (self,software,t_Arquivo):
            self.Ocuped[software] = t_Arquivo
            return self.Ocuped

    def hdvalue (self,):
        if self._Disk_user == 0:
            return self.discorigido
        else:
            
           self.discorigido -= sum(self.Ocuped.values())
        return self.discorigido

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
    print('Welcome to the Jungle!!!\n')
    print(f'{MyComputer.Modelo} fabricante {MyComputer.Fabricante}\nsiga as instruções iniciais a seguir!')              
else:
    print('usuario preferio nao ligar o computador')
    exit()
        
while True:
    print('-'*50)
    print('\033[1;32m INSTRUÇÕES >\033[0;0m Com o comando "windows" ou "linox" instale o sistema operacional\nNão esqueça os "drivers" nem o "vscode" e comece estudar!.\n')
    print('    [1]INSTALAR\n\n    [2]DESISTALAR\n\n    [3]DESLIGAR')
    print('-'*50)   
    question = int(input('Utilize os numeros para seguir as instruções:'))
    if (MyComputer.Verificador(question) == 1): 
        print('\n')
        softwares = input('informe o nome do arquivo: ')
        sleep(0.3)
        t_Arquivo = float(input('informe o tamanho do arquivo: '))
        MyComputer.Disk_user = t_Arquivo
        MyComputer.Disk_Rigid(softwares,t_Arquivo)
        print(f'\033[1;32m{softwares}\033[0;0m foi instalado com sucesso!\n espaço usado:\033[1;31m  {MyComputer.Disk_user} \033[0;0m GB')
        print('-'*50) 
    elif (question == 3):
        print('desligando...!')
        exit()
    else:
        print(f'Disco local > C: {MyComputer.Ocuped}')
        sleep(1.0)
        unis_arqv = input('Informe o item a ser Desistalado: ')
        MyComputer.Uninstaler(unis_arqv)
        print(f'\033[1;31m {unis_arqv} \033[0;0m Desinstalado com sucesso!\nDisco Local > C: {MyComputer.Ocuped}')
        print(f'Espaço Livre:\033[1;32m {MyComputer.hdvalue()} \033[0;0m')
        print('-'*50) 
        


 
        
        
        


    
 
 





                
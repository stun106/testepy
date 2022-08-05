
from time import sleep


class Car:
    def __init__(self,marca,modelo,ano,cambio):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.Kmh = 0
        self.cambio = cambio

   

    def Ligar (self,a,b = 'y'):
        if a == b:

            return True
            
        else:
            return False

    def Aceleração(self):
        self.Kmh = 0
        while self.Kmh < 120:
            self.Kmh+=1
            print (self.Kmh,' Km/h')
            sleep(0.1)



CarMarca = input('informe a marca do carro: ')
Model = input('informe o modelo: ')
Year = input('informe o ano do carro: ')
Cambio = input('informe o cambio: ')

MyCar = Car(CarMarca,Model,Year,Cambio)
print('-'*50)
sleep(1.0)
Power_On = input('deseja Ligar seu possante? digite [Y/N]: ').lower()
if (MyCar.Ligar(Power_On) == True):
    print('Vruuum,Seu carro tem a performace de 0 kmh a 120 kmh,coloque o cinto!'  )
    sleep(3.0)
    MyCar.Aceleração()
    
else:
    print('algo deu errado')
    
    


          



    


    
    
            
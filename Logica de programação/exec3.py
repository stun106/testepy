# exercicio da postila, calculando IMC
     #(obs: perguntar o professor sobre os operadores logicos dessa função.)

peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
import math
imc = math.ceil(peso/altura**2)
if imc == 27 or imc <= 29 :
   print('Seu IMC é ', imc,'Sobrepeso Atenção! Alguns quilos a mais já são suficientes para que algumas pessoas desenvolvam doenças associadas, como diabetes e hipertensão. É importante rever seus hábitos. Procure um médico.5')
else:
   print('Seu IMC é', imc, 'Você esta obeso, va praticar um esporte!')

             #atividade numero 3 da lista de exercicio !

#func = input('digite o nome do funcionario: ')
#salaraio = input('digite salario: ')
#print("O funcionario " +func+ " tem um salario de " +salaraio+" em junho!")

#atividade numero 4 da lista de exercicios ! 

#num = float(input('digite um numero: '))
#num2 = float(input('digite outro numero: '))
#res = (num+num2)
#print("a soma entre " +str(num)+  " e ", num2 , " é igual a: " , res)

#-----------------------------------------------------------------------------

                #EXERCICIOS DA APOSTILA DA INFINITY SCHOOL

#Ex-07

#num = int(9)
#num2 = int(8)
#num3 = int(7)
#dividendo = int(3)
#soma = int(num+num2+num3)
#media = (soma/dividendo)
#print('A media dos numeros é ',str(media))

#Ex-08

#aluno1 = input('digite o nome do aluno: ')
#nota1 = float(7.5)
#nota2 = float(7.8)
#nota3 = float(3.1)
#nota4 = float(5.5)
#print('Aluno: ',aluno1)
#print('Notas : ')
#print(nota1,nota2,nota3,nota4)
#notas = (nota1+nota2+nota3+nota4)
#import math
#media1= math.ceil(notas/4)
#print('Média: ')
#print(media1)

#ex do dia ! 

#a = int(10)
#b = int(50)
#a,b = b,a
#print('a= ',a, ' b= ', b)

# exercicio da postila, calculando IMC




peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))
import math
imc = math.ceil(peso/altura**2)
if imc == 27 or imc <= 29 :
    print('Seu IMC é ', imc,'Sobrepeso Atenção! Alguns quilos a mais já são suficientes para que algumas pessoas desenvolvam doenças associadas, como diabetes e hipertensão. É importante rever seus hábitos. Procure um médico.5')
else:
    print('Seu IMC é', imc, 'Você esta obeso, va jogar basquete!')



#Prova Estrutura de Repetição (em Python) 

"""Questão 1 
[LP-A04] Faça um programa que receba 2 (Dois) números inteiros e positivos e imprima na tela todos os números primos que existem entre eles.

Exemplo:

Entrada
1 10

Saída

2 3 5 7"""


primos=[]
number1 = int(input('digite um numero: '))
number2 = int(input('digite outro numero: '))
if number1<number2:
    for x in range(number1,number2+1):
        if x > 1:
            for i in range(2,x):
                if x % i==0:
                    break 
            else: 
                primos.append(x)
    print(primos)
else:
    for i in range(number2, number1+1):
        if i > 1:
            for i in range(2,i):
                if i % i==0:
                    break 
        else: 
            primos.append(i)
    print(primos)




'''questão 2'''


litros = []
somaL = 0
Quant_V = int(input('Informe quantos vazamentos notificados: '))
for L in range(1,Quant_V+1):
    Quant_H2o = int(input('Informe a quantidade de agua perdida por hora: '))
    Quant__hrl = int(input('Informe a quantidade de horas que o vazamento ficou aberto: '))         
    res = Quant_H2o*Quant__hrl
    litros.append(res)


for s in litros: 
    somaL += s 
print(f'quantidade de água desperdiçada em vazamentos de água por toda a cidade é {somaL} litros.')


'''questao 3'''

direção = 0
while True:
    direction = input('Digite a direção que o carro irá percorrer: ')
    if direction == 'direita':
        direção+=1
    elif direction == 'esquerda':
        direção+=1
    elif direction == 'frente':
        direção+=1
    elif direction == 'parar':
        break
    else:
        print('verifique seus dados')

print(f'{direção/100} KM')



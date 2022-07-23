#Atividade 4

'''Faça uma função que receba um valor inteiro e positivo e calcula o seu fatorial.'''




def Factorial(a,b,):
    a = 1
    for x in range(b,1,-1):
        a*=x
        print(a)

valor = 1
number = int(input('digite um numero: '))
Factorial(valor,number)

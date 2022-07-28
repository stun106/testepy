#Atividade 5
'''Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.'''

def Comparação(a,b):

    if a > b: 
        return a
    elif a < b:
        return b 
    else:
        return('numeros iguais!')


number1 = int(input('digite um numero: '))
number2 = int(input('digite outro numero: '))

print(Comparação(number1,number2))
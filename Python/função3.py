#Atividade 3
"""Faça um procedimento que recebe 3 valores inteiros por parâmetro e retorna-os
ordenados em ordem crescente.
"""
def Crescente(a,b,c):
    a = 0
    while a < b: 
        a+=c
        print(a)


number1 = int(input('digite um numero inicializador: '))
number2 = int(input('digite um numero que irá finalizar: '))
passo = int(input('de quanto em quanto o numero crescerá? '))

Crescente(number1,number2,passo)

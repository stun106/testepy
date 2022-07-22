#Atividade 1

"""Crie um algoritmo em Python, que dado dois números informados pelo usuário e
sua operação (das 4 operações básicas da matemática), realize os cálculos
adequados dentro de funções."""

def Calculadora(a,b,c=None):
    if c != None and c == '/':
        return (a/b)
    elif c != None and c =='*':
        return (a*b)
    elif c != None and c == '-':
        return(a-b)
    else:
        return(a+b)

while True:
    n =int(input('digite um numero: '))
    o = input('digite a operação, Ex: "+": ')
    n2 = int(input('digite outro numero: '))
    stop = input('aperte "Y" para confirmar: ').lower()
    if stop != 'y':
        continue
    print(Calculadora(n,n2,o))




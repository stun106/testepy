'''[PT-A05] sobre funções chegou a hora de você criar um código com a seguintes características: Para um número qualquer(n) informado pelo usuário, use a função que possibilite receber um valor inteiro(n) e imprima até (n) linhas.

Exemplo abaixo:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n '''

def SeqPiramid(n):
    for x in range(1,n+1):
        pass 
        for i in range(1,x+1):
            print(i,end='')
        print('\r')

entry = int(input('Digite um numero: '))
SeqPiramid(entry)
  
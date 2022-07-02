#ESTRUTURA CONDICIONAL

#Ex1 manipulando variavel boleana com condiçoes

numero = int(input("digite um numero: "))
numero_bol = True
if numero % 2:
    numero_bol = False
    print("falso")
else:
    numero_bol= True
    print("verdadeiro")
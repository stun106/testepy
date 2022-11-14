'''[PT-A01] Utilizando seus conhecimentos de condicional e estrutura lógica escreva uma código que faz uma análise de um número digitado qualquer (input) e o classifique como o número impar ou par

Exemplo:
Entrada ->2022
Saída   -> par'''


while True:
    try:
        Entry = int(input('digite um numero: '))
        if Entry % 2 == 0:
            print('é par\n')
        else: 
            print('impar\n')
    except:
        print('Algo deu errado, verifique seus dados!\n')

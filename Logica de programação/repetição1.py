#APOSTILHA 3 - ESTRUTURA DE REPETIÇÃO

"""EXERCICIO 1 - SORTEANDO UM NUMERO"""


import random
sorteado =random.randrange(1,10)
for n in range(1,10+1):  
    escolha = int(input('escolha um numero: ')) 
    if escolha == sorteado: 
        print(f'o numero sorteado foi {sorteado}, parabens voce ganhou!')
        break

    elif sorteado > escolha:
        print(f'voce escolheu {escolha}, o numero que você escolheu é maior que o sorteado')
    else: 
        print(f'voce escolheu {escolha}, o numero que você escolheu é menor que o sorteado')
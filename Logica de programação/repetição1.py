#APOSTILHA 3 - ESTRUTURA DE REPETIÇÃO

"""EXERCICIO 1 - SORTEANDO UM NUMERO"""


# import random
# sorteado =random.randrange(1,6+1)
# for n in range(1,10+1):  
#     escolha = int(input('escolha um numero: ')) 
#     if escolha == sorteado: 
#         print(f'o numero sorteado foi {sorteado}, parabens voce ganhou!')
#         break

#     elif sorteado > escolha:
#         print(f'voce escolheu {escolha}, o numero que você escolheu é maior que o sorteado')
#     else: 
#         print(f'voce escolheu {escolha}, o numero que você escolheu é menor que o sorteado')
import random




    


# escolha = input('>')      
# if escolha == 'salvar a pessoa':
#     dado =random.randrange(1,6)
#     print('jogando dado...')
#     print(dado)
    
# if dado > 1:
#     print('Você incrivelmente mata o troll e salva a pessoa')
# else: 
#     print('você falha, e morre')


        # escolha = input('escolha as alternativas> ')      
        # if escolha == '1':
        #    dado =random.randrange(1,6+1)
        # elif dado == 1:
        #     print(f'{dado} acerto critico! voce pode escolher oque fazer com o Trol')
        #     print('Incrivel, Você matou o Trol')
        # else: 
        #     dead('O trol inteceptou usa ação e o esmagou!')

       
    

escolha = input(' escolha e digite uma opção> ')
if escolha == 'provocar o trol':
    print('jogue o dado! de 1 a 4 a ação será executa, Boa Sorte!')
    dado =random.randrange(1,7)
    print('jogando o dado...')
    print(dado)
if dado < '4':
    print('O Trol esta se movendo da porta...')
    print('Você pode passar agora!')       
else:
    print('Eu não faço ideia do que isso significa.')
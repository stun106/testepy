# Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você é um "natural" e venceu o jogo. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.

#-----------------------------------------------

from random import randrange
from time import sleep

def Start():
    n = input('Digite o nome do jogador: ')
    p = input('press "Y" para Iniciar: ')
    return (n,p)
    
     
Start()

def ParDeDado():
    a=randrange(2,12)
    return a

while True:
    print('-'*30)
    sleep(0.5)
    print('preparando pra jogar!')
    sleep(1.0)
    PardeDado = ParDeDado()
    if PardeDado == 7 or PardeDado == 11:
        print(f'Plick, Plick... Você tirou {PardeDado}')
        sleep(1.0)
        print('você é um "natural" e venceu o jogo')
        print('-'*30)
        Start()
    elif PardeDado >= 4 and PardeDado <= 7 or PardeDado >= 8 and PardeDado <=10:
        print('que sorte, vc não perdeu mas pode jogar mais uma vez!')
        sleep(0.5)
        print(f'Plick, Plick... Você tirou {PardeDado}')
    else:
        print(f'Plick, Plick... Você tirou {PardeDado}')
        sleep(1.0)
        print('You Loose, Sir.Craps!')
        print('-'*30)
        Start()

        






   
    









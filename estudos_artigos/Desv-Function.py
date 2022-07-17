"""Desvio de Funções"""

from sys import exit

def Gold_room():
    print('essa sala é cheia de ouro. quanto você pode pegar?')         

    escolha = input('>')
    if '0' in escolha or '1' in escolha:                           #<- condição que aplica valor a um input.
        quanto_pega = int(escolha)
    else:
        dead('man, aprenda oque é numero')  
    
    if quanto_pega < 50:
        print('Otimo, você não é ganacioso, you win!')              #ultima sala, fim do jogo!
        exit(0)
    else:
        dead('você é um bastardo ganancioso![R.I.P]')

def Trol_room():
    print('Tem um Trol aqui!!!')
    print('o Trol esta comendo uma pessoa...')
    print('o Trol esta de frente a outra porta...')
    print('como você vai mover o trol?')
    trol_movido = False

    while True:
        escolha = input('>')
        if escolha == 'salva a pessoa':
            dead('O Trol ver você e então da um tapa em sua cara...[R.I.P]')
        elif escolha == 'provoca o trol'and not trol_movido:
            print('O Trol esta se movendo da porta...')
            print('Você pode passar agora!')
            trol_movido = True
        elif escolha == 'provocar trol' and trol_movido:
            dead('O Trol fica chateado e mastiga sua perna...[R.I.P]')
        

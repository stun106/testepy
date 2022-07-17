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
        dead('você é um bastardo ganancioso!')

def Trol_room():
    print('Tem um Trol aqui!!!')
    print('o Trol esta comendo uma pessoa...')
    print('o Trol esta de frente a outra porta...')
    print('como você vai mover o trol?')
    trol_movido = False

    while True:                                                                             # <---- whiletrue para o usuario escolher a condição certa ate acertar
        escolha = input('>')
        if escolha == 'salva a pessoa':
            dead('O Trol ver você e então da um tapa em sua cara...')
        elif escolha == 'provoca o trol'and not trol_movido:
            print('O Trol esta se movendo da porta...')
            print('Você pode passar agora!')
            trol_movido = True
        elif escolha == 'provocar trol' and trol_movido:
            dead('O Trol fica chateado e mastiga sua perna...')
        elif escolha == 'abrir a porta' and trol_movido:
            Gold_room()
        else:
            print('Eu não faço ideia do que isso significa.')

def Baium_room():
    print('Aqui você ver o grande Baium')
    print('Emitindo uma pressão espiritual do mal, você se sente paralizado, então o grande Baium percebe sua presensa e você enlouquece...')
    print('Você foge pela sua vida ou fica para lutar?')

    escolha = input('>')
    if 'fugir' in escolha:
        start()
    elif 'lutar' in escolha:
        dead('Nem sempre o bem vence o mal!')
    else:
        Baium_room()

def dead(Descanse):
    print(Descanse,'[R.I.P]')
    print('Deseja tentar outra vez?')
    escolha = input('>')
    if escolha == 'sim':
        start()
    else:
        print('Você é um maldito bastardo!')
        exit(0)

def start():
    print('Então você caiu no sono...')
    print('Você esta num lugar sombrio, há uma porta para sua direita e esquerda...')
    print('qual porta escolher?')

    escolha = input('>')
    if escolha == 'esquerda':
        Trol_room()
    elif escolha == 'direita':
        Baium_room()
    else:
        dead('O medo te paraliza ?')


start()

        
        

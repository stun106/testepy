"""Desvio de Funções"""

from sys import exit
from time import sleep
import random



def Gold_room():
    print('uffa!')
    sleep(1.0)
    print('essa sala é cheia de ouro. quanto você pode pegar?')         
    escolha = int(input('> quilates: '))
    if  escolha < 10000:                    #<- condição que aplica valor a um input.    
        print('Você não é medroso e nem Ganancioso!')
        sleep(1.0)
        print('O medo pode te afetar, mas sempre siga em frente, a Ganancia pode te apodrecer aos poucos mas a Humildade lhe enriquece.') #ultima sala, fim do jogo!
        sleep(1.0)
        print('Bom trabalho, você venceu!')
        exit(0)
    elif escolha == str:
        dead('man, aprenda oque é numero')  
    else:
        dead('você é um bastardo ganancioso!')

def Trol_room():
    print('Tem um Trol aqui!')
    sleep(1.0)
    print('Logo você percebe que o trol esta comendo algo')
    sleep(1.0)
    print('é alguem, alguma pessoa..')
    sleep(1.0)
    print('o Trol esta de frente a outra porta...')
    sleep(1.0)
    print('você tem 3 opções:\n 1-Provocar o trol; \n 2-Não fazer nada; \n 3-Salvar a pessoa')

    escolha = input(' escolha e digite uma opção: ')
    bear_move = False
    dado =random.randrange(1,7)
    while True: 
        print('jogue o dado! de 1 a 4 a ação será executa, Boa Sorte!')
        confirmador = str(input('digite "Y" para jogar o dado: '))
        sleep(1.0)
        print('jogando o dado...')
        print('resultado: ',dado)
        if confirmador != 'y':
            print('man, você é um bastardo que não sabe ler?')
        elif escolha == 'provocar trol' or dado <=4 and not bear_move:
            print('O Trol esta se movendo ate você ...')
            sleep(1.0)
            regressiva()
            print('rapido digite "abrir porta"!')
            bear_move = True
        else: 
            dead('você falhou!, o Trol te esmagou!')
        escolha = input('> ')
        if escolha in 'abrir a porta':
            Gold_room()
        else:
            sleep(1.0)
        dead('O trol te esmagou! o medo lhe paralizou?') 

def Baium_room():
    print('Aqui você ver o grande Baium')
    sleep(1.0)
    print('Emitindo uma pressão espiritual do mal, você se sente paralizado, então o grande Baium percebe sua presensa e você enlouquece...')
    sleep(1.0)
    print('Você foge pela sua vida ou fica para lutar?')

    escolha = input('> ')
    if 'fugir' in escolha:
        Trol_room()
    elif 'ficar' in escolha:
        print('...')
        dead('Nem sempre o bem vence o mal!')
    else:
        Baium_room()

def dead(Descanse):
    print(Descanse,'[R.I.P]')
    sleep(1.0)
    print('Deseja tentar outra vez?')
    escolha = input('> ')
    if escolha == 'sim':
        start()
    else:
        print('Você é um maldito bastardo!')
        exit(0)

def regressiva():
    for x in range(5,-1,-1):
        print(x,'corra!')
        sleep(0.5)

def start():
    print('-'*50)
    print('Então você caiu no sono...')
    sleep(1.0)
    print('Você esta num lugar sombrio, há uma porta para sua direita e esquerda...')
    sleep(1.0)
    print('qual porta escolher?')
       
    escolha = input('> ')
    if escolha == 'esquerda':
        Trol_room()
    elif escolha == 'direita':
        Baium_room()
    else:
        dead('O medo te paraliza ?')


start()

        
        

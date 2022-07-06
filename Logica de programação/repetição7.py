"""Faça uma calculadora"""
#incremento,Listas

number = 0
number_two = 0
press_off = 'p'
while number != 'p':
    number = float(input('digite um numero: '))
    operador  = str(input('digite "SOMA" para adição, "SUB" subtração, "MULT" para multiplicação, "DIV" para divisão:  ')).lower()
    number_two = float(input('digite outro numero: '))
    operações = [number + number_two, number - number_two, number*number_two, number/number_two]
    if operador != 'soma' and operador != 'sub' and operador != 'mult' and operador != 'div':
        print('Verifique seus dados, Ultilize apenas os dados informados a cima!')
        continue
    elif operador == 'soma':
      print(f'o resultado é: {operações[0]}')
    elif operador == 'sub':
        print(f'o resultado é: {operações[1]}')
    elif operador == 'mult':
        print(f'o resultado é: {operações[2]}')
    else:
        print(f'o resultado é: {operações[3]:.1f}')
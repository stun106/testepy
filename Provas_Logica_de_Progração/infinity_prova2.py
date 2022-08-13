#Apostila 3 prova 3

number = 0
number2 = 0
while number != 10:
    number = int(input('digite um numero: '))
    number2 = int(input('digite outro numero: '))
    confirmador = str(input('Aperte "Y" para prosseguir: ')).upper()
    operações = [number + number2, number * number2, (number+number2)/2, number**2, number2**3]
    if confirmador != 'Y':
        print('Verifique seus dados, Ultilize as instruções a cima!')
        continue
    else:
        print(f'A soma entre os numeros é {operações[0]}\n A multiplicacão dos dois numeros é {operações[1]}\n A média entre eles {operações[2]}\n O primeiro elevado ao quadrado {operações[3]}\n O segundo elevado ao cubo {operações[4]}' )
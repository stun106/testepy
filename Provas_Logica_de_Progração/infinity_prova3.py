'''Prova Introdução ao Python e Estrutura Condicional'''



'''questão 1'''
while True:
    sIgNoS = ['Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem', 'Libra', 'Escorpião', 'Sagitário', 'Capricórnio', 'Aquário', 'Peixes']
    DaY= int(input('Dia de Nascimento: '))
    moUnTh = str(input('Mês de Nascimento: '))
    confirme = str(input('Digite "Y" para continuar: ')).lower()
    if confirme != 'y':
        print('Siga as instruções a cima!')
    elif DaY >= 21 and moUnTh == 'março' or moUnTh == 'abril' and DaY <= 20:
        print(sIgNoS[0])
    elif DaY >= 21 and moUnTh == 'abril' or moUnTh == 'maio' and DaY <= 20:
        print(sIgNoS[1])
    elif DaY >= 21 and moUnTh == 'maio' or moUnTh == 'junho' and DaY <= 22:
        print(sIgNoS[2])
    elif DaY >= 21 and moUnTh == 'junho' or moUnTh == 'julho' and DaY <= 20:
        print(sIgNoS[3])
    elif DaY <=23 and moUnTh == 'julho' or moUnTh == 'agosto' and DaY <= 22:
        print(sIgNoS[4])
    elif DaY <=23 and moUnTh == 'agosto' or moUnTh == 'setembro' and DaY <= 22:
        print(sIgNoS[5])
    elif DaY <=23 and moUnTh == 'setembro' or moUnTh == 'outubro' and DaY <= 22:
        print(sIgNoS[6])
    elif DaY <=23 and moUnTh == 'outubro' or moUnTh == 'novembro' and DaY <= 21:
        print(sIgNoS[7])
    elif DaY <=22 and moUnTh == 'novembro' or moUnTh == 'dezembro' and DaY <= 21:
        print(sIgNoS[8])
    elif DaY <=22 and moUnTh == 'dezembro' or moUnTh == 'janeiro' and DaY <= 20:
        print(sIgNoS[9])
    elif DaY <=21 and moUnTh == 'janeiro' or moUnTh == 'fevereiro' and DaY <= 18:
        print(sIgNoS[10])
    else:
        print(sIgNoS[11])




'''questão 2'''
year = int(input('digite o ano que nasceu'))
month = int(input('digite o mes que nasceu'))
day = int(input('digite o dia que nasceu'))
age = 2022-year
print(f'{age},{month},{day}')
if month >= 12 and day >=30:
    print('"Verifique seus dados!"')
elif year < 1900:
    print('você é um ser humano?')
else: 
    live = int(age*365)+month*30+day
    
    print(live)
    
base = int(input('digite a base da area do triangulo: '))
altura = int(input('digite a altura do triangulo: '))
print(base*altura)




'''questão 3'''

primos = []
number1 = int(input('digite um numero: '))
number2 = int(input('digite outro numero: '))

for x in range(number1,number2+1):
    cont=0
    for y in range(number1,number2+1):
        if x % y == 0:
            cont+=1
    if cont == 2:
        primos.append(x)

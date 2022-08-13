# Sistema de provas atualizados(novas questões)

"""questão 1"""

question = str(input('Qual seu nome: '))
print(f'Olá {question}, seja bem vindo(a)! ')



"""questão 2"""

number = float(input('Digite um numero: ')) 
double = number*2
part = number/3
print(f'dobro: {double}\nterça parte: {part:.2f} ')



"""questão 3"""

space = int(input('informe o espaço: '))
time = int(input('informe o tempo: '))
velocity = space/time
print(f'velocidade: {velocity}')



"""questão 4"""

value_hour = float(input('digite o valor de sua hora trabalhada: '))
value_mouth = float(input('digite a quantidade de horas trabalhada: '))
S_gross = value_hour*value_mouth #<---- salario bruto
IR = [(S_gross*5)/100, (S_gross*10)/100, (S_gross*20)/100]
INSS = (S_gross*10)/100      # <----- descontos
FGTS = (S_gross*11)/100
if S_gross < 900:
    print(f'Salario Bruto:R$ {S_gross}\n (-)IR:R$ {IR[0]}\n(-)INSS:R$ {INSS}\nFGTS: {FGTS}\nTotal de descontos:R$ INSENTO\nSalario liquido:R$ {S_gross-INSS}')
elif S_gross >= 900 and S_gross < 1500:
    print(f'Salario Bruto:R$ {S_gross}\n(-)IR:R$ {IR[0]}\n(-)INSS: {INSS}\nFGTS:R$ {FGTS}\nTotal de descontos:R$ {IR[0]+INSS}\nSalario liquido:R$ {S_gross-INSS-IR[0]}')
elif S_gross >= 1500 and S_gross < 2500:
    print(f'Salario Bruto:R$ {S_gross}\n(-)IR:R$ {IR[1]}\n(-)INSS:R$ {INSS}\nFGTS:R$ {FGTS}\nTotal de descontos:R$ {IR[1]+INSS}\nSalario liquido:R$ {S_gross-INSS-IR[1]}')
else:
    print(f'Salario Bruto: {S_gross}\n(-)IR:R$ {IR[2]}\n(-)INSS:R$ {INSS}\nFGTS:R$ {FGTS}\nTotal de descontos:R$ {IR[2]+INSS}\nSalario liquido:R$ {S_gross-INSS-IR[2]}')

    

"""questão 5"""

s_worker = float(input('Digite o salario do colaborador: '))
rjst = [(s_worker*20)/100,(s_worker*15)/100,(s_worker*10)/100, (s_worker*5)/100]
if s_worker > 1500:
    print(f'R$ {s_worker+rjst[3]}')
elif s_worker > 700:
    print(f'R$ {s_worker+rjst[2]}')
elif s_worker > 280:
    print(f'R$ {s_worker+rjst[1]}')
else: 
    print(f'R$ {s_worker+rjst[0]}')

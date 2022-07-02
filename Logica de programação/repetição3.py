"""EXERCICIO 3 - PORTATORES DE COVID19"""


pergunta = 'y'
for i in pergunta:
    pl = int(input('digite numero de pacientes com sintomas leves: '))
    pa = int(input('digite numero de pacientes com sintomas assintomaticos: '))
    pg = int(input('digite numero de pacientes com sintomas graves: '))
    pergunta = str(input('aperte "Y" para confirmar: ')).lower()
    calc = round(pl*100/10) 
    calc1 = round(pa*100/10)
    calc2 = (round(pg*100/10))
    if pergunta != 'y':
        print('ultilize apenas "Y" como resposta')
    elif calc > 10*100/10 or calc == calc1 :
        print('erro')
    elif calc1 > 10*100/10 or calc1 == calc2 or calc1 == calc:
        print('erro')
    elif calc2 > 10*100/10 or calc2 == calc1 or calc2 == calc:
        print('erro')
    else:
        
        print(f'sintomas leves = {calc}%')
        print(f'sintomas assintomatico {calc1}%')
        print(f'sintomas graves {calc2}%')
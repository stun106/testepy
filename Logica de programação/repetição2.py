'''EXERCICIO 2 - PROGRAMA PARA MEDIR VALOR DE TONELADAS'''

Value_FIX_TN = float(15.000)
Pergunta = 'S'
TONELADAS = 0
while Pergunta == 'S':
    t = int(input('digite o numero de toneladas transportadas: ')) 
    print(t,'t')
    Pergunta = str(input('deseja continuar calculando ? [{S}/{N}]  ')).upper()
if  Pergunta == 'S':
    TONELADAS += t 
    print(f'valor total de toneladas: {TONELADAS}t')
else:
    res = Value_FIX_TN*t
    print(f'o valor total faturado foi R${res:,.3f}')
#ex3 Programa para validar credito

salario = int(input('digite seu salario: '))
V_parcela = int(input('digite o valor da parcela: '))
parcela_porcento = float(0.30)
parcela_max = salario*parcela_porcento
if V_parcela > parcela_max:
    print(f'o valor da parcela esta MAIOR que 30% do seu salario, seu credito NAO foi aprovado ')
else:
    print(f'o valor da parcela esta MENOR que 30%, OK, credito aprovado!')

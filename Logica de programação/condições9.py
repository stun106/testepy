#MAIS EXERCICIOS DE CONDIÇÕES

#Ex1 Programa para calcular valor de passagem por km 

Passagem_m = float(0.85)
passagem_l = float (0.65)
km_base = int(250)
km = int(input('quantos quilometros pretende viajar?'))
if km > km_base: 
    valor1_ = km*passagem_l
    print(f'Sua passagem sera R${passagem_l} por km que ficara no valor de R${valor1_}')
else:
    valor2_ = km*Passagem_m
    print(f'Sua passagem sera R${Passagem_m} por km que ficara no valor de R${valor2_}')
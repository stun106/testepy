#Ex2 c/ listas

passagem = [0.85,0.65]
km_base = int(250)
km = int(input('quantos quilometros pretende viajar?'))
if km > km_base: 
    valor1_ = km*passagem[0]
    print(f'Sua passagem sera R${passagem[1]} por km que ficara no valor de R${valor1_}')
else:
    valor2_ = km*passagem[1]
    print(f'Sua passagem sera R${passagem[0]} por km que ficara no valor de R${valor2_}')

print('fim')
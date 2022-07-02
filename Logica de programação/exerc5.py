#LP01 -ex04 Programa para calcular votos

eleitores = float(input('Total de eleitores: '))
V_Branco = float(input('Total de votos em branco: '))
V_Nulos = float(input('Total de votos nulos '))
V_Validos = float(input('Total de votos validos '))
validos = (V_Validos / 100) * eleitores / 100
branco = (V_Branco / 100) * eleitores / 100
nulos = (V_Nulos / 100) * eleitores / 100
print(f"Total de votos Validos no municipio : {validos}%"
f" Total de votos Nulos : {nulos}%"
f" total de votos em branco {branco}%")

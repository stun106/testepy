#Ex 3 (hospital e respiradores)

respiradores = int(50)
hosp1 = int(input("digite o numero de ocupação deste hospital: "))
hosp_resp = int(input("digite quantos respitadores o hospital esta utilizando: "))
taxa_ocupaçao = (60 * hosp1) / 100
if hosp1 < hosp_resp:
   print(f'{taxa_ocupaçao}"ERRO!" Dados incoerentes!')
elif taxa_ocupaçao <= 60 and hosp_resp >= respiradores:
   print(f"a taxa de ocupação no hosp1 é {taxa_ocupaçao}% e esta sendo utilizado {hosp_resp}, hospital no padrão")
else:
    print(f"a taxa de ocupação no hosp1 é {taxa_ocupaçao}% e esta sendo utilizado {hosp_resp}, iremos mandar mais 5 respiradores!")
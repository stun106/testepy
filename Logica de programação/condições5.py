#ex2 

Temperatura = int(input("Digite sua temperatura: "))
cancela = False
if Temperatura <= 37 or Temperatura == 37: 
    cancela:True
    print(f"Sua temperatura é {Temperatura}º pode passar!")
else: 
    cancela: False
    print(f"Sua temperatura é {Temperatura}º procure um medico")
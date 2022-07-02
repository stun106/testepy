#LP01-ex02 Calculando Fahrenheit para Celsios

TF = float(input('digite uma temperatura em Fº '))
TF_Resultado = round((TF - 32) / 9)
T_Celsios = 5* TF_Resultado
print(f" Temperatura {TF}º Fahrenheit para {T_Celsios} Celsios" )
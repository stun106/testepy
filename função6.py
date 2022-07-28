def SomaLimite(a,b,l=15):
    
    if a+b > l:
        return a+b
    else:
        return('não foi possivel realizar a soma')

number1 = int(input('digite um numero: '))
number2 = int(input('digite outro numero: '))
print(SomaLimite(number1,number2))
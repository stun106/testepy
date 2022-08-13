'''1. [PT-A01] Escreva uma função que recebe um determinado ano e retorne o século daquele ano.Exemplo:
Entrada -> 1453
Saída   -> XV'''
  
def TransformRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    roman = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    y = 12
      
    while number:
        div = number // num[y]
        number %= num[y]
  
        while div:
            print(roman[y], end = "")
            div -= 1
        y -= 1
  
contador = 0 
sec = 0
anos = int(input('Informe o ano: '))
while contador < anos:
    contador+=100
    if contador / 100:
        sec+=1
print("Seculo", end = " ")
TransformRoman(sec)
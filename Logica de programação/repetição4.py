"""EXEMPLO 4 - VOGAIS DIGITADAS"""

vogal = 0
palavra = str(input('digite qualquer palavra: '))
for vogais in palavra:
    if vogais == 'a' or vogais == 'e' or vogais == 'i' or vogais == 'o'  or vogais == 'u':
        print(vogais)
        vogal+=1
print(vogal, 'vogais')
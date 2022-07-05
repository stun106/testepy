# APOSTILHA 3 - REPETIÇÃO E CICLO

"""Possibilidades com while 'Break' e 'Continue' """

x = 0
number = 0  # <- se não atribuir um valor  a variavel não vai dar certo.
while x < 11:
    if number != 10:
        number = int(input('digite um numero: '))
        print('"Numero Invalido" Tente Novamente!')
        continue # <- o continue não interromperá o loop até que a condição esteja correta.
    else:
        print(x)
        x+=1


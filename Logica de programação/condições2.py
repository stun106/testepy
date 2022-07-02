# ex2 condições - Programa para calcular media usando condições

aluno = input('digite o nome do aluno: ')
nota1 = float(input('digite a nota da avaliação I '))
nota2 = float(input('digite a nota da avaliação II '))
nota3 = float(input('digite a nota da avaliação III '))
media = round((nota1+nota2+nota3) / 3)
if media >= 6:
    print(f"Parabens sua media foi {media}! você passou!!")
else:
    print(f"sua media foi {media}, estude mais da proxima vez!")

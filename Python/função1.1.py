#Atividade 2 

"""Elaborar um algoritmo que calcule a área de triângulos , quantos o usuário quiser calcular
separe a função com o nome “calcula_triangulo”."""

def Calcula_triangulo(b,a):
    return b*a/2


Calcula_triangulo.__doc__
'esta função calcula a area do triangulo'

base = int(input('digite a base da area do triangulo: '))
altura = int(input('digite a altura da area do triangulo : '))

print(Calcula_triangulo(base,altura))


# crie uma lista de 10 a 20 e multiplique os valores pelo dobro.
def Crescente(l,c):
    for x in l:
        c=x*2
        return c  #<--- lembre-se, nunca utilize uma função de entrada ou saida quando estiver criando uma função especifica.
        


CrescList = list(range (10,21))
c = 0
Crescente(CrescList,c)
    
    
from random import randrange


def ParDeDado(b,c):
    a=randrange(b,c)
    return a

def ContadorDePontos(pontos,c,a,b):
    while True:
        if ParDeDado(a,b) > 4 and ParDeDado(a,b) <=5 or ParDeDado(a,b) == 6 or ParDeDado(a,b)== 8 or ParDeDado(a,b) > 9 and ParDeDado(a,b)<=10:
            c=0
            pontos +=c
            return pontos
        else:
            break


cont = 0
valor = 0
ContadorDePontos(valor,cont,1,12)


    

# Dado = ParDeDado(1,12)
# if Dado == 7 or Dado == 11:
#     print(f'Você tirou: {Dado}. Você é um jogador natural !')
# elif Dado > 4 and Dado <=5 or Dado == 6 or Dado == 8 or Dado > 9 and Dado <=10:
  
    
# else: 
#     print(f'Você tirou: {Dado}. Você foi nomeado a Sir.LooserCraps"')




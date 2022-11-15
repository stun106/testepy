'''[PT-A07] Em um campeonato de surf realizado pela WSL foi analisada uma falha na programa de premiação do evento. Faça um código usando seus conhecimentos adquiridos em Python no qual tenha como principal finalidade definir as colocações dos participantes, leve em conta que, é impossível haver empate técnico, a saída do código deverá dizer o nome do participante e sua pontuação adjunto da sua colocação final e por fim defina uma função que consiga abranger todo código e a execute com as pontuações abaixo . 

Lucas - 1454 pontos
Pedro - 1243 pontos
Ricardo - 1452 pontos'''


def insert(l:int,p:int,r:int,L:list) -> list:
    l += 1454
    p += 1243
    r += 1452
    L.append(l)
    L.append(p)
    L.append(r)
    L.sort(reverse=True)
    return L


score = list()
atleta1 = 0
atleta2 = 0
atleta3 = 0
insert(atleta1,atleta2,atleta3,score)
print(f'Atletas: Lucas, Pedro, Ricador - Scores {score}')
print(f'1st - Lucas - {score[0]}\n 2st - Ricardo {score[1]}\n 3st - Pedro {score[2]}')




    






    












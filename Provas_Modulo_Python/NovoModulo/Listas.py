'''[PT-A03] com intuito de organizar o pasto, o fazendeiro que andava estudando a linguagem Python queria fazer um arranjo em sua fazenda  usando o método de listas, sabendo disso ajude o agrônomo a realizar essa mudança. Levando em consideração que no pasto 1 (que também é uma lista)tem  4 listas com um animal diferente em cada(animais da sua escolha)e dentro dessas listas havia 4 cores de animais(cores da sua escolha porém sempre diferentes),faça um código responsável por mudar 3 listas de animais do pasto 1 para o pasto 2 que estava vazio e imprimindo o resultado final dos animais do pasto 2 e os animais do pasto 1 '''

pasto1 = [
        'vacas=',['marrom','branco','cinza','bege'],
        'bezerros=',['lilas','amarelo','vermelho','bege'],
        'cavalos=',['marrom','branco','cinza','bege'],
        'ovelhas=',['marrom claro','cinza escuro','azul','bege']
        ]

pasto2 = []

animal1 = pasto1.pop(0)
corsanimal1 = pasto1.pop(0)
animal2 = pasto1.pop(0)
corsanimal2 = pasto1.pop(0)
animal3 = pasto1.pop(2)
corsanimal3 = pasto1.pop(2)

pasto2.append(animal1)
pasto2.append(corsanimal1)
pasto2.append(animal2)
pasto2.append(corsanimal2)
pasto2.append(animal3)
pasto2.append(corsanimal3)

print('Pasto 1\n',pasto1,'\n')
print('pasto 2\n',pasto2)


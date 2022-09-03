

#-----------------------------------------------------------------------------




#ex5 (times)
#time1 = input('Digite seu time preferido da NBA: ')
#time2 = input('Digite um time que você menos gosta da NBA: ')
#pontos_time1 = int(input('Digite quantos pontos fizeram seu time favorito:')) 
#pontos_time2 = int(input('Digite quantos pontos fizeram o outro time: '))

#if pontos_time1 == pontos_time2:
#    print(f"{time1} {pontos_time1} X {pontos_time2} {time2} EMPATE!" )
#elif pontos_time1 < pontos_time2:
#    print(f"{time1} {pontos_time1} X {pontos_time2} {time2} DERROTA :/!" )
#else:
#    print(f"{time1} {pontos_time1} X {pontos_time2} {time2} VITORIOSO, UMA MAQUINA, UMA BESTA ENJAULADA COM ODIO SEU FILHO DA P*** !" )

#==================================================================================================



#Livro: Aprenda Pynthon3 do jeito certo. 

#LOOPS E LISTAS  

# numero = [1,2,3,4,5]
# frutas = ['maça', 'laranja','uva','limao']
# escolha = [1, 'maça', 2, 'laranja',3,'limao']

# # esse primeiro tipo de loop 'for' percorre uma lista
# for number in numero:
#     print(f'esses são os numeros {number}\n')

# # mesma coisa com o codigo a cima
# for fruits in frutas:
#     print(f'essas são as frutas {fruits}\n')

# for i in escolha:
#     print(f'peguei {i}\n')

# # PRESTE ATENÇÃO NISSO! tambem podemos construir listas, primeiro comece com uma vazia

# elementos = []

# # entao use a função range para fazer a contagem de 0 a 5

# for i in range(0,6):
#    print(f'adicionando {i} para a lista')

# #'append' é uma funçao que as listas entendem
# elementos.append(i)

#  #agora podemos imprimi-las tbm

# for i in elementos:
#    print(f'elementos são {i}')


# LOOPS WHILE

# n = 0
# numeros = [] 
# while n < 6:
#     print(f'o numero {n}')
#     numeros.append(n)
#     n=n+1
#     print(f'da lista{numeros}')
#     print(f'representa na lista como {n}')

# faça um loop que multiplique como uma tabuada

# n = 0
# mult = int(input('digite um multiplicador: '))

# while n < 11:
#     res = mult*n
#     print(f'{mult} x {n} = {res}')
#     n+=1


#===========================================================

# pergunta = 'y'
# for i in pergunta:
#     pl = int(input('digite numero de pacientes com sintomas leves: '))
#     pa = int(input('digite numero de pacientes com sintomas assintomaticos: '))
#     pg = int(input('digite numero de pacientes com sintomas graves: '))
#     pergunta = str(input('aperte "Y" para confirmar: ')).lower()
#     calc = round(pl*100/10) 
#     calc1 = round(pa*100/10)
#     calc2 = (round(pg*100/10))
#     if pergunta != 'y':
#         print('ultilize apenas "Y" como resposta')
#     else:
        
#         print(f'sintomas leves = {calc}%')
#         print(f'sintomas assuntomatico = {calc1}%')
#         print(f'sintomas graves = {calc2}%')



#==========================================
"""Calculo vetorial usando FOR"""


# vetor=1
# number= int(input('Digite um numero: '))
# for vetorial in range(number,1,-1):
#     vetor*=vetorial
#     print(vetor)





'''Numeros primos '''
# cont = 0
# number = int(input('digite um numero: '))
# for primo in range(1,number+1):
#     if number % primo  == 0:
#         cont+=1

# if cont == 2:
#     print(primo,'primo')
# else:
#     print('nao é primo')

#============================================
'''função para contagem regressiva'''

# from time import sleep
# def regressiva():
#     for x in range(0,120+1):
#         print(x)
#         sleep(0.1)

'''função dobrando valores de uma lista'''

# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos+=1



# valores = [6,5,1,8,2]      
# dobra(valores)
# print(valores)

# =======================================


# litros = []
# soma = 0
# Quant_V = int(input('Informe quantos vazamentos notificados: '))
# for L in range(1,Quant_V+1):
#     Quant_H2o = int(input('Informe a quantidade de agua perdida por hora: '))
#     Quant__hrl = int(input('Informe a quantidade de horas que o vazamento ficou aberto: '))
#     res = Quant_H2o*Quant__hrl
#     litros.append(res)
# print(litros)

# for s in litros: 
#     soma += s 
# print(soma)

# while True:
#     sIgNoS = ['Áries', 'Touro', 'Gêmeos', 'Câncer', 'Leão', 'Virgem', 'Libra', 'Escorpião', 'Sagitário', 'Capricórnio', 'Aquário', 'Peixes']    
#     DaY= int(input('Dia de Nascimento: '))    
#     moUnTh = str(input('Mês de Nascimento: '))    
#     confirme = str(input('Digite "Y" para continuar: ')).lower()    
#     if confirme != 'y':       
#         print('Siga as instruções a cima!')    
#     elif DaY >= 21 and moUnTh == 'janeiro' or  moUnTh == 'fevereiro' and DaY <=18:        
#         print(sIgNoS[10])        
#         break    
#     elif DaY >= 19 and moUnTh == 'fevereiro' or moUnTh == 'março' and DaY <= 20:  
#         print(sIgNoS[11])       
#         break   
#     elif DaY >= 21 and moUnTh == 'março' or moUnTh == 'abril' and DaY <= 20:       
#         print(sIgNoS[0])  
#         break    
#     elif DaY >= 21 and moUnTh == 'abril' or moUnTh == 'maio' and DaY <= 20: 
#         print(sIgNoS[1])
#         break 
#     elif DaY >= 21 and moUnTh == 'junho' or moUnTh == 'julho' and DaY <= 22:
#         print(sIgNoS[3])       
#         break    
#     elif DaY >= 23 and moUnTh == 'julho' or moUnTh == 'agosto' and DaY <= 22:
#         print(sIgNoS[4])        
#         break    
#     elif DaY >= 23 and moUnTh == 'agosto' or moUnTh == 'setembro' and DaY <= 22:
#         print(sIgNoS[5])       
#         break    
#     elif DaY >= 23 and moUnTh == 'setembro' or moUnTh == 'outubro' and DaY <= 22:
#         print(sIgNoS[6]) 
#         break    
#     elif DaY >= 23 and moUnTh == 'outubro' or moUnTh == 'novembro' and DaY <= 21:
#         print(sIgNoS[7])       
#         break    
#     elif DaY >= 22 and moUnTh == 'novembro' or moUnTh == 'dezembro' and DaY <= 21:        
#         print(sIgNoS[8])        
#         break    
#     else:         
#         print(sIgNoS[9])        
#         break


# primos = []
# number1 = int(input('digite um numero: '))
# number2 = int(input('digite outro numero: '))

# for x in range(number1,number2+1):
#     cont=0
#     for y in range(number1,number2+1):
#         if x % y == 0:
#             cont+=1
#     if cont == 2:
#         primos.append(x)

# print(primos)

# n1 = 50 

# n2 = 5 

# while n1 != n2: 

#     if n1<n2:

#         n2 = n2 - n1

#     else: 

#         n1 = n1- n2 

# print(n1)

# def TransformRoman(number):
#     num = [1, 4, 5, 9, 10, 40, 50, 90,
#         100, 400, 500, 900, 1000]
#     roman = ["I", "IV", "V", "IX", "X", "XL",
#         "L", "XC", "C", "CD", "D", "CM", "M"]
#     y = 12
      
#     while number:
#         div = number // num[y]
#         number %= num[y]
  
#         while div:
#             print(roman[y], end = "")
#             div -= 1
#         y -= 1
  
# contador = 0 
# sec = 0
# anos = int(input('Informe o ano: '))
# while contador < anos:
#     contador+=100
#     if contador / 100:
#         sec+=1
# print("Seculo", end = " ")
# TransformRoman(sec)



    
# horas = 
# entrada = int(input('informe: '))
# saida = int(input('informe: '))
# # duração = 0
# # while entrada < saida:
# #     hr += 1   
# # print(hr)

# entrada = [8.20]
# saida = (22.10)
# for i in entrada:
#     saida -= i
# print(round(saida)


def addcpf(a):
    a = ''
    while len(a) == 11:
        a = ''
    return a

    

cpf = str(input('informe seu cpf: '))    
addcpf(cpf)

# while len(cpf) < 4:
#     cpf = str(input('Erro, informe apenas as informaçoes corretas: '))
# print(f'cpf registrado {cpf}')
    






    
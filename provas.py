#primeira prova Lp01 (Infinity School)

##1º
#nome = input("digite seu nome: ")
#print(f"olá {nome}, seja bem vindo!")

##2º
#numero = float(input("digite um numero "))
#resultado1 = numero * numero
#resultado2 = numero / 3
#print  (f" o numero é {numero}, seu dobro é {resultado1} é sua terça parte é {resultado2}")



#apostilha 2 prova 2 

"""Questão 1"""


# automovel_autonomia = int(12)
# tempo_viagem = float(input('Digite o tempo da viagem: '))
# velocidade_m = float(input('digite a velocidade media durante a viagem: '))
# distancia = tempo_viagem*velocidade_m
# litros_usados = round(distancia / automovel_autonomia)
# print(f'concluindo a viagem em {tempo_viagem}Hr, numa velocidade de {velocidade_m}KM/h, percorrendo uma distancia de {distancia}KM sua autonomia foi {litros_usados} Litros')

"""Questão 2"""



#usando While

# r = 'S'
# mulher = homem = 0
# n= float(input('Digite quantidade de habitantes que moram nesta cidade: '))
# while r == 'S':
#     if n == 0 and n < 1 :
#         print('"ERRO" Verifique seus dados!')
#         break
#     s = int(input('Digite 1 para HOMEM e 2 para MULHER: '))
#     if s != 1 and s != 2:
#         print('"ERRO" Ultilize para responder apenas 1 e 2!')
#         break
#     r = str(input(f'QUER CONTINUAR A PESQUISA? S / N: ')).upper()
#     if r != 'S' and r != 'N':
#         print('"ERRO" Ultilize as informações corretas para responder e continuar!')
#         break
#     if s % 2 == 0:
#         mulher+=1
#         print('MULHER')
#     else:
#         homem+=1
#         print('HOMEM')
# print(f'{homem} do sexo Masculino\n {mulher} do sexo Feminino.')
    
#Usando FOR (em andamento)

# s = 0
# M = 1
# F = 2
# MULHER = HOMEM = 0
# n = float(input('Digite quantidade de habitantes que moram nesta cidade: '))
# n_q = int(input('Quantas destas pessoas voce gostaria de entrevistar ?'))
# for s in range(n_q):
#     s = int(input(f'Se for homem digite {1} se for mulher digite {2}: ')) 
#     if s == n_q:
#         break
#     elif s != 1 and s != 2:
#         print('"ERRO", Verifique seus dados!')
#     elif s == 1:
#         print('homem')
#     else:
#         print('mulher')


"""QUESTÃO 3 """


# adolecente = 0
# jovem = 0
# adulto = 0 
# idoso = 0 
# ansião =0
# for pessoas in range(1,15+1):
#     idade = int(input(f'digite a idade da {pessoas}º pessoa: '))
#     if idade == 0 or idade < 11:
#         print('crianças nao participaram dessa pesquisa.')
#         break
#     if idade <= 15:  
#         adolecente += 1
#     elif idade > 16 and idade < 30:
#         jovem += 1
#     elif idade >= 31 and idade < 45:
#         adulto += 1
#     elif idade >= 46 and idade < 60:
#         idoso +=1
#     else:
#         ansião +=1
# print(f'{adolecente} adolecente/s, {jovem} Jovens, {adulto} adulto/s, {idoso} idoso/s, {ansião} ancião/ões')
# print(f'da primeira a ultima faixa etaria temos o percentual de {adolecente+ansião/100*15}%')


"""QUESTÃO 4"""    



# nota_= 0
# for n in range(1,3+1):
#     nota = float(input(f'digite a {n}º nota do aluno: '))
#     nota_+=nota/3
# print(f' a media de suas notas são: {nota_}')
# presença = str(input('o aluno compareceu no minimo 40 aulas ? S/N: ')).lower()
# if presença !='s' and presença != 'n':
#     print('Responda apenas usando "S" ou "N"')
# elif nota_ > 6 and presença == 's':
#     print('aprovado')
# else: 
#     print('reprovado')


"""QUESTÃO 5"""


valor_d = 0
valor = 0
desconto = 0
for p in range (1,3+1):
    produto = float(input('Digite o valor da compra: '))
    r = str(input('o cliente deseja mais algum produto? S/N: ')).lower()
    valor += produto
    print(f'R${valor}')
    if r!='s' and r != 'n': 
        print('verifique seus dados')
        break
    if valor >= 500 and valor <= 3000 and valor + 100:
        desconto+=1 
        res = (valor*desconto)/100
        print(f'o cliente ganhou um desconto {desconto}% ou seja R$-{res}, o produto ficará no valor de {valor-res} ')      
    else: 
        print('Cliente nao tem direito a desconto')
        


 

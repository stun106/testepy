             #atividade numero 3 da lista de exercicio !

#func = input('digite o nome do funcionario: ')
#salaraio = input('digite salario: ')
#print("O funcionario " +func+ " tem um salario de " +salaraio+" em junho!")

#atividade numero 4 da lista de exercicios ! 

#num = float(input('digite um numero: '))
#num2 = float(input('digite outro numero: '))
#res = (num+num2)
#print("a soma entre " +str(num)+  " e ", num2 , " é igual a: " , res)

#-----------------------------------------------------------------------------

                #EXERCICIOS DA APOSTILA DA INFINITY SCHOOL

#Ex-07

#num = int(9)
#num2 = int(8)
#num3 = int(7)
#dividendo = int(3)
#soma = int(num+num2+num3)
#media = (soma/dividendo)
#print('A media dos numeros é ',str(media))

#Ex-08

#aluno1 = input('digite o nome do aluno: ')
#nota1 = float(7.5)
#nota2 = float(7.8)
#nota3 = float(3.1)
#nota4 = float(5.5)
#print('Aluno: ',aluno1)
#print('Notas : ')
#print(nota1,nota2,nota3,nota4)
#notas = (nota1+nota2+nota3+nota4)
#import math
#media1= math.ceil(notas/4)
#print('Média: ')
#print(media1)

#ex do dia ! 
#a = int(10)
#b = int(50)
#a,b = b,a
#print('a= ',a, ' b= ', b)

# exercicio da postila, calculando IMC
     #(obs: perguntar o professor sobre os operadores logicos dessa função.)

#peso = float(input('digite seu peso: '))
#altura = float(input('digite sua altura: '))
#import math
#imc = math.ceil(peso/altura**2)
#if imc == 27 or imc <= 29 :
    #print('Seu IMC é ', imc,'Sobrepeso Atenção! Alguns quilos a mais já são suficientes para que algumas pessoas desenvolvam doenças associadas, como diabetes e hipertensão. É importante rever seus hábitos. Procure um médico.5')
#else:
    #print('Seu IMC é', imc, 'Você esta obeso, va praticar um esporte!')

#LP01-ex02
#TF = float(input('digite uma temperatura em Fº '))
#TF_Resultado = round((TF - 32) / 9)
#T_Celsios = 5* TF_Resultado
#print(f" Temperatura {TF}º Fahrenheit para {T_Celsios} Celsios" )

#LP01 -ex04

#eleitores = float(input('Total de eleitores: '))
#V_Branco = float(input('Total de votos em branco: '))
#V_Nulos = float(input('Total de votos nulos '))
#V_Validos = float(input('Total de votos validos '))
#validos = (V_Validos / 100) * eleitores / 100
#branco = (V_Branco / 100) * eleitores / 100
#nulos = (V_Nulos / 100) * eleitores / 100
#print(f"Total de votos Validos no municipio : {validos}%"
#f" Total de votos Nulos : {nulos}%"
#f" total de votos em branco {branco}%")

#LP06 -ex06

#v_carro_f  = float(input('digite o valor do automovel: '))
#v_carro_i_f = (73 * v_carro_f) / 100
#valor_total_carro = (v_carro_f+v_carro_i_f)
#print(f" Seu automóvel custara com todos os impostos atribuido: R$ {valor_total_carro}.")


#-------------------------------------------------------------------------

#INTRODUÇÃO A CONDICIONAIS

#aula1 - ex1 

#alunos = int(input('digite o numero de alunos para usar o elevador: '))
#if alunos <= 10 :
    #print("os alunos podem subir!")
#else:
   # print("excesso de peso! NAO PERMITIDO !!")


# ex2 

#aluno = input('digite o nome do aluno: ')
#nota1 = float(input('digite a nota da avaliação I '))
#nota2 = float(input('digite a nota da avaliação II '))
#nota3 = float(input('digite a nota da avaliação III '))
#media = round((nota1+nota2+nota3) / 3)
#if media >= 6:
    #print(f"Parabens sua media foi {media}! você passou!!")
#else:
    #print(f"sua media foi {media}, estude mais da proxima vez!")


#---------------------------------------------------------------------------
#primeira prova Lp01 (Infinity School)

##1º
#nome = input("digite seu nome: ")
#print(f"olá {nome}, seja bem vindo!")

##2º
#numero = float(input("digite um numero "))
#resultado1 = numero * numero
#resultado2 = numero / 3
#print  (f" o numero é {numero}, seu dobro é {resultado1} é sua terça parte é {resultado2}")

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

#ESTRUTURA CONDICIONAL

#Ex1

#numero = int(input("digite um numero: "))
#numero_bol = True
#if numero % 2:
    #numero_bol = False
    #print("falso")
#else:
    #numero_bol= True
    #print("verdadeiro")
    
#ex2 

#Temperatura = int(input("Digite sua temperatura: "))
    #cancela = False
    #if Temperatura <= 37 or Temperatura == 37: 
#cancela:True
#print(f"Sua temperatura é {Temperatura}º pode passar!")
#else: 
#ancela: False
#print(f"Sua temperatura é {Temperatura}º procure um medico")




#Ex 3 (hospital e respiradores)

#respiradores = int(50)
#hosp1 = int(input("digite o numero de ocupação deste hospital: "))
#hosp_resp = int(input("digite quantos respitadores o hospital esta utilizando: "))
#taxa_ocupaçao = (60 * hosp1) / 100
#if taxa_ocupaçao < hosp_resp:
    #print('"ERRO!" Dados incoerentes!')
#elif taxa_ocupaçao <= 60 and hosp_resp >= respiradores:
    #print(f"a taxa de ocupação no hosp1 é {taxa_ocupaçao}% e esta sendo utilizado {hosp_resp}, hospital no padrão")
#else:
    #print(f"a taxa de ocupação no hosp1 é {taxa_ocupaçao}% e esta sendo utilizado {hosp_resp}, iremos mandar mais 5 respiradores!")



from camp import Camp
from amador import amadores
from pro import profissionais
from Lenda import Lendas

camp = Camp()

nome = 'Invitation Madre'
local = 'Madre de Deus - Ba'
premio = 50.000
patro = 'Wave Beach','Feras Beach'
atleta = ['Alejo','Zidane','Medina','SurfistaPrateado','Patolino','Pernalonga']
camp.select(nome,local,premio,patro,atleta)
print(camp.dadoscamp)

print('-'*40,'\n')
#etapa Amador
atletas1 = amadores()
print ('Final Amadores:')
atleta = 'Alejo'
idade = 26
categoria = 'Amador'
pontos = 10
atletas1.select(atleta,idade,categoria,pontos)
print(atletas1.dadoscamp)

atletas2 = amadores()
atleta =  'Zidane'
idade = 22
categoria = 'amador'
pontos = 8
atletas2.select(atleta,idade,categoria,pontos)
print(atletas2.dadoscamp)

#     p/ teste
# atletas3 = Lendas()
# atleta =  'Roberto Carlos'
# idade = 55
# categoria = 'Lendas'
# pontos = 9.5
# atletas3.select(atleta,idade,categoria,pontos)
# print(atletas3.dadoscamp)

print(f'Vencedor: {atletas1.Atletas}')

print('-'*40,'\n')
#etapa Pro
atletasp1 = profissionais()
print ('Final Profissional:')
atleta = 'Medina'
idade = 25
categoria = 'Profissional'
pontos = 45
atletasp1.select(atleta,idade,categoria,pontos)
print(atletasp1.dadoscamp)

atletasp2 = profissionais()
atleta =  'Surfista Prateado'
idade = 42
categoria = 'Profissional'
pontos = 45.5
atletasp2.select(atleta,idade,categoria,pontos)
print(atletasp2.dadoscamp)

atletasL3 = Lendas()
atleta =  'Paladino Mascarado'
idade = 55
categoria = 'Lendas'
pontos = 50
atletasL3.select(atleta,idade,categoria,pontos)
print(atletasL3.dadoscamp)
print(f'Vencedor: {atletasL3.AtletasL}')

print('-'*40,'\n')
#Etapa Lenda
atletasL1 = Lendas()
print ('Final Lendas:')
atleta = 'Patolino'
idade = 78
categoria = 'Lendas'
pontos = 55
atletasL1.select(atleta,idade,categoria,pontos)
print(atletasL1.dadoscamp)

atletasL2 = Lendas()
atleta =  'PernaLonga'
idade = 75
categoria = 'Lendas'
pontos = 100
atletasL2.select(atleta,idade,categoria,pontos)
print(atletasL2.dadoscamp)
    #p/ teste
# atletas3 = amadores()
# atleta = 'Alejo'
# idade = 26
# categoria = 'Amador'
# pontos = 10
# atletas3.select(atleta,idade,categoria,pontos)
# print(atletas3.dadoscamp)
print(f'Vencedor: {atletasL2.AtletasL}')





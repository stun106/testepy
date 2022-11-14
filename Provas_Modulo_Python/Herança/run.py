from Herança import Registros
from Usuario import users
from Friend import Friends
from Family import Families
from Guia import Guia

print('Bem Vindo ao Sistema MyLogTracks\n')
app = Registros()
User = users()
nome = 'Mallu'
idade = 20
endereco = '25 de março, salvador - ba'
friends = 'USUARIO'
User.Select(nome,idade,endereco,friends)

print(f'Informações do Usuario <{User.Date()}>\n')
usuario4 = Guia()
nome = 'BemTeVi'
idade = 35
endereco = 'Chapada Diamantina - BA'
conection = 'Guia'
valor = 150
usuario4.Select(nome,idade,endereco,conection,valor)


print(f'Trilhas Disponiveis {app.Trilhas()}\n\n Guias Disponiveis {usuario4.Date()}\n')


#testando o codigo
print('Trilha selecionada: \n')

app = Registros()
usuario1 = Friends()
nome = 'Nenzoca'
idade = 45
endereco = 'Itinga, Lauro de freitas - Ba'
conection = 'Amigo'
pontos = 25  
app.selectTrilha2(nome,conection,idade)

usuario2 = Families()
nome = 'Marilene'
idade = 15
endereco = '25 de março, salvador - ba'
conection = 'Familia'
pontos = 15
app.selectTrilha2(nome,conection,idade)

usuario3 = Friends()
nome = 'Furinga'
idade = 35
endereco = 'Itinga, Lauro de freitas - Ba'
conection = 'Amigo'
pontos = 25
app.selectTrilha2(nome,conection,idade)

usuario4 = Guia()
nome = 'BemTeVi'
idade = 35
endereco = 'Chapada Diamantina - BA'
conection = 'Guia'
valor = 150
app.selectTrilha2(nome,conection,idade)
app.Game1()

print(f'{app.UserTrilhas},\n Score total: {app.Upontos} Pts!')   

# Desative os comentarios para mais testes

# app = Registros()
# usuario1 = Friends()
# nome = 'ruan'
# idade = 15
# endereco = '25 de março, salvador - ba'
# conection = 'Amigo'
# pontos = 15
# app.selectTrilha1(nome,conection,idade)

# usuario2 = Families()
# nome = 'Lailton'
# idade = 10
# endereco = 'Itinga, Lauro de freitas - Ba'
# conection = 'Familia'
# app.selectTrilha1(nome,conection,idade)
# pontos = 25

# usuario3 = Friends()
# nome = 'Luan'
# idade = 15
# endereco = '25 de março, salvador - ba'
# conection = 'Amigo'
# pontos = 16
# app.selectTrilha1(nome,conection,idade)

# usuario4 = Friends()
# nome = 'Nenzoca'
# idade = 45
# endereco = 'Itinga, Lauro de freitas - Ba'
# conection = 'Amigo'
# app.selectTrilha1(nome,conection,idade)
# pontos = 25

# usuario5 = Friends()
# nome = 'Marilene'
# idade = 20
# endereco = '25 de março, salvador - ba'
# conection = 'Amigo'
# pontos = 15
# app.selectTrilha1(nome,conection,idade)

# usuario6 = Friends()
# nome = 'Furinga'
# idade = 35
# endereco = 'Itinga, Lauro de freitas - Ba'
# conection = 'Amigo'
# app.selectTrilha1(nome,conection,idade)
# pontos = 25

# usuario7 = Friends()
# nome = 'Caio'
# idade = 35
# endereco = '25 de março, salvador - ba'
# conection = 'Amigo'
# pontos = 15
# app.selectTrilha1(nome,conection,idade)

# usuario8 = Families()
# nome = 'Jadiscrei'
# idade = 35
# endereco = 'Itinga, Lauro de freitas - Ba'
# conection = 'Familia'
# app.selectTrilha1(nome,conection,idade)
# pontos = 25

# usuario9 = Friends()
# nome = 'Amendoin'
# idade = 35
# endereco = '25 de março, salvador - ba'
# conection = 'Amigo'
# pontos = 15
# app.selectTrilha1(nome,conection,idade)

# usuario10 = Families()
# nome = 'Leleco'
# idade = 35
# endereco = 'Itinga, Lauro de freitas - Ba'
# conection = 'Familia'
# app.selectTrilha1(nome,conection,idade)
# pontos = 25

# app.Game()

# print(f'{app.UserTrilhas},\n Score total: {app.Upontos} Pts!')   
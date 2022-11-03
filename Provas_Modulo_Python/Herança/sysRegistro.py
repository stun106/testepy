'''[PT-06] Mallu é uma menina muito aventureira e gosta bastante de viajar para fazer trilhas. Porém ela não sabe exatamente como registrar esses momentos. Além das fotos, ela gostaria de obter relatórios anuais sobre as suas viagens e aventuras, podendo recuperar informações como: quantidade de trilhas que fez no ano, quilometragem percorrida, entre outras. Para isso Mallu te convidou a desenvolver o sistema de MyLogTracks, com as seguintes especificações:

O sistema deverá cadastrar pessoas, que podem ser amigos, família ou guia, todos eles devem ser registrados com nome, idade e endereço. Porém  guia terá o cadastro também do valor médio por trilha. No sistema deverá ser cadastrado também trilha, que terá informações das pessoas que foram na trilha e outras informações como: distância total, grau de dificuldade (ex: fácil, médio, difícil, etc), nome e localização (ex: Vale do capão).

Além disso Mallu deseja gameficar as aventuras dela da seguinte forma: Cada trilha que ela fizer, ela obterá uma pontuação, programada da seguinte forma: Cada pessoa que seja da família na trilha, ela recebe 20 pontos, cada amigo 15 pontos, se tiver guia, ela perde 5 pontos, pois ela gosta de aventura. Se tiver qualquer pessoa na trilha com menos que 18 anos, ela ganha ainda + 10 pontos (sempre por pessoa). Se a trilha tiver mais de 10 pessoas, ela perde também 5 pontos.'''

class Registros():
    def __init__(self) -> None:
        self._Name = ''
        self._Age = 0
        self._Andress = ''
        self._Date = {}

    @property
    def Name(self):
        return self._Name
    Name.setter
    def Name(self,nome):
        self._Name = nome
        return self._Name
    
    @property
    def Idade(self):
        return self._Age
    Idade.setter
    def Idade(self,idade):
        self._Age += idade
        return self._Age
    
    @property
    def Endereco(self):
        return self._Andress
    Endereco.setter
    def Endereco(self,endereco):
        self._Andress = endereco
        return self._Andress
    


    def __Insert_Into(self,nome,idade,endereco):
        self.Name(nome)
        self.Idade(idade)
        self.Endereco(endereco)

    @property
    def Select(self):
        return self._Date
    Select.setter
    def Select(self,nome,idade,endereco):
        self.__Insert_Into(nome,idade,endereco)
        self._Date['Nome'] = self._Name
        self._Date['Idade'] = self._Age
        self._Date['Endereço'] = self._Andress
        return self._Date



#teste
# app = Registros()

# nome = 'Kirk Jhonson'
# idade = 26
# endereco = '14 de agosto'
# print(app.Select(nome,idade,endereco))





'''[PT-07] Em um campeonato de surf podem ter 3 categorias:

Amador
Profissional
Lenda
Para todos os tipos de campeonato, temos o cadastro do nome do campeonato, local onde ocorrerá, premiação, patrocinadores (previamente cadastrados com nome e valor) e os atletas. Os atletas terão nome, idade, pontuação e categoria que compete (Amador, profissional ou lenda). Os atletas lenda podem participar de qualquer competição, já os profissionais, apenas do profissional e do amador, sendo que o amador só poderá participar do próprio circuito. É preciso haver este bloqueio no sistema. A pontuação do atleta que ganha o campeonato é:

Amador: 10 pontos
Profissional: 50 pontos
Lenda: 100 pontos'''

class Camp:
    def __init__(self) -> None:
        self.Champ = ''
        self.Local = ''
        self.premio = 0
        self.Patrocinadores = ''
        self.dadoscamp = {}
        self.Atletas = ''

    def insert(self,nome,local,premio,patro,atleta):
        self.Champ = nome
        self.Local = local
        self.premio += premio
        self.Patrocinadores = patro
        self.Atletas = atleta
    
    def select(self,nome,local,premio,patro,atleta):
        self.insert(nome,local,premio,patro,atleta)
        self.dadoscamp['Evento'] = self.Champ
        self.dadoscamp['Localidade'] = self.Local
        self.dadoscamp['Premiação'] = self.premio
        self.dadoscamp['Patrocinadores'] = self.Patrocinadores
        self.dadoscamp['Atletas'] = self.Atletas
        print('Registro concluido')




    









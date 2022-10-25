from Lenda import Lendas
from camp import Camp
class profissionais(Lendas,Camp):
    def __init__(self) -> None:
        super().__init__()
        self.Atletasp = ''
        self.Idadep = []
        self.Categoriap = ''
        self.Pontuacaop = []


    def insert(self,atleta,idade,categoria,pontos):
        self.Atletasp = atleta
        self.Idadep.append(idade)
        self.Categoriap = categoria
        self.Pontuacaop.append(pontos)
    
    def select(self,atleta,idade,categoria,pontos):
        self.insert(atleta,idade,categoria,pontos)
        self.dadoscamp['Atleta'] = self.Atletasp
        self.dadoscamp['Idade'] = self.Idadep
        self.dadoscamp['Categoria'] = self.Categoriap
        self.dadoscamp['Pontuação'] = self.Pontuacaop
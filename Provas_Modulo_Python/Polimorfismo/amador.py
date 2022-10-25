from Lenda import Lendas
from camp import Camp
class amadores(Lendas,Camp):
    def __init__(self) -> None:
        super().__init__()
        self.Atletas = ''
        self.Idade = []
        self.Categoria = ''
        self.Pontuacao = []


    def insert(self,atleta,idade,categoria,pontos):
        self.Atletas = atleta
        self.Idade.append(idade)
        self.Categoria = categoria
        self.Pontuacao.append(pontos)
        
    
    def select(self,atleta,idade,categoria,pontos):
        self.insert(atleta,idade,categoria,pontos)
        self.dadoscamp['Atleta'] = self.Atletas
        self.dadoscamp['Idade'] = self.Idade
        self.dadoscamp['Categoria'] = self.Categoria
        self.dadoscamp['Pontuação'] = self.Pontuacao
        print('MenssageBox: Dados Persistidos com sucesso!')
       




       








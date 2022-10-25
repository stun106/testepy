from camp import Camp
class Lendas(Camp):
    def __init__(self) -> None:
        super().__init__()
        self.AtletasL = ''
        self.IdadeL = []
        self.CategoriaL = ''
        self.PontuacaoL = []


    def insert(self,atleta,idade,categoria,pontos):
        self.AtletasL = atleta
        self.IdadeL.append(idade)
        self.CategoriaL = categoria
        self.PontuacaoL.append(pontos)
    
    def select(self,atleta,idade,categoria,pontos):
        self.insert(atleta,idade,categoria,pontos)
        self.dadoscamp['Atleta'] = self.AtletasL
        self.dadoscamp['Idade'] = self.IdadeL
        self.dadoscamp['Categoria'] = self.CategoriaL
        self.dadoscamp['Pontuação'] = self.PontuacaoL
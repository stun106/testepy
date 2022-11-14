from Herança import Registros
class Guia(Registros):
    def __init__(self) -> None:
        super().__init__()
        self._ValorPorTrilha = 150


    @property
    def ValorGuia(self):
        return self._ValorPorTrilha
    ValorGuia.setter
    def ValorGuia(self,valor):
        self._ValorPorTrilha = valor

    def __Insert_Into(self, nome, idade, endereco,conection,valor):
        self._Name = nome
        self._Age = idade
        self._Andress = endereco
        self.FriendConection = conection
        self._ValorPorTrilha = valor

    def Select(self, nome, idade, endereco,conection,valor):
        self.__Insert_Into(nome,idade,endereco,conection,valor)
        self._Date['Nome'] = self._Name
        self._Date['Idade'] = self._Age
        self._Date['Endereço'] = self._Andress
        self._Date['Conecção'] = self.FriendConection
        self._Date['Valor/Serviço'] = self._ValorPorTrilha
        return self._Date


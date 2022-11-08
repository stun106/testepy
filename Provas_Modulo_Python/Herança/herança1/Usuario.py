from Herança import Registros
class users(Registros):
    def __init__(self) -> None:
        super().__init__()

    def __Insert_Into(self, nome, idade, endereco,conection):
        self._Name = nome
        self._Age = idade
        self._Andress = endereco
        self.FriendConection = conection

    def Select(self, nome, idade, endereco,conection):
        self.__Insert_Into(nome,idade,endereco,conection)
        self._Date['Nome'] = self._Name
        self._Date['Idade'] = self._Age
        self._Date['Endereço'] = self._Andress
        self._Date['Conecção'] = self.FriendConection
        return self._Date



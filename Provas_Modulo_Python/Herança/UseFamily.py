from sysRegistro import Registros
class Families(Registros):
    def __init__(self) -> None:
        super().__init__()
        self.FriendConection = ''
        self.Pontos = 0

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


#teste
# usuario = Families()
# nome = 'Lailton'
# idade = 35
# endereco = 'Itinga, Lauro de freitas - Ba'
# conection = 'Familia'
# print(usuario.Select(nome,idade,endereco,conection))
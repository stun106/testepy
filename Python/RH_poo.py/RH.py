from random import randint
from pessoa import*
class RH:
    
    def __init__(self,nome,sexo):
        self.matricula = 0
        self._salario = 1450
        self.Funcionario = Pessoa(nome,sexo)

    @property
    def salario(self):
        return self._salario
    
    @salario.setter                                                 #<--- Encapsulamento
    def salario(self,experiencia):
        if experiencia > 6:
            self._salario += self._salario*20/100
            return self._salario


    def geradorMatricula(self):
        self.matricula = [randint(0,100) for x in range(0,4)]     #<-- gerador de matriculas onde a funçao randinit varia de 0,100 enquando atribui valores ateatoriamente em 4 indices de uma lista.
        return self.matricula

    def addFuncionario(self,cpf):
        self.geradorMatricula()
        self.Funcionario.dadosPessoa[self.Funcionario.nome] = self.Funcionario.cpf
        self.Funcionario.cpf.append(cpf)                                                #<-- metodo para adicionar funcionarios 
        self.Funcionario.dadosPessoa[self.Funcionario.sexo] = self.matricula
        return self.Funcionario.dadosPessoa


 



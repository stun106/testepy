"""[PT-A04] Você foi convidado a desenvolver um sistema para registro de um estacionamento, onde mantém informações sobre os veículos que entram e saem do local. Os veículos são cadastrados com tipo do veículo (carro, moto, caminhão, etc.), placa, modelo, data e horário de entrada e data e horário de saída, com um valor total a pagar. O sistema deve receber como input o valor da hora e só deve atribuir o total a pagar no momento que receber a informação do horário de saída, que não é obrigatório inserir na hora do registro do veículo. Para isso, deve-se encapsular todos os atributos e ter mapeado a regra que a saída do veículo não poderá ser mais antiga que a entrada dele no estacionamento."""


class Registro:
    def __init__(self,name,cpf,tipoauto,model,placa):
        self.Name = name
        self.Cpf = cpf
        self.Automovel = tipoauto
        self.Modelo = model
        self.placa = placa
        




        
from supermercado import Systemercado
from cliente import Cliente

Mercado = Systemercado()

while True:
    print('Bem vindos ao Systermercado!')
    print('para ser um cliente vip basta apenas se cadastrar..')
    question = input('Deseja se tornar um cliente Vip: [Y/N]')
    if Mercado.ClienteVip(question) == True:
        Name = str(input('informe seu nome: '))
        cpf = str(input('informe seu CPF: '))
        endereço = str(input('informe seu endereço: '))
        Mercado.Cadastro(Name,cpf,endereço)
        print(Mercado.Pessoa.pessoa)



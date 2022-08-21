from supermercado import Systemercado
from carrinhodecompra import CarrinhoDeCompras

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
        carrinho = CarrinhoDeCompras()   
        print(Mercado.produtospreços)
        Pedido = input('adicione no carrinho suas compras: ')
        carrinho.addCarrinho(Pedido)
        print(carrinho.Carrinho)
    



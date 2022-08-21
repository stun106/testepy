from ast import Pass
from supermercado import Systemercado
from carrinhodecompra import CarrinhoDeCompras

Mercado = Systemercado()

while True:
    print('Bem vindos ao Systermercado!')
    print('para ser um cliente vip basta apenas se cadastrar..')
    question = input('Deseja se tornar um cliente Vip: [Y/N]: ')
    if Mercado.ClienteVip(question) == True:
        print('Concluindo o cadastro cliente terá descontos de 10%! ')
        Name = str(input('informe seu nome: '))
        cpf = str(input('informe seu CPF: '))
        endereço = str(input('informe seu endereço: '))
        Mercado.Cadastro(Name,cpf,endereço)
        print(Mercado.pessoa)
        Mercado.Vip = True
        Pass
    if Mercado.Vip == True:
        carrinho = CarrinhoDeCompras()  
        while True: 
            print(Mercado.produtospreços)
            Pedido = input('adicione no carrinho suas compras: ')
            carrinho.addCarrinho(Pedido)
            question = input('Deseja continuar comprando [Y/N]: ')
            if Mercado.ClienteVip(question) == False:
                print(carrinho.Carrinho)
                print(f'Valor de sua compra: \033[1;32m{carrinho.Compra(Pedido,question)} R$\033[0;0m')
    else:
        Mercado.vip = False
        carrinho = CarrinhoDeCompras()  
        while True: 
            print(Mercado.produtospreços)
            Pedido = input('adicione no carrinho suas compras: ')
            carrinho.addCarrinho(Pedido)
            question = input('Deseja continuar comprando [Y/N]: ')
            if Mercado.ClienteVip(question) == False:
                print(carrinho.Carrinho)
                print(f'Valor de sua compra: \033[1;32m{carrinho.Compra(Pedido,question)} R$\033[0;0m')
                carrinho.resetsystem()
        
            
             
    



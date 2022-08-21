'''Crie uma classe CarrinhoDeCompras onde os atributos serão duas listas, uma para os produtos e outra para seus respectivos preços, se o cliente é VIP ou não e o total da compra que deve ser iniciado com 0.0.
Em seguida, crie os métodos para adicionar produtos ao carrinho e o exibir total da compra, que deverá imprimir em tela todos os produtos, os preços e, por fim, o total. Se o cliente for VIP, a compra terá 10% de desconto.'''

class Cliente: 
    def __init__(self,Vip = False):
        self.pessoa = {}
        self.Vip = Vip



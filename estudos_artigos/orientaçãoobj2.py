#Crie uma CLASSE chamada ContasBancarias com os seguintes atributos 
#Conta, Correntista, saldo, tipo, agencia
#e os seguintes métodos:
# Sacar()
# Depositar()
# ListarMov()
# Abrir()
# Encerrar()



class ContasBancarias:
    extrato = []
    def __init__(self, Conta,Agencia, Correntista,Tipo):
        self.Depositar = Conta
        self.Correntista = Correntista
        self.Saldo = 0
        self.Tipo = Tipo
        self.Agencia = Agencia
        self.extrato

    def verificador(self,a,b = 'y'):
        if a == b:
            return True
        else:
            return  False

    def depositar(self,Valor):
        self.Saldo+=Valor
        self.extrato.append(self.Saldo)
        return MinhaConta.Saldo
    
    def sacar(self,Valor):
        if self.Saldo >= Valor:
            self.Saldo-=Valor
            self.extrato.append(self.Saldo)
            return MinhaConta.Saldo
        else: 
            return('Saldo insuficiente para Saque.')


cc = input('informe sua conta: ')
ag = input('informe a agencia: ')
Prop = input('informe o nome do Correntista: ')
tipo = input('informe o tipo da conta: ')


MinhaConta = ContasBancarias(cc,ag,Prop,tipo)
print(f'''Bem vindo ao banco {MinhaConta.Correntista},
            seu Saldo é {MinhaConta.Saldo}
        ''')


podeDepositar = input('deseja depositar? digite [Y/N] Sim ou Não:')
if(MinhaConta.verificador(podeDepositar) == True):
    Dep = float(input('Digite o Valor do deposito: '))
    MinhaConta.depositar(Dep)
    print(f'Deposito no valor de R$  \033[1;32m {MinhaConta.Saldo} \033[0;0m bem sucedido')


podeSacar = input('deseja sacar? digite [Y/N] Sim ou Não:')
if(MinhaConta.verificador(podeSacar) == True):
    Sac = float(input('digite o valor do seu saque: '))
    MinhaConta.sacar(Sac)
    print(f'Você retirou R$ \033[1;31m{Sac}\033[0;0m da sua conta')
    print(f'Saldo atual: R$ {MinhaConta.Saldo}')

tirarExtrato = input('deseja consultar o extrato? digite [Y/N] Sim ou Não:')
if(MinhaConta.verificador(tirarExtrato) == True):
    print(MinhaConta.extrato)

    





 




   

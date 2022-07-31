#Crie uma CLASSE chamada ContasBancarias com os seguintes atributos 
#Conta, Correntista, saldo, tipo, agencia
#e os seguintes métodos:
# Sacar()
# Depositar()
# ListarMov()
# Abrir()
# Encerrar()



class ContasBancarias:

    def __init__(self, Conta,Agencia, Correntista,Tipo):
        self.Depositar = Conta
        self.Correntista = Correntista
        self.Saldo = 0
        self.Tipo = Tipo
        self.Agencia = Agencia

    def verificador(self,a,b = 'y'):
        if a == b:
            return True
        else:
            return  False

    def depositar(self,Valor):
        self.Saldo+=Valor
        return MinhaConta.Saldo


cc = input('informe sua conta: ')
ag = input('informe a agencia: ')
Prop = input('informe o nome do Correntista: ')
tipo = input('informe o tipo da conta: ')

MinhaConta = ContasBancarias(cc,ag,Prop,tipo)
print(f'''Bem vindo ao banco {MinhaConta.Correntista},
        seu Saldo é {MinhaConta.Saldo}
        ''')


podeDepositar = input('deseja depositar? digite [Y/N] Sim ou Não:')
Dep = float(input('Digite o Valor do deposito: '))
if(MinhaConta.verificador(podeDepositar) == True):
    MinhaConta.depositar(Dep)
    print(MinhaConta.Saldo)



 




   

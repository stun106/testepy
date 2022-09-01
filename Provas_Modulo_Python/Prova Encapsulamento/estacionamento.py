from datetime import date
from sysEstacionamento import sysEstacionamento
sys = sysEstacionamento()

# while True:
#     print('='*50)
#     print('\n')
#     print('Salvador Shopping Pay Parking')
#     print('\n')
#     print('='*50)
    # nameInfo = input('informe seu nome: ')
    # cpfInfo = input('Informe seu cpf: ')
    # typeAuto = input('informe o tipo do veiculo, ex (moto, caminhão) : ')
    # modelo = input('informe o modelo do veiculo: ')
    # placa = input('informe a placa do veiculo: ')
sys.Dados()
entradaInfo = float(input('Horario da entrada ex(8.30): '))
saidaInfo = float(input('Horario de saida, Ex(13.00): '))
print (f'{sys.Dados()}\n{date.today()} - Entrada:{sys.addEntrada(entradaInfo)} Saida:{sys.addSaida(saidaInfo)}\nValor:')


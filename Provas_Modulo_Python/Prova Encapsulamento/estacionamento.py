from datetime import date
from sysEstacionamento import sysEstacionamento
while True:
    print('='*50)
    print('Salvador Shopping Pay Parking')
    print('='*50)
    name = input('informe seu nome: ')
    cpf = float(input('Informe seu cpf: '))
    tipoauto = input('informe o tipo do veiculo, ex (moto, caminhão) : ')
    model = input('informe o modelo do veiculo: ')
    placa = input('informe a placa do veiculo: ')
    sys = sysEstacionamento(name,cpf,tipoauto,model,placa)
    print(sys.Dados())
    print('='*50)
    print('\n')
    entradaInfo = float(input('Horario da entrada ex(8.30): '))
    question = input('press "Y" para Sair e realizar pagamento: ')
    
    if (sys.verificador(question)) == True:
        saidaInfo = float(input('Horario de saida, Ex(13.00): '))
        print (f'{sys.Dados()}\n{date.today()} - Entrada:{sys.addEntrada(entradaInfo)} Saida:{sys.addSaida(saidaInfo)}\nValor: R$ {sys.sysCobranca(entradaInfo,saidaInfo)} ')

    else:
        print('siga as instruções a cima')
        continue


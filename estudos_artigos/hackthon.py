# Auxiliar o controle de doaçoes realizadas para o evento e as preferencias de instituiçoes



dados = []
doaçoes = []
while True:
    name = input('Informe o nome do doador: ' )
    cpf = input('informe o cpf do doador: ')
    item = input('informe  doação: ')
    quant =input('informe a quantidade: ')
    confirm = input('aperte "Y" para validar a doao, ou digite "X" para consultar os dados: ').lower()
    dados = dados + [{
        'name' : name,
        'cpf' : cpf,
    }]

    doaçoes = doaçoes + [{
    'item' : item,
    'quant' : quant,
    }]
    if confirm != 'y' and confirm != 'x':
        print('Verifique seus dados')
        continue
    else:
        break

print(dados[0]['name'],'- ', dados[0]['cpf'])
print(doaçoes[0]['item'],'- ',doaçoes[0]['quant'] )

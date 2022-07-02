#Ex (Elif = else+if)

nome = (input('digite o nome do empregado: '))
registro = 6666
ano = int(input(f'digite o ano que {nome} nasceu: ')) 
ano_ingresso = int(input('digite o ano de ingresso na empresa:'))
ano_res = int(2022 - ano)
data_in = int(2022 - ano_ingresso)
if ano_res == 65 or ano_res > 65: 
    print(f'Funcionario {nome} com numero de registro {registro} tem {ano_res}anos e trabalha a {data_in} anos conosco, por isso esta apto para se aposentar . ')
elif data_in == 30 and data_in > 30: 
    print(f'Funcionario {nome} com numero de registro {registro} tem {ano_res}anos e trabalha a {data_in} anos conosco, por isso esta apto para se aposentar por tempos de serviço.')
else: 
    print(f'Funcionario {nome} com numero de registro {registro} tem {ano_res}anos e trabalha a {data_in} anos conosco, por isso não esta apto para aposentadoria .')
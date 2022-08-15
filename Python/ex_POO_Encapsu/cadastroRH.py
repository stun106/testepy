from pessoa import*
from RH import*

nome = input('Informe o nome do Funcionario: ')
sexo = str(input('informe o sexo do Funcionario: '))
cpf = int(input('informe o cpf do funcionario: '))
Funcionarios = RH(nome,sexo)
Funcionarios.addFuncionario(cpf)
experiencia = int(input('informe a quantidade de meses do contrato: '))
Funcionarios.salario = experiencia
print(f'{Funcionarios.Funcionario.dadosPessoa}\nSalario: {Funcionarios.salario}')



    
    
        
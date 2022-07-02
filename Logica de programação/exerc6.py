#LP06 -ex06 Programa para calcular imposto de carros

v_carro_f  = float(input('digite o valor do automovel: '))
v_carro_i_f = (73 * v_carro_f) / 100
valor_total_carro = (v_carro_f+v_carro_i_f)
print(f" Seu automóvel custara com todos os impostos atribuido: R$ {valor_total_carro}.")
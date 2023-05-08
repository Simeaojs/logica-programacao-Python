
sal_base = 0
vantagens = 0
desc = 0

sal_base = float(input('Digite o Salario Liquido: '))
vantagens = float(input('Digite as vantagens: '))
desc = float(input('Digite os descontos: '))

sal_liquido = sal_base + vantagens - desc

print('O Salario Base foi: ', sal_liquido)

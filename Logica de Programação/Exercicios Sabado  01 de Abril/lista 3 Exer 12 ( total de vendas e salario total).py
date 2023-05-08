print()

tot_vendas = 0
tot_salario = 0
comisao = 0

while True:
    n_matricula = int(input(' Digite a Matricula: '))
    if n_matricula == 99:
        break
    sal_fixo = float(input('Digite o Salario fixo: '))
    tot_venda = float(input('Digite o total de vendas: '))

    if tot_venda > 1000:
        comisao = tot_venda - 1000
        novo_sal = sal_fixo +(1000 * 0.03)+(comisao * 0.05)
        
    else:
        novo_sal = sal_fixo + (comisao * 3/100) 
        
    print(f'Matricula do vendedor:{n_matricula}')
    print(f'Salario fixo:{sal_fixo}R$')
    print(f'Comisão:{comisao}R$')
    print(f'Novo Salario:{novo_sal}R$')
            

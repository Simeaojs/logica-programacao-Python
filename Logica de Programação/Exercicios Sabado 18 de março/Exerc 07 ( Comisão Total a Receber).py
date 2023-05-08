print()

sal_fixo = float(input('Qual foi o Salario fixo do Vendedor?: '))
tot_vendas = float(input('O total de vendas Efetudas: '))

tot_a_receber = sal_fixo + (tot_vendas * 0.15)

print(f'O Total A Receber sera:R$:{tot_a_receber:.2f}')

# Entrada

# Nome vendedor
# Salario fixo
# Vendas por Mês

# Procesamento

# Acrecentar + 15% de comisão sobre suas vendas

# Saida

# Informar seu nome
# Salario Fixo
# Salario no final do mês


print()

nome_vend = input(" Informe seu nome:")
sal_fixo = float(input(" Informe seu Salario fixo:R$"))
venda_mes = float(input(" Quanto de vendas nesse mês?: R$"))

# calcula a comissão do vendedor multiplicando o total de vendas por 15% (0.15)
venda_mes = venda_mes * 0.15

# Por fim, calcula o salário total somando o salário fixo e as vendas do mês
sal_final_mes = sal_fixo + venda_mes
print()

# imprime os resultados na tela.
print("Nome:", nome_vend)
print()
print(f" Salario fixo: R${sal_fixo:.2f}")

print(f" Salario Final do mês: R${sal_final_mes:.2f}")

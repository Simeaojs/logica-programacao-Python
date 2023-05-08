
# Entrada

# Custo do produto
# Percentual informado pelo usuario

# processamento

# Acrescimo sobre o custo informado pelo usuario

# Saida

# Valor de venda


print()
cust_prod = float(input(' Digite o custo do produto:R$ '))
percent = float(input(' Informe um percentual para retono: %'))

vlr_venda = (percent*cust_prod / 100) + cust_prod

print(f'O valor de venda sera: R${vlr_venda:.2f}')

# Entrada

# Custo de fabrica

# Processamento

# custo de fabrica + porcentagem do distribuidor + impostos
# aplicados primeiro o imposto depois a percentagem sobre o resultado
# a percentagem do distribuidor seja de 28% e os impostos de 45%

# Saida

# custo

print()

# Na primeira linha, utilizamos a função input para pedir ao usuário que digite o custo de fábrica do carro.
# Em seguida, convertemos o valor para um número de ponto flutuante utilizando a função float.
cust_fabri = float(input(" Digite o custo de fabrica: R$"))

# Na segunda linha, calculamos o valor dos impostos, que correspondem a 45% do custo de fábrica.
imposto = 0.45 * cust_fabri
# Na terceira linha, calculamos o valor da percentagem do distribuidor, que corresponde a 28% da soma do custo de fábrica com os impostos.
custo_distri = 0.28 * (cust_fabri + imposto)
# Na quarta linha, somamos os três valores calculados para obter o custo ao consumidor.
consumidor = cust_fabri + imposto + custo_distri

print()

# Utilizamos a letra f dentro das chaves da string formatada para indicar que queremos um número de ponto flutuante,
# e utilizamos :.2f para indicar que queremos apenas duas casas decimais.
print(f"O valor final do carro sera: R${consumidor:.2f}")

# Loop While
print()

populacao_a = 90000
populacao_b = 200000
# Taxas de Crecimento
taxa_a = 0.03
taxa_b = 0.015
anos_necessarios = 0

while (populacao_a < populacao_b):
    anos_necessarios += 1 #incremento
    populacao_a = populacao_a*(1 + taxa_a)
    populacao_b = populacao_b*(1 + taxa_b)
print(f'Serão Necessarios {anos_necessarios} anos Para a população do Pais A Utrapasse ou Iguale do Pais B.') 

# Loop For
'''print()

populacao_a = 90000
populacao_b = 200000
# Taxas de Crecimento
taxa_a = 0.03
taxa_b = 0.015
anos_necessarios = 0
for ano in range (1,1000000):
    populacao_a = populacao_a*(1+taxa_a)
    populacao_b = populacao_b*(1+taxa_b)
    if populacao_a >= populacao_b:
        anos_necessarios = ano 
        break
print(f'Serão Necessarios {anos_necessarios} anos Para a população do Pais A Utrapasse ou Iguale do Pais B.')'''

populacaoA = 100000
populacaoB = 300000
taxa_cresA = 0.03
taxa_cresB = 0.015

anosCress = 0
while populacaoA < populacaoB:

    populacaoA = populacaoA * (taxa_cresA + 1)
    populacaoB = populacaoB * (taxa_cresB+1)
    anosCress = anosCress + 1
print(' Sera necessarios', anosCress,
      'Para que a polpulado do pais A ultapasse a do pais B')
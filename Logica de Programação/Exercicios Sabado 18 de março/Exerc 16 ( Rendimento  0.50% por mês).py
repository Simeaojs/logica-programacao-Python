print()

print('Taxa de juros de 0.50% ao mês:')

juros_taxa =  0.5 / 100

deposito = float(input('Quanto quer Investir?: '))

juros = deposito * juros_taxa

rendimento_mes = deposito + juros

print(f' O seu investimento de R$:{deposito:.2f} Terá um Rendimento de R$:{rendimento_mes:.2f} por mês')

'''TAXA_JUROS = 0.005 / 100  # Taxa de juros mensal

deposito = float(input('Quanto deseja investir? R$ '))

juros = deposito * TAXA_JUROS
rendimento = deposito + juros

print(f'Seu investimento de R$ {deposito:.2f} renderá R$ {rendimento:.2f} em um mês.')'''


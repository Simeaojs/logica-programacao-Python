
# Entrada

# idade em anos
# meses e dias

# Processamento5

#

#  Saida

# Mostrar expressa apenas em dias


print()

idade_anos = int(input(' Digite sua idade:'))
idade_mes = int(input(' Digite os meses:'))
idade_dias = int(input(' Digite os dias:'))

# Ira multiplicar idade em anos x365
# Ira multiplicar idade em mes x 30
# Depois ira somar idade em anos + idade em meses com os dias
idade_dias = (idade_anos*365)+(idade_mes*30)+idade_dias

print()
print(' Sua idade em dias é:', idade_dias, 'Dias')

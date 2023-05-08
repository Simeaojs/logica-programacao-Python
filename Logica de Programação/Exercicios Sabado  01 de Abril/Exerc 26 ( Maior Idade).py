# Loop While
print()

maior_idade = 0

while True:
    idade = int(input('Digite a Idade ou 100 Para Encerrar: '))
    if idade == 100:
        break
    if idade > maior_idade:
        maior_idade = idade
print(f'A Maior idade Recebida foi:{maior_idade}')

#Loop for
'''print()

maior_idade = 0

for idade in range (1,100):
    idade = int(input('Digite a Idade ou 100 Para Encerrar: '))
    if idade == 100:
        break
    if idade > maior_idade:
        maior_idade = idade
print(f'A Maior idade Recebida foi:{maior_idade}')'''
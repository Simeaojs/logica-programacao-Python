print()
menor_peso = 99999 # Inicializa o menor peso como infinito
while True:
    peso = float(input(' digite o peso em Kg: '))
    if peso > 200:
        print('Peso superior a 200Kg:')
        break
    if peso < menor_peso:
        menor_peso = peso
print(' Menor peso foi:', menor_peso)

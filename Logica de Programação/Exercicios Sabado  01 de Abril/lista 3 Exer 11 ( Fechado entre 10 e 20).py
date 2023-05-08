print()

fora_intervalo = 0
dentro_intervalo = 0

for i in range(5):
    numero = float(input(' Digite os valore para saber de estão dentro ou fora do intervalo entre 10 e 20: '))
    if numero >= 10 and numero <= 20:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print(' O valores dentro do intervalo sao:',dentro_intervalo,'E fora do intervalo são:',fora_intervalo)
    
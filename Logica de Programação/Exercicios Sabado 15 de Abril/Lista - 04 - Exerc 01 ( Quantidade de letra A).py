

quantiA = 0

for c in range(5):
    frase = input('Digite a frase: ')
    tam = len(frase)
    quantiA = quantiA + frase.lower().count('a')
print('A quantidade de "a" nas Frases foi: ', quantiA)

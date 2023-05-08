print()

maior = -1
for i in range(5):
    frase = input('Digite as Frases: ')
    tam = len(frase)
    if tam > maior:
        maior = tam
        maiorfrase = frase
print('A maior frase foi:', maiorfrase, 'Com o Tamanho:', maior)

print()
# Forma 01

frase = input('Digite sua Frase: ')
tam = len(frase)
contA = 0
for p in range(tam):
    if frase[p].lower() == 'a':
        contA = contA + 1
print('A quantidade de "a":', contA)

# Forma 02

print('A quantidade de "a":',frase.lower().count('a'))
print('A frase invertida : ',frase[::-1])
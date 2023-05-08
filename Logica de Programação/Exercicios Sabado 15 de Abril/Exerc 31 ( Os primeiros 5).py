print()

frase = input('frase: ')

ra = frase[0:5]  # Os primeiros 5 caracteres da frase.
rb = frase[-5:]  # Os ultimos 5 caracteres da frase.
rc = ra[::-1]    # Os primeiros 5 caracteres da frase invertidos.
tam = len(frase)  # Conta Quantos Caracteres tem na frase.

print('Ra:', ra)
print('Rb:', rb)
print('Rc:', rc)
print(frase[0:5][::-1])
print('O tamanho da frase:', tam)

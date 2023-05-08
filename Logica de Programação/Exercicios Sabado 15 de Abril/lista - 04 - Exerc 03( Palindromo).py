
while True:
    frase = input('Digite a frase: ').upper()
    if frase == 'fim':
        break
    aux = frase.replace(' ', '')
    if frase == frase[::-1]:
        print('A frase',aux,'É um Palindromo')
    else:
         print('A frase',aux,'Não é um Palindromo')

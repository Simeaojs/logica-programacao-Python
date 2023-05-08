

'''peso=float(input(' Digite o peso :'))
if peso>50:
    excesso=peso-50
    multa=peso*4
    print(' Excesso:',excesso)
    print(' multa:',multa)
else:
    print('Peso Ok')'''

peso = float(input('Qual foi o peso do peixe?: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
    print(f'O Excesso foi: {excesso}Kg')
    print(f'A multa foi de: {multa}R$')
else:
    print(' Não Houve Excesso de peso!')    

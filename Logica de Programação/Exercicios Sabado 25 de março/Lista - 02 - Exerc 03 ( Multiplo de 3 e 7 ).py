print()
numero = int(input(" Escreva um numero "))
r1 = numero % 3
r2 = numero % 7
if r1 == 0 and r2 == 0:
    print("Multiplo de 3 e 7")
else:
    print("Nao e multiplo de 3 e 7")

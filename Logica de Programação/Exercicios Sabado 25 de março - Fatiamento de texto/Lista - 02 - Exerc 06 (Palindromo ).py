print()
n = int(input(" Digite cinco numeros inteiros"))
dm = n // 10000
r1 = n % 10000
m = r1 // 1000
r2 = r1 % 1000
c = r2 // 100
r3 = r2 % 100
d = r3 // 10
u = r3 % 10
if dm == u and m == d:
    print("E um PALINDROMO")
else:
    print("Nao e um PALINDROMO")
# Usando Fatiamento de texto

n = input(" Numero: ")
if n == n[::-1]:
    print(" E um PALINDROMO ")
else:
    print(" Nao é um PALINDROMO")

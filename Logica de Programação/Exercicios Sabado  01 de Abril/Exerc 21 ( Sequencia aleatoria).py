# Loop While

print()

numeros = 1
soma = 0
i = 0

while i < 5:
    numero = float(input("Digite o número: "))
    numeros+=1
    soma += numero
    i += 1

media = soma / 5

print("A soma dos números é:", soma)
print("A média aritmética dos números é:", media)


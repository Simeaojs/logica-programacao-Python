print()
numero = int(input(" Digite um numero inteiro positivo entre 0 e 999:"))

# Mostra o primeiro numero da direita pra esquerda Ex: 764%10 = 4
unidade = numero % 10

# Divisão interia da dezena depois mostrando o primeiro numero da direita Ex: (764//10=76)(76%10=6)
dezena = numero // 10 % 10

# Divisão inteira da Dezena Ex: 764 // 100 = 7
centena = numero // 100

print("\ncentena:=", centena, "\ndezena:=", dezena, "\nunidade:=", unidade)

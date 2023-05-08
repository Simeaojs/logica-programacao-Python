
nome = input('Digite seu nome: ').upper() # Usando o modo .upper() para receber o nome maiusculo
for i in range(len(nome)+1):# Usando o loop for para fazer a iteraçao de 0 ate o comprimento do nome +1
    print(nome[:i])

print()

maior_idade = -1
menor_idade = 999999 # Pra achar o nome da pesso mais nova 
soma_idade = 0
for i in range(10):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    # Descobrindo a maior idade e o nome da pessoa mais velha
    if idade > maior_idade:
        maior_idade = idade 
        nome_velha = nome

    # Descobrindo a menor idade e o nome da pessoa mais velha
    if idade < menor_idade:
        menor_idade = idade
        nome_nova = nome 
    # Insumo para descibrir a media
    soma_idade = soma_idade + idade

print(' A maior idade Resgitrada foi de:',nome_velha,'com',maior_idade,'anos')   
print(' O nome da pessoa mais nova é:',nome_nova,'com',menor_idade,'anos')     
media = soma_idade / i # Achando a media 
print('A media das idades foi: ',media)
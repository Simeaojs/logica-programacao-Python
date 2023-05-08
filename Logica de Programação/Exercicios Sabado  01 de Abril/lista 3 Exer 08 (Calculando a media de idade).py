print()

soma = 0 # Varialvel pra achar a media de pessoas
tot_pessoas = 0 # Contador 

while True:
    idade = int(input('Digite a idade: '))
    if idade == 0:
        break  # Comando de parada se o numero for igual a (0)

    # Fazendo a soma pra poder achar a media
    soma = soma + idade
    tot_pessoas += 1  # Contador. A Cada loop Acrescenta  + 1 ao total de pessoas

# achando a media as somas das idades / pelo total de pessoas
media = soma / tot_pessoas
print(' A media de idade desse grupo de pessoas e:', media)

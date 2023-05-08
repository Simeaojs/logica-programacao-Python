print()

'''Tem-se um conjunto de dados contendo altura e sexo (“M” ou “F”) de 50 pessoas, fazer um 
programa que calcule e escreva:

a) a maior e a menor altura do grupo
b) média de altura das mulheres
c) o número de homens'''

maior_altura = -1
menor_altura = 999999
soma_altura = 0
tot_homens = 0
tot_mulheres = 0

while True:
    sexo = input('Digite o sexo M ou F ou Digite fim para encerrar:')
    if sexo == 'fim':
        break
    altura = float(input('Altura: '))

    if altura > maior_altura:
        maior_altura = altura

    if altura < menor_altura:
        menor_altura = altura

    if sexo == 'f':
        tot_mulheres = tot_mulheres + 1
        soma_altura = soma_altura + altura

    else:
        tot_homens = tot_homens + 1
print()
print('A maior altura do grupo foi:',maior_altura, 'e a menor foi:', menor_altura)
media = soma_altura / tot_mulheres
print('A media da altura das mulheres foi:',media)
print('O numero de homens foi:', tot_homens)

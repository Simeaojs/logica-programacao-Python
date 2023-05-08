'''print()
numeros = 0
numero = 0
soma = 0
quantidade = 0
soma_pares = 0
quantidade_pares = 0

while (numero != 999):
    numero = int(input('Digite um numero: '))
    if numero != 999:
        numeros += numero
        soma += numero
        quantidade += 1
        if numero % 2 == 0:
            soma_pares += numero
            quantidade_pares += 1
print('Quantidade de numeros digitados: ',quantidade)
print('Soma dos Valores Digitados: ', soma)

if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print('Media dos numeros pares Digitados:', media_pares)

else:
    print('nehum numero par foi Digitado')'''

tot_numeros = 0
soma = 0
tot_par = 0
soma_par = 0

while True:
    numero = int(input('Digite os numeros: '))
    if numero == 999: break
    tot_numeros = tot_numeros + 1
    soma = soma + numero
    resto = numero % 2
    
    if resto == 0:
        tot_par = tot_par + 1
        soma_par = soma_par + numero

print('O total de numeros Digitados foi: ',tot_numeros)  
print('A soma dos numeros digitados foi: ',soma)      
media_par = soma_par / tot_par
print('A media dos numeros digitados foi: ',media_par)
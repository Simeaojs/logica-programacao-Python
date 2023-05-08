print()

menor_altura = 999999
soma_altura_m = 0
tot_m = 0

for i in range(4):

    sexo = input('Digite o sexo M ou F: ').upper()
    altura = float(input('Digite a altura: '))
    
    if altura < menor_altura:
        menor_altura = altura
    if sexo == 'm':
        tot_m = tot_m + 1
        soma_altura_m = soma_altura_m + altura

# Apos o laço
print(f'A menor altura foi: {menor_altura:.2f}')
if tot_m != 0:
  media = tot_m / soma_altura_m
  print(f'A media das alturas dos meninos foi: {media:.2f}')
else:
    print('Não foram informados os meninos') 

'''menoraltura = 9999
qtdmeninos = somaalturameninos = 0
for volta in range(4):
    sexo = input('Sexo:')
    altura = float(input('Altura:'))
    if altura < menoraltura : menoraltura = altura

    if sexo == 'm':  # Computa se Menino 
        qtdmeninos = qtdmeninos + 1
        somaalturameninos = somaalturameninos + altura
#Após o laço
print('Menor Altura do grupo:', menoraltura)
if qtdmeninos != 0 :
   media = somaalturameninos / qtdmeninos
   print('A média das alturas dos meninos:',media)
else:
   print('Não foram informados meninos')'''


# Declaraçao de variaveis
maior_altura = 0
soma_altura_mulheres = 0
qtd_mulheres = 0
qtd_homens = 0

while True:
    sexo = input(' Me diga o sexo:')
    if sexo == 'fim': break
    altura = float(input(' Digite a altura: '))
    # Achar a Maior Altura

    if altura > maior_altura: # A)
        maior_altura = altura  
    # Media Altura das Mulheres 

    if sexo == 'f': # B) # FAzer a soma para depois encontrar a media da altura das mulheres.
        qtd_mulheres = qtd_mulheres + 1
        soma_altura_mulheres = soma_altura_mulheres + altura
    # Achar a Quantidade de Homens
        
    else: #C)
        qtd_homens = qtd_homens + 1


print('Maior altura foi: ', altura)
media = soma_altura_mulheres / qtd_mulheres # Media altura das Mulheres , apos feito a soma.
print('Media de altura das mulheres:', media) 
print('Quantidade de Homens foi:', qtd_homens)

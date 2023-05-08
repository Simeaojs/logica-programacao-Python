print()

maior_idade = -1
tot_mulheres = tot_mulheres1835 = 0

while True:
    idade = int(input('Digite a idade ou (-1) para encerar : '))
    if idade == -1 :
        break
    sexo = input('Digite o sexo: ')
    olhos = input('olhos: ')
    
   # Achando a maior idade 
    if idade > maior_idade:
        maior_idade = idade
   # Calulando a porcentagem
    if sexo == 'f':
        tot_mulheres += 1
        if idade >= 18 and idade <= 35 and olhos == 'v':
             tot_mulheres1835 += 1
    # calcaulando o percentual fora do laço 
perc = tot_mulheres1835 * 100 / tot_mulheres 
print('O percentual foi de mulheres entre 18,35 anos com olhos verdes :', perc)

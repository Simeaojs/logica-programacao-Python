print()

qtd_sim = qtd_nao = 0
tot_mulheres = tot_mulheres_sim = 0
tot_homens = tot_homens_nao = 0

while True:
    sexo = input('Sexo M ou F ou FIM para Encerra: ')
    if sexo.lower() == 'fim': break
    print()
    resposta = input('Digite sua resposta SIM ou NAO: ')
    print()

    if resposta == 'sim': 
        qtd_sim = qtd_sim + 1
    else:
        qtd_nao = qtd_nao + 1    
    if sexo == 'f':
        tot_mulheres = tot_mulheres + 1
        if resposta == 'sim':
            tot_mulheres_sim = tot_mulheres_sim + 1
    else:
        tot_homens = tot_homens + 1
        if resposta == 'nao':
            tot_homens_nao = tot_homens_nao + 1

        
tot_resposta = tot_homens + tot_mulheres         
perc_sim = tot_mulheres_sim / tot_mulheres * 100
perc_nao = tot_homens_nao / tot_resposta * 100


print('Quantidade de sim: ',qtd_sim)
print('Quantidade de nao: ',qtd_nao)
print(f'O percentual de sim: {perc_sim:.2%}')
print(f'O percentual de nao: {perc_nao:.2%}')                   
            

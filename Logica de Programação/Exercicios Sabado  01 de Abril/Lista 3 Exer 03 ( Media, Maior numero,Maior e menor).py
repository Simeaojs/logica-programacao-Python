print()

tot_impar = soma_impar = 0 # Achar a media dos impares precisa somar com o total de impares
maior_par = -1  # pra achar o maior sempre inicia com o menor numero -1
maior_geral = -1  # pra acahar o menor sempre inicia com o maior numero 999
menor_geral =  999999  # pra acahar o menor sempre inicia com o maior numero 999

for i in range(5):
    
    num = int(input('Digite os numeros: '))
   
    resto = num % 2 # Se o resto da divisao for 
    if resto != 0: # Diferente de 0 # E impar
      tot_impar += 1 # achando a media dos impares 
      soma_impar += num  
    
    else: # É par
       if num > maior_par: # Achando o maior numero par 
          maior_par = num

    if num > maior_geral: # Achando o maior Geral 
          maior_geral = num

    if num < menor_geral: # o Menor geral ( pra poder fazer a diferença no final)
          menor_geral = num

media = soma_impar / tot_impar # Fora do laço Achando A media dos impares pegando a soma com o total de impares
diferenca = maior_geral - menor_geral # achando a Deferença maior geral - o menor geral

print('A media dos impares foi: ',media)
print('O maior par foi: ',maior_par)    
print(' Maior geral foi: ',maior_geral)  
print(' A diferança do maior pra o menor foi: ',diferenca)        

        


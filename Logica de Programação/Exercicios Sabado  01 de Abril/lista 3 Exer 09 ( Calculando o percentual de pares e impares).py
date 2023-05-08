print()

tot_par = tot_impar = 0

while True:
    valor = float(input('Digite os valores: '))
    if valor == 99:
        break # Comando de parada.
    resto = valor % 2 
    if resto == 0: # Se o Resto da divisão for igual a 0 entao e Par
        tot_par += 1 # Contador, a cada loop incrementa mais 1 na contagem
    else:
        tot_impar += 1 # Senão é Impar.

tot_numeros = tot_par + tot_impar # Criando a variavel (tot_numeros) Fazendo o total de numeros 
perpar = tot_par * 100 / tot_numeros # percentual de par
perimpar = tot_impar * 100 / tot_numeros # percentual de impar 

print('O percentual de numeros par foi:', perpar)
print('O percentual de numeros impares foi:', perimpar)

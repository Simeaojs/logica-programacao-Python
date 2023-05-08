print()

nome = input('Digite um nome com mais de 10 caracteres: ')

tam = len(nome) # Contando os Caracteres.

metade = tam//2 # Dividindo a Frase em Duas partes.

p1 = nome[0:metade] # Parte 1 do Inicio Ate a metade.


p2 = nome[metade:] # Parte 2 da Metade até o fim.

senha = p2[0:2] + '%%' + p1[-3:] # Concatenado (+) As dois Primeiros Caracteres da parte 2 ,( %% ) com  as Três Ultimas da primeira parte.

print(' Parte 1:',p1)
print(' Parte 2:',p2)
print(' Senha:',senha)

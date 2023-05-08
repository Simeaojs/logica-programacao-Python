'''print()

nome = input('Digite um nome com mais de 10 caracteres: ')

tam = len(nome)  # Contando os Caracteres.

metade = tam//2  # Dividindo a Frase em Duas partes.

p1 = nome[0:metade]  # Parte 1 do Inicio Ate a metade.


p2 = nome[metade:]  # Parte 2 da Metade até o fim.

# Concatenado (++) As dois Primeiros Caracteres da parte 2 ,( %% ) com  as Três Ultimas da primeira parte.
senha = p2[0:2] + '%%' + p1[-3:]

print(' Parte 1:', p1)
print(' Parte 2:', p2)
print(' Senha:', senha)'''

'''Usando o While True:'''

while True:
    nome = input('Digite seu nome Para criar senha ou FIM para Encerra : ')

    aux = nome.upper() # Usando o metodo (.upper()) para retornar o nome maiusculo 
    if aux == 'FIM': break

    nome = nome.replace(' ','@') # Usando o Metodo (.replace('_','*')) Para subistituir no texto o primeiro caractere pelo segundo.

    tam = len(nome) # Contando o Tamando do Texto

    if tam > 10:
        metade = tam//2
        p1 = nome[0:metade]
        p2 = nome[metade:]
        senha = p2[0:2]+'%%'+p1[-3:]
        print(' A senha Sera :',senha)
    else:
        print('Digite Um nome com mais de 10 Caracteres: ')
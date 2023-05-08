print()

nome = input('Digite um nome com mais de 10 caracteres: ')
tam = len(nome)
metade = tam//2
p1 = nome[0:metade]
p2 = nome[metade:]
senha = p2[0:2] + '%%' + p1[-3:]

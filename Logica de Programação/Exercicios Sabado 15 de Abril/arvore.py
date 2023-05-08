print()

nome = input('nome:')
tam = len(nome)
seq = ''
for p in range(tam):
    seq = seq + nome[p]
    print(''*(tam-(p+1))+seq[::-1][:-1]+seq)

'''nome = input('Nome:')
tam = len(nome)
seq = ''
for p in range(tam):
    seq = seq + nome[p]
    print(' '*(tam-(p+1))+seq[::-1][:-1]+seq)'''

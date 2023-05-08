print()

mi = float(input(' Massa inicial: '))
mf = mi
tempo = 0
while mf > 0.5:
    mf = mf/2
    tempo = tempo + 50
print('Massa inicia:', mi, ' \nMassa final:', mf, ' \nTempo:', tempo)

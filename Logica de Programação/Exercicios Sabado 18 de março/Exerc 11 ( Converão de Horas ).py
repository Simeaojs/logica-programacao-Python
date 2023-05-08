

print()

duracao_segundos = int(input(' Quanto tempo durou o evento? em segundos:'))

# Na segunda linha, calculamos a quantidade de horas utilizando a divisão inteira por 3600
# (que representa o número de segundos em uma hora.
horas = duracao_segundos // 3600

# Na terceira linha, calculamos a quantidade de minutos utilizando o resto da divisão por 3600 dividido por 60
# que representa o número de segundos em um minuto
minutos = (duracao_segundos % 3600) // 60

# Na quarta linha, calculamos a quantidade de segundos utilizando o resto da divisão por 60.
segundos = duracao_segundos % 60

print()

print(f'{horas}h {minutos}mim {segundos}s')

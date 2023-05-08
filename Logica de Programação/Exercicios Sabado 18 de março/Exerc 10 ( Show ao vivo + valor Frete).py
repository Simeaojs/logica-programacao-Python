print()

vlr_hora = float(input('Digite o valor da hora a Ser cobrado: '))
distancia = float(input('Digite a Distancia em Km: '))
duracao = float(input('Imforme a Duração do Show: '))

deslocamento = distancia * 50
vlr_show = (vlr_hora * duracao) + deslocamento
frete = deslocamento * 0.35
print()
print(f'O valor do show foi de:R$ {vlr_show}')
print(f'Valor do Frete para o Transportador foi de:R$ {frete}')

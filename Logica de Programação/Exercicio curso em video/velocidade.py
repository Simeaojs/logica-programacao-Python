
velocidade=float(input(' velocidade KM/h:'))
limite=80
multa=7
if velocidade>limite:
    acima_do_limite=velocidade-limite
    multa=acima_do_limite*multa
    print(' multa por excesso',multa)
else:
    print(' Velocidade normal')

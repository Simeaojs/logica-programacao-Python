
'''velocidade = float(input(' velocidade KM/h:'))
limite = 80
multa = 7
if velocidade > limite:
    acima_do_limite = velocidade - limite
    multa = acima_do_limite * multa
    print(f' multa por excesso de velocidade: R${multa}')
else:
    print(' Velocidade normal')'''

velocidade = float(input(' Velocidade KM/H:'))
limite = 80 
multa = 10 
if velocidade > limite:

    acima_do_limite  = velocidade - limite
    multa = acima_do_limite * multa

    print(f' Multa por excesso de velocidade: R${multa}')

else:
    print('Não ultrapassou o limite de velocidade')    

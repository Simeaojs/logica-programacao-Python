

dist_viagem=float(input(' Distancia da viagem KM:'))
preco_passagem = dist_viagem*0.50
if dist_viagem<200:
    print(' o preço da passagem foi',preco_passagem)
else:
    preco_passagem_menor=dist_viagem*0.45
    print('preco menor',preco_passagem_menor)

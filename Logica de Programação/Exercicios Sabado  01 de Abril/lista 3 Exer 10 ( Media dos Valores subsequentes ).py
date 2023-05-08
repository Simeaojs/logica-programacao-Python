print()


'''while True:
    numero = int(input(' Valores: '))
    if numero == 0:
        break
    valor = numero + 1
    soma = 0
    for i in range(10):
        soma = soma + valor
        valor += 1
    print('A soma é:', soma)'''

while True:
    n = int(input('Número:'))
    if n == 0 : break
    v = n + 1
    soma = 0
    for i in range(10):
        soma = soma + v
        v = v + 1
    print('Soma:', soma)

'''soma_total = 0
contador = 0

while True:
    valor = int(input("Digite um valor (0 para sair): "))
    
    if valor == 0:
        break
    
    soma_parcial = 0
    
    for i in range(10):
        valor_subsequente = int(input(f"Digite o {i+1}º valor subsequente: "))
        soma_parcial += valor_subsequente
        
    soma_total += soma_parcial
    contador += 10
    
    media = soma_parcial / 10
    
    print(f"Soma parcial: {soma_parcial}")
    print(f"Média parcial: {media}")
    
media_total = soma_total / contador
print(f"Soma total: {soma_total}")
print(f"Média total: {media_total}")'''


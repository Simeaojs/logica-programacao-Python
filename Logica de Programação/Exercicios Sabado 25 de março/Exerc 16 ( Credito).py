# entrada

# saldo medio

# processamento


# saida
# credito disponivel

print()

saldo_me = float(input("Saldo Médio: "))

if saldo_me <= 500:
    perc = 0
if saldo_me > 501 and saldo_me <= 1000:
    perc = 30
if saldo_me > 1001 and saldo_me <= 3000:
    perc = 40
if saldo_me > 3001:
    perc = 50

credito = saldo_me * perc / 100

print(f"Valor do Credito:R$ {credito}")

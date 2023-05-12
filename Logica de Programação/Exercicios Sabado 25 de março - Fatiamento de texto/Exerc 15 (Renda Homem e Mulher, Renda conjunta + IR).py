
rh = float(input(" Renda do homem:"))
rm = float(input(" Renda da Mulher:"))
rc = rh + rm

if rc <= 900:
    perc = 0
if rc > 900 and rc <= 1500:
    perc = 10
if rc > 1500 and rc <= 2500:
    perc = 15
if rc > 2500:
    perc = 25

ir = rc * perc / 100
rl = rc - ir

print(f'\nRenda Conjunta:R$ {rc} \nPercentual Ir:{perc}% \nValor IR:R$ {ir} \nRenda Liquida:R$ {rl}')

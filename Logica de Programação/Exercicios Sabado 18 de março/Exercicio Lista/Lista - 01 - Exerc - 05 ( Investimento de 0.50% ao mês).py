print(" Taxa de juros a 0,50% a.m:")

valor_deposito = float(input(" Quanto vc quer investir:"))

juros_fixo = valor_deposito * 0.005

rendimento_mes = juros_fixo + valor_deposito


print(f" \nRendimento mensal estimado: {rendimento_mes:.2f}R$")

# IF SIMPLES

salarioatual = float(input(" Salario Atual "))

if salarioatual < 1100:
    aumento = (salarioatual * 10 / 100) + salarioatual

if salarioatual >= 1101 and salarioatual <= 2000:
    aumento = (salarioatual * 7) / 100 + salarioatual


if salarioatual > 2001:
    aumento = (salarioatual * 5) / 100 + salarioatual

print(" seu novo salario sera", aumento)

# IF COMPOSTO

if salarioatual < 1100:
    aumento = (salarioatual * 10 / 100) + salarioatual

else:
    if salarioatual < 2000:
        aumento = (salarioatual * 7 / 100) + salarioatual

    else:
        aumento = (salarioatual * 5 / 100) + salarioatual

print(" seu novo salario sera", aumento)


# COM ELIF


if salarioatual < 1100:
    aumento = salarioatual + (salarioatual * 10 / 100)  # salario * 1.1

elif salarioatual < 2000:
    aumento = salarioatual + (salarioatual * 7 / 100)  # salario * 1.07

else:
    aumento = salarioatual + (salarioatual * 5 / 100)  # salario * 1.05


print(" seu novo salario sera", aumento)

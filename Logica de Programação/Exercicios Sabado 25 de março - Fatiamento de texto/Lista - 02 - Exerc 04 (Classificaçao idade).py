# IF Simples

print()

idade = int(input(" Digite sua idade: "))

if idade >= 21:
    classi = "Maior de idade"
if idade < 21:
    classi = "Menor de idade"
if idade >= 65:
    classi = "Pessoa idosa"
print()

print("Sua classificacao e:", classi)

# IF Composto

idade = int(input("Idade:"))
if idade >= 21 and idade < 65:
    classif = "Maior Idade"
else:
    if idade < 21:
        classif = "Menor Idade"
    else:
        classif = "Pessoa Idosa"

print("Classificação:", classif)

# ELIF

print()
idade = int(input("Digite sua idade: "))
if idade >= 21 and idade < 65:
    classi = "Maior de idade"
elif idade < 21:
    classi = "Menor de idade"
else:
    classi = "Pessoa idosa"
print("Sua classificacao e:", classi)

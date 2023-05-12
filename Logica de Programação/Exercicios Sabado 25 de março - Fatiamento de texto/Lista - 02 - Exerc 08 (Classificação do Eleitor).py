# If simples

print()

idade = int(input("Qual sua idade: "))
if idade <= 16:
    sit = " Nao eleitor"
if idade >= 18 and idade < 65:
    sit = "Eleitor obrigatorio"
if idade > 16 and idade < 18 or idade > 65:
    sit = "Eleitor facultativo"

print("Sua situacao e:", sit)

# if composto

idade = int(input("Digite a idade da pessoa: "))

if idade < 16:
    print("Não eleitor")
else:
    if idade < 18 or idade >= 65:
        print("Eleitor facultativo")
    else:
        print("Eleitor obrigatório")

# ELIF

idade = int(input("Digite a idade da pessoa: "))

if idade < 16:
    print("Não eleitor")
elif idade >= 18 and idade < 65:
    print("Eleitor obrigatório")
else:
    print("Eleitor facultativo")

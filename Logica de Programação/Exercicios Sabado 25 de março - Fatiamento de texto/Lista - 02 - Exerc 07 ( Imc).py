# if simples

print()

peso = float(input("Digite seu peso"))
altura = float(input("Digite sua altura"))

imc = peso / (altura**2)
if imc < 20:
    sit = "Abaixo do peso"
if imc >= 20 and peso <= 25:
    sit = "Peso normal"
if imc > 25 and peso <= 30:
    sit = "Sobre peso"
if imc > 30 and peso <= 40:
    sit = "Obeso"
if imc > 40:
    sit = "Obeso Morbido"


# if  composto

if imc < 20:
    sit = "Abaixo do peso"
else:
    if imc < 25:
        sit = "Peso normal"
    else:
        if imc < 30:
            sit = "Sobre peso"
        else:
            if imc < 40:
                sit = "Obeso"
            else:
                sit = "Obeso Morbido"

            # ELIF

if imc < 20:
    sit = "Abaixo do peso"
elif imc < 25:
    sit = "Peso normal"
elif imc < 30:
    sit = "Sobre peso"
elif imc < 40:
    sit = "Obeso"
else:
    sit = "Obeso Morbido"

print("\nSua situacao e", sit)

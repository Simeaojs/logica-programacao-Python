from num2words import num2words

n = int(input("Digite um número: "))

extenso = num2words(n, lang="pt-br", to="ordinal")

if n == 1:
    extenso = " Um "
elif n == 2:
    extenso = " Dois"
elif n == 3:
    extenso = " Tres"
elif n == 4:
    extenso = " Quatro"
elif n == 5:
    extenso = " Cinco"
elif n == 6:
    extenso = " Seis"
elif n == 7:
    extenso = " Sete"
elif n == 8:
    extenso = " Oito"
elif n == 9:
    extenso = " Nove"
elif n == 10:
    extenso = " Dez"
else:
    extenso = " Numero invalido"

print(extenso)

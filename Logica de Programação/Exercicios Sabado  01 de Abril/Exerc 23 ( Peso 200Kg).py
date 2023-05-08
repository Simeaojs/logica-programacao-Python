# Loop While
print()
menor_peso = 0

while True:
    peso = float(input('Digite um peso em Kg: '))
    if peso > 200:
        print('Peso superio a 200Kg:')
        break
    if peso < 200:
        menor_peso = peso
print('Menor peso foi', menor_peso)

#Loop For
'''print()
menor_peso = float('inf')

for i in range (1,1000000):
    peso = float(input('Digite um peso em Kg: ')) 
    if peso > 200:
        print('Peso Superior a 200Kg:')  
        break   
    if peso < 200:
        menor_peso = peso
print('O menor peso foi',menor_peso,'Kg')'''    



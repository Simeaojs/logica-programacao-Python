
'''salario_atual=float(input(' Digite seu salario atual:'))
if salario_atual > 1250:
    novo_salario=salario_atual+(salario_atual*0.10)
    
    
if salario_atual<=1249:
    novo_salario=salario_atual+(salario_atual*0.15)

print(' Salario novo',novo_salario)'''

salario = float(input(' Digite seu salario atual:'))

if salario > 1250:
    novo_salario = salario + (salario * 0.10)

if salario <= 1249:
    novo_salario = salario + (salario * 0.15)

print(f' Salario novo: R${novo_salario}')    

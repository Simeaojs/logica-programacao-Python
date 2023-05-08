print()

Sal_bruto = float(input('Qual foi seu Salario Bruto: '))

vlr_ir = (Sal_bruto * 0.05)
vlr_inss = (Sal_bruto * 0.11)
sal_liquido = Sal_bruto - (vlr_ir + vlr_inss)

print(f'\nO valor do Imposto de Renda é :R$:{vlr_ir} \nO valor do INSS é:R$: {vlr_inss} \nO Salario Liquido foi:R$ :{sal_liquido}')

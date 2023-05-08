print()

vlr_sal_minimo = float(input('Digite o Valor do Salario minimo: '))
qtd_Kw_consumo= float(input('Quandidade de Kw Consumido pela Resedencia: '))


vlr_kw_milesimo = vlr_sal_minimo / 1000

vlr_conta = vlr_kw_milesimo * qtd_Kw_consumo

vlr_desc = vlr_conta - ((vlr_conta * 15)/100)


print(f'O valor em Reais de cada Kw:{vlr_kw_milesimo}')
print(f'O Valor da conta foi:R${vlr_conta:.2f}')
print(f'O Valor com Desconto de 15% Será de:R${vlr_desc:.2f}')


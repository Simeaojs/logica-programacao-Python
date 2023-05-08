
qtd_apart = int(input('Digite A Quantidade de Apartamentos '))
vlr_agua = float(input('Digite o Valor da Água: '))
vlr_enrgia = float(input('Digite o Valor da Enegia: '))

rateio = (vlr_agua + vlr_enrgia) / qtd_apart

print(f'O Valor que cada Apartamento deve pagar é: R${rateio:.2f}')

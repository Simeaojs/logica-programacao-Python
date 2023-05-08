print()

qtd_h_trabalhadas = float(
    input('Digite A Quantidade de Horas trabalha por mês: '))
vlr_hora = float(input('Digite o Valor Da hora Trabalhada: '))

vlr_receber = qtd_h_trabalhadas*vlr_hora

print(f'O Valor Que o Professor ira Receber por mês e R$:{vlr_receber}')

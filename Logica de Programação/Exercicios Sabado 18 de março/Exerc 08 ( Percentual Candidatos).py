print()

tot_homens = int(input('Digite o total de homens: '))
tot_Mulheres = int(input('Digite o total de Mulheres: '))
tot_Ausentes = int(input('O Total de Ausentes: '))

tot_candidatos = tot_homens + tot_Mulheres + tot_Ausentes
p1 = (tot_homens * 100) / tot_candidatos

tot_presentes = tot_homens + tot_Mulheres
p2 = (tot_Ausentes * 100) / tot_presentes



print(f'O Percentual dos Homens em Relação ao total de inscritos: {p1:.2f}%')
print(f'O Percebtual de Ausentes em Relação ao total de Presentes: {p2:.2f}%')

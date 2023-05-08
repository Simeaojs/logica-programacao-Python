# Contadores e Acumuladores

# Loop For
'''total_gols = 0
for i in range(3):
    gols = int(input(f'Quantos gols foram marcados no {i+1} jogo?'))
    total_gols += gols
print(f'O total de gols marcados no Campeonato foi {total_gols}.')'''

# Loop While
total_gols=0
jogos=1
while(jogos <= 3):
    gols = int(input(f'Quantos gols foram marcados no {jogos} jogo?'))
    total_gols += gols
    jogos += 1
print(f'O total de gols marcados no Campeonato foi {total_gols}.')    

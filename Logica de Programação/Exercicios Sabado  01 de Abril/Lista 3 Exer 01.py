print()

soma = 0 # Pra poder tirar a media precissa declarar a variavel soma

print('Digite 5 idades para saber a média entre elas!')
for i in range (0,5,1):
    print()
    idade = int(input('Digite uma idade: '))
    soma += idade
media = soma / 5 # Media sempre fora do laço 
print('A média das idade digitadas foi:', media)    






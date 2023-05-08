import random

jogadas = ["pedra", "papel", "tesoura"]

print("Vamos jogar Jokenpo!")
print("Escolha sua jogada:")
print("1 - pedra")
print("2 - papel")
print("3 - tesoura")

jogada_jogador = int(input("Digite o número da sua jogada: "))
jogada_jogador -= 1

jogada_computador = random.randint(0, 2)

print("Você escolheu:", jogadas[jogada_jogador])
print("O computador escolheu:", jogadas [jogada_computador])

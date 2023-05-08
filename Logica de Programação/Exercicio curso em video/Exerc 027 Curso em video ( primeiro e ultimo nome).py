
# Usando o Strip() para eliminar os espaços
n = input('Digite o nome: ').strip().upper()
nome = n.split() # usando o split para contar a quantidade de palavras separando-a por (","",")
print(' Seu primeiro nome é: ',nome[0])
print(' Seu ultimo nome é:',(nome[len(nome)-1])) # Pegou o nome usou o len() para contar a quantidade de nomes e depois usou [-1] para começar a contagem do final


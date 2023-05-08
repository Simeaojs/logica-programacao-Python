
# Receba do teclado 5 notas de alunos e calcular a media aritmetica

soma = 0
n = 1
while (n <= 5):
    nota = float(input(' Informe a '+str(n)+'a.nota:'))  #A função converte o especificado em uma cadeia de caracteres.+str()+
    soma += nota
    n += 1
    media = soma/5
    
print(' A media calculada foi:', media)

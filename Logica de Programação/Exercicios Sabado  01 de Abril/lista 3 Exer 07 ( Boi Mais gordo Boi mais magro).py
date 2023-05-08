print()

mais_gordo = -1
mais_magro = 999999

for i in range(8):
    
    ident = int(input(' Digite a Identificação do boi: '))
    peso = float(input('Digite o peso do boi(Kg): '))
    # achar o boi mais gordo
    if peso > mais_gordo:
        mais_gordo = peso
        # Criar uma variavel para receber a identificação se vai ser gordo ou magro.
        registrogordo = ident
    # achar o boi mais magro
    if peso < mais_magro:
        mais_magro = peso
        # Criar uma variavel para receber a identificação se vai ser gordo ou magro.
        registromagro = ident

print('O boi mais gordo Registro:', registrogordo,
      'Tem o peso de:', mais_gordo, 'Kg')
print('O boi mais magro Registro:', registromagro,
      'Tem o peso de:', mais_magro, 'Kg')

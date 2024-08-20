# Dada uma lista de nomes, crie uma nova lista apenas com os nomes que começam com a letra "A".

lista_nomes = ['David', 'Atena', 'Marcos', 'Alex', 'Joana', 'Alexandre']

lista_nova_A = [nome for nome in lista_nomes if nome.lower()[0] == 'a']

print(lista_nova_A)

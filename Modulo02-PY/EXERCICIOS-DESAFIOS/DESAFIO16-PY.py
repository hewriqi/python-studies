# Escreva um programa que compare duas listas. Considere a primeira lista como a versão inicial e a segunda como a versão após alterações. Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações entre essas duas versões, listando:
# - os elementos que não mudaram
# - os novos elementos
# - os elementos que foram removidos

lista_antes = [1, 2, 3, 4, 5]
lista_depois = [3, 4, 6, 3, 2, 1]

conjunto_antes = set(lista_antes)
conjunto_depois = set(lista_depois)

print(f'Os valores que não mudaram foram: ', conjunto_antes & conjunto_depois)

print('Os novos valores são: ', conjunto_depois - conjunto_antes)

print(f'Os valores que foram removidos são: ',
      conjunto_antes - conjunto_depois)

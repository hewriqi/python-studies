# Dada uma lista de números, crie uma nova lista apenas com os números maiores que 5.
numeros = [1, 2, 6, 8, 100, 2, 3, 4, 5, 7, 10]

nova_lista_numeros = [numero for numero in numeros if numero > 5]

print(nova_lista_numeros)

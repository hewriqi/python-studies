# Dada uma lista de números, crie uma nova lista com o dobro de cada número, mas apenas se o número for ímpar
numeros = [1, 2, 5, 7, 0, 23, 123, 44, 2, 5, 7]

nova_lista_dobro_impar = [numero * 2 for numero in numeros if numero % 2 != 0]

print(nova_lista_dobro_impar)

# Dada uma lista de números, crie uma nova lista contendo apenas os números pares e maiores que 10.
lista_numeros = [1, 2, 7, 2, 43, 24, 2, 56, 3, 14, 1, 33, 42, 14, 6, 2, 1]

lista_nova_pares_maior10 = [
    numero for numero in lista_numeros if numero > 10 and numero % 2 == 0]

print(lista_nova_pares_maior10)

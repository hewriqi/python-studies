# List comprehension em Python
# É uma forma mais rápida de criar
# listas a partir de iteráveis.

# print(list(range(10)))
lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

# ----- como fazer essas 4 linhas de código acima usando list comprehension -----

lista = [
    numero * 2
    for numero in range(10)
]  # colocar à esquerda do for aquilo que eu quero incluir na lista.
print(list(range(10)))
print(lista)

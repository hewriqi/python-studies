"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +

append = adiciona valores ao final da lista
pop = remove o ultimo valor/elemento da lista
del = apagar um índice da lista
insert = insere um valor em um indice que vc queira
clear = limpa a lista

Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

lista = [10, 20, 30, 40]
lista.append('Henrique')
nome = lista.pop()
lista.append(1337)
del lista[-1]
# lista.clear()
lista.insert(0, 5)
print(lista[4])

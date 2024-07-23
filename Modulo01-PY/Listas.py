"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, etc
"""
#        +01234
string = 'ABCDE'  # 5 caracteres (len)
#        -54321
# print(bool([]))  # falsy
# print(lista, type(lista))

#         0     1         2          3    4   # POSIÇÕES DENTRO DA LISTA
#        -5    -4        -3         -2   -1   # POSIÇÕES DENTRO DA LISTA
lista = [123, True, 'Luiz Otávio',  1.2, []]
lista[-3] = 'Maria'  # AQUI EU MUDEI O 'LUIZ OTÁVIO' PARA MARIA
print(lista)  # PRINTEI A LISTA INTEIRA
# PRINTEI O INDICE 2 DA LISTA (MARIA, PORQUE MUDEI DE LUIZ OTÁVIO) E O TIPO DESSE INDICE 2, QUE NO CASO É UMA STRING.
print(lista[2], type(lista[2]))

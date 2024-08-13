# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy
pessoa = {
    'nome': 'Henrique',
    'sobrenome': 'Junior',
    # 'idade': 18,
}
pessoa.setdefault('idade', 18)

print(f'Número de chaves: {len(pessoa)}')

print(list(pessoa.keys()))

print(list(pessoa.values()))

for valores in pessoa.values():
    print(valores, end=' ')


print(list(pessoa.items()))

for chave, valor in pessoa.items():
    print(chave, valor)

print(pessoa['idade'])

# shallow copy vs deepcopy
d1 = {
    'pessoa': 'Henrique',
    'sobrenome': 'Junior',
    'l1': [1, 2, 3]
}
d2 = d1.copy()
print(d2)
d2 = copy.deepcopy(d1)
d2['pessoa'] = 'AAAAA'
d2['l1'][1] = 999

print(d1)
print(d2)

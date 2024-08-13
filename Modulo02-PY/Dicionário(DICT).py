"""
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo
par de "chave" e "valor".
Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
O valor pode ser de qualquer tipo, incluindo outro
dicionário.
Usamos as chaves - {} - ou a classe dict para criar
dicionários.
Imutáveis: str, int, float, bool, tuple
Mutável: dict, list
"""
pessoa = {
    'nome': 'Henrique',
    'sobrenome': 'Junior',
    'idade': 18,
    'altura': 1.65,
    'endereços': [
        {'rua': 'tal rua', 'número': 123},
        {'rua': 'tal rua', 'número': 456},
    ],
}
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

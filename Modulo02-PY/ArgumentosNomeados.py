"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento(valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} z={z}', '|', 'x + y + z =  ', x + y + z)


soma(4, 5, 3)
soma(y=2, z=3, x=1)
print(1, 2, 3, sep='-')

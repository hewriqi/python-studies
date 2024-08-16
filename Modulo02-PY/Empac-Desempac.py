# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# ------------ PODE FAZER DESSA FORMA ------------
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# print(a1)

# for chave, valor in pessoa.items():
#     print(chave, valor)
# ------- OU DESSA --------
pessoa = {
    'nome': 'Henrique',
    'sobrenome': 'Junior',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.65,
}

pessoa_dados_completo = {**pessoa, **dados_pessoa}
pessoa_dados_completo.update({'sexo': 'Masculino'})
for chave, valor in pessoa_dados_completo.items():
    print(chave, valor)

# args e kwargs
# kwargs ( keyword arguments - argumentos nomeados )

print('-' * 35)


def mostra_argumentos_nomeados(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)


# mostra_argumentos_nomeados(1, 2, nome='Joana', qlq=123)
mostra_argumentos_nomeados(**pessoa_dados_completo)

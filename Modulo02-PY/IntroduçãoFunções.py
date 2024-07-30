"""
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, as funções Python retornam None (NADA).
"""


def imprimir(a, b, c):
    soma = a + b + c
    print(a, b, c)
    print(soma)


imprimir(4, 5, 6)


def linhaSep():
    print('-' * 30)


linhaSep()


def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}!')


saudacao('Henrique')


def mensagem(msg):
    print('-' * 25)
    print(msg)
    print('-' * 25)


mensagem('SISTEMA DE ALUNOS')

# PRÁTICA


def soma(a, b):
    s = a + b
    print(f'{a} + {b} = {s}')


soma(4, 5)
soma(2, 1)
soma(8, 9)

# a = 4
# b = 5
# s = a + b
# print(s)

# a = 2
# b = 1
# s = a + b
# print(s)

# a = 8
# b = 9
# s = a + b
# print(s)

linhaSep()


def contadores(*num):
    for valor in num:
        print(f'{valor}', end=' ')
    print('FIM')


contadores(2, 1, 7)
contadores(8, 0)
contadores(4, 4, 7, 6, 2)

linhaSep()


def contador(*num):
    tamanho = len(num)
    print(f'Recebi:{num} // São ao todo {tamanho} números. ')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

linhaSep()


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

"""
Faça um programa que tenha uma função chamada 
contador(), que receba três parâmetros: início, fim 
e passo. Seu programa tem que realizar três contagens 
através da função criada: 

de 1 até 10, de 1 em 1; 
de 10 até 0, de 2 em 2.
"""


def mostrarlinha():
    print('=' * 30)


def contador(i, f, p):
    if p == 0:
        print('O passo não pode ser 0')
        return
    if i < f:
        for i in range(i, f + 1, p):
            print(i, end=' ')
    else:
        for i in range(i, f - 1, - p):
            print(i, end=' ')


print("Contagem de 1 até 10, de 1 em 1:")
contador(1, 10, 1)

print("\nContagem de 10 até 0, de 2 em 2:")
contador(10, 0, 3)

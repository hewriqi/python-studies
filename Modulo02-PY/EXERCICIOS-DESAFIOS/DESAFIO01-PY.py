"""
Faça um programa que tenha uma função chamda "área()", que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno.

Write a program that has a function called "area()", which receives the dimensions of a
rectangular plot (width and length) and show the area of the plot.
"""


def area(l, c):
    calculo = l * c
    print(f'A área de um terreno {l} x {c} = {calculo}m²')


print('PROGRAMA DE CONTROLE DE TERRENOS: ')

print('\n\nControle de Terrenos')
print('-' * 25)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)
print('-' * 25)

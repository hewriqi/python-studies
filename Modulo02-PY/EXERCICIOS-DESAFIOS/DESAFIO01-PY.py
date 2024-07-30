"""
Faça um programa que tenha uma função chamda "área()", que receba as dimensões de um
terreno retangular (largura e comprimento) e mostre a área do terreno.

Write a program that has a function called "area()", which receives the dimensions of a
rectangular plot (width and length) and show the area of the plot.
"""


def area(largura, comprimento):
    calculo = largura * comprimento
    print(f'A área de um terreno {largura} x {comprimento} = {calculo}m²')


print('CONTROLE DE TERRENOS')
print('-' * 25)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area(largura, comprimento)

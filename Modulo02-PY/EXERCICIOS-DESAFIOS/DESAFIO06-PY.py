"""
Faça um programa, com uma função que 
necessite de um argumento. A função retorna 
o valor de caractere 'P', se seu argumento 
for positivo, e 'N', se seu argumento for 
zero ou negativo.
"""


def verificar_argumento(n):
    if n > 0:
        return 'P'
    else:
        return 'N'


try:
    numero = float(input("Digite um número: "))
    resultado = verificar_argumento(numero)
    print(f'O resultado é [ {resultado} ]')
except ValueError:
    print('Por favor, insira um número válido.')

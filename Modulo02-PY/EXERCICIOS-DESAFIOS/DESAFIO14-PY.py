"""
Escreva uma função que, dado o valor da conta de um restaurante, calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.
"""


def gorjeta(valor_conta):
    calculo_gorjeta = (valor_conta * 10) / 100
    print(f'A conta de R${valor_conta}, o valor da gorjeta para o garçom é de R${
          calculo_gorjeta}')
    return calculo_gorjeta


gorjeta(777)

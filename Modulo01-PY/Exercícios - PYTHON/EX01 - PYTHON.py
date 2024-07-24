# EXERCICIO - MENU DE OPÇÕES

from time import sleep
from math import trunc
num1 = float(input("Digite um número: "))  # PEÇO O 1o NÚMERO AO USUÁRIO
num2 = float(input("Digite um número: "))  # PEÇO O 2o NÚMERO AO USUÁRIO
pergunta = 0
# ENQUANTO A RESPOSTA DESSA PERGUNTA ABAIXO FOR DIFERENTE DE 5 (5 = SAIR DO PROGRAMA) EU VOU CONTINUAR MOSTRANDO AO USUARIO O MENU DE OPÇÕES
while pergunta != 5:
    pergunta = str(input("""\nQual operação vc deseja fazer?
[1] SOMA
[2] MULTIPLICAR
[3] MOSTRAR MAIOR
[4] QUERO DIGITAR NOVOS NÚMEROS
[5] SAIR DO PROGRAMA

>>>>>>>>>     """)).strip().upper()

    if pergunta == '1':  # SE A RESPOSTA FOR 1, FAÇO A SOMA
        soma = num1 + num2
        print('=='*10)
        print(f'\nO resultado da SOMA foi de: [ {trunc(soma)} ]')
        print('=='*10)
        continue
    elif pergunta == '2':  # SE A RESPOSTA FOR 2, FAÇO A MULTIPLICAÇÃO
        mult = num1 * num2
        print('=='*10)
        print(f'\nO resultado da MULTIPLICAÇÃO foi: [ {mult} ]')
        print('=='*10)
        continue
    elif pergunta == '3':  # SE A RESPOSTA FOR 3, MOSTRO O MAIOR NÚMERO
        if num1 > num2:
            print('=='*10)
            print(f'O número {num1} é MAIOR!')
            print('=='*10)
            continue
        elif num2 > num1:  # SE A RESPOSTA FOR 3, MOSTRO O MAIOR NÚMERO
            print('=='*10)
            print(f'O número {num2} é MAIOR')
            print('=='*10)
            continue
        else:  # SE NEM UM NEM OUTRO É MAIOR, ENTÃO OS DOIS SÃO IGUAIS
            print('=='*10)
            print(f'O número {num1} e o {num2} são IGUAIS!')
            print('=='*10)
            continue
    elif pergunta == '4':  # SE A RESPOSTA FOR 4, O USUÁRIO PODERÁ DIGITAR NOVOS NÚMEROS
        print('=='*10)
        print('\nCONTINUANDO O PROGRAMA...')
        sleep(1.9)
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite um número: "))
        continue
    elif pergunta == '5':  # SE A RESPOSTA FOR 5, O USUÁRIO VAI FINALIZAR O PROGRAMA
        print('=='*10)
        print('SAINDO...')
        sleep(2.15)
        break
    else:
        print('Opção inválida, tente novamente...')
        continue
print('=='*10)
print('\nFIM DO PROGRAMA.\nVOLTE SEMPRE!')

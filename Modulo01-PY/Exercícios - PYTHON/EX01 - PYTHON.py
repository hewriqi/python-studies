from time import sleep
from math import trunc
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
pergunta = 0
while pergunta != 5:
    pergunta = str(input("""\nQual operação vc deseja fazer?
[1] SOMA
[2] MULTIPLICAR
[3] MOSTRAR MAIOR
[4] QUERO DIGITAR NOVOS NÚMEROS
[5] SAIR DO PROGRAMA

>>>>>>>>>     """)).strip().upper()

    if pergunta == '1':
        soma = num1 + num2
        print('=='*10)
        print(f'\nO resultado da SOMA foi de: [ {trunc(soma)} ]')
        print('=='*10)
        continue
    elif pergunta == '2':
        mult = num1 * num2
        print('=='*10)
        print(f'\nO resultado da MULTIPLICAÇÃO foi de: [ {mult} ]')
        print('=='*10)
        continue
    elif pergunta == '3':
        if num1 > num2:
            print('=='*10)
            print(f'O número {num1} é MAIOR!')
            print('=='*10)
            continue
        elif num2 > num1:
            print('=='*10)
            print(f'O número {num2} é MAIOR')
            print('=='*10)
            continue
        else:
            print('=='*10)
            print(f'O número {num1} e o {num2} são IGUAIS!')
            print('=='*10)
            continue
    elif pergunta == '4':
        print('=='*10)
        print('\nCONTINUANDO O PROGRAMA...')
        sleep(1.9)
        num1 = float(input("Digite um número: "))
        num2 = float(input("Digite um número: "))
        continue
    elif pergunta == '5':
        print('=='*10)
        print('SAINDO...')
        sleep(2.15)
        break
    else:
        print('Opção inválida, tente novamente...')
        continue
print('=='*10)
print('\nFIM DO PROGRAMA.\nVOLTE SEMPRE!')

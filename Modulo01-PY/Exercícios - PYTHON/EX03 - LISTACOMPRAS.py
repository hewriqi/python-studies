"""
Faça uma lista de compras com LISTAS.
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de 
índices inexistentes na lista.
"""
import os
from time import sleep
lista_de_compras = []
while True:
    pergunta_usuario = input(
        "Selecione sua opção\n[i]nserir | [a]pagar | [l]istar:  ")

    if pergunta_usuario == 'i':
        os.system('cls')
        pergunta_inserir = str(
            input("Qual produto você deseja adicionar à lista?: "))
        lista_de_compras.append(pergunta_inserir)
    elif pergunta_usuario == 'a':
        if pergunta_usuario == 'a' and len(lista_de_compras) == 0:
            print('Nada para apagar, tente novamente.')
            sleep(1.5)
        indice_apagar = int(input("Escolha o indice para apagar:  "))
        try:
            del lista_de_compras[indice_apagar]
        except ValueError:
            print('Por favor digite um número inteiro.')
        except IndexError:
            print("Não existe esse índice na lista.")
    elif pergunta_usuario == 'l':
        os.system('cls')
        if len(lista_de_compras) == 0:
            print('Nada para listar, tente novamente.')
            sleep(1.5)
        for i, produto in enumerate(lista_de_compras):
            print(i, produto)

    else:
        print("Por favor, escolha entre [i], [a] ou [l]")

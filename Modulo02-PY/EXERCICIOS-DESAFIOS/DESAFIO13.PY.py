"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação 
da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela 
deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
from time import sleep
contador_sim = 0
contador_nao = 0
while True:
    try:
        pergunta_tel = input("Telefonou para a vítima?")
        if pergunta_tel == 'sim':
            contador_sim += 1
        elif pergunta_tel == 'nao':
            contador_nao += 1
        else:
            print('Tente novamente...')
            continue
        pergunta_local = input("Esteve no local do crime?")
        if pergunta_local == 'sim':
            contador_sim += 1
        elif pergunta_local == 'nao':
            contador_nao += 1
        else:
            print('Tente novamente...')
            continue
        pergunta_mora_perto = input("Mora perto da vítima?")
        if pergunta_mora_perto == 'sim':
            contador_sim += 1
        elif pergunta_mora_perto == 'nao':
            contador_nao += 1
        else:
            print('Tente novamente...')
            continue
        pergunta_devia = input("Devia para a vítima?")
        if pergunta_devia == 'sim':
            contador_sim += 1
        elif pergunta_devia == 'nao':
            contador_nao += 1
        else:
            print('Tente novamente...')
            continue
        pergunta_trabalhou = input("Já trabalhou com a vítima?")
        if pergunta_trabalhou == 'sim':
            contador_sim += 1
        elif pergunta_trabalhou == 'nao':
            contador_nao += 1
        else:
            print('Tente novamente...')
            continue

        sleep(2)

        if contador_sim == 2:
            print('Você é suspeito')
            break
        elif contador_sim == 3 or contador_sim == 4:
            print('Você é cumplice')
            break
        elif contador_sim > 4:
            print('Você é Assassino')
            break
    except ValueError:
        print("Digite palavras ao invés de números, tente novamente...")
        continue

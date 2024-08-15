# Exercício - sistema de perguntas e respostas
from time import sleep
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quem é o melhor jogador de futebol do mundo?',
        'Opções': ['Neymar Junior', 'Cristiano Ronaldo', 'Lionel Messi', 'Yuri Alberto'],
        'Resposta': 'Neymar Junior',
    },
]

# CÓDIGO:

def traco():
    print('-' * 25)


contador_acertos = 0
while True:
    for pergunta in perguntas:
        print()
        print(pergunta['Pergunta'])
        for i, opcao in enumerate(pergunta['Opções']):
            print(f'{i}) {opcao}')

        try:
            resposta_1 = int(input('Digite uma opção: '))
            if pergunta['Opções'][resposta_1] == pergunta['Resposta']:
                print('\nRESPOSTA CORRETA 👍')
                contador_acertos += 1
                print()
                traco()
            else:
                print('RESPOSTA ERRADA❌ || \nA resposta correta era: ', end=' ')
                print(pergunta['Resposta'])
                print()
                traco()
        except (ValueError, IndexError):
            print('Valor inválido, tenta novamente.')
            traco()
            continue
    break

if contador_acertos == 1:
    print(f'\nVocê acertou {contador_acertos} perguntas de 3 perguntas, precisa melhorar!')

elif contador_acertos == 2:
    print(f'\nVocê acertou {contador_acertos} perguntas de 3 perguntas, está ótimo!')

elif contador_acertos == 3:
    print(f'\nVocê acertou {contador_acertos} perguntas de 3 perguntas, PARABÉNS!!!')

sleep(1)
print('\nFIM')

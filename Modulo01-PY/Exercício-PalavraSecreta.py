"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
# ----------------------------------------------
"""
Make a game for the user to guess which one
the secret word.
- You will propose a secret word
any and will give the possibility to
the user types only one letter.
- When the user types a letter, you
will check if the letter entered is
in the secret word.
    - If the letter entered is in the
    secret word; display the letter;
    - If the letter entered is not
    in the secret word; display *.
Count your attempts
user.
"""
# ----------- CODE -------------#
from time import sleep
import os
contador_tentativas = 0
palavra_secreta = 'neymar'
tentativas_certas = ''
while True:
    tentativa_usuario = input("Digite uma letra: ").lower()
    contador_tentativas += 1

    # SE O USUARIO DIGITAR > 1 LETRA, CAI NO PRINT E VOLTA NO WHILE (CONTINUE) ATÉ ELE DIGITAR SOMENTE !!! UMA !!! LETRA.
    if len(tentativa_usuario) > 1:
        print('Digite apenas UMA letra por favor')
        continue

    # SE A LETRA DE TENTATIVA DO USUÁRIO ESTIVER NA PALAVRA SECRETA, A VARIAVEL DE TENTATIVAS CERTAS VAI RECEBER ESSAS LETRAS QUE O USUÁRIO ACERTOU.
    if tentativa_usuario in palavra_secreta:
        tentativas_certas += tentativa_usuario

    palavra_formada = ''
    for letra_secreta in palavra_secreta:  # PERCORRENDO LETRA POR LETRA DA MINHA PALAVRA SECRETA
        # SE A LETRA SECRETA ESTIVER NAS TENTATIVAS CERTAS DO USUÁRIO, ELE SUBSTITUI PELA LETRA, CASO NÃO, ENTRA NO ELSE ( MOSTRA O '*')
        if letra_secreta in tentativas_certas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
        print("VOCÊ GANHOU!")
        print('A palavra era', palavra_secreta)
        print(f"\nSeu numero de tentativas: [ {contador_tentativas}x ]")
        sleep(0.75)
        print('\nLIMPANDO...')
        sleep(2)
        os.system('cls')

# EX01 -  MANIPULAÇÃO DE SRINGS
nome = str(input("Digite seu nome: ")).strip()
print(f"Olá {nome}, irei mostrar seu nome em diversas formas!")
# MOSTRO AO USUÁRIO O SEU NOME DE VÁRIAS FORMAS
print(f"Seu nome em maiúsculo é: {nome.upper()}")
print(f"Seu nome em minúsculo é: {nome.lower()}")
print(f"Seu nome tem {len(nome) - nome.count(' ')} letras")

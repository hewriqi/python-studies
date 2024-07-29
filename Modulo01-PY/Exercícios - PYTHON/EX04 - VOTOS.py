from time import sleep

print("""CANDIDATOS:
      [1] Henrique
      [2] Gabriel
      [3] Carlos
      [4] Pedro""")

# Contadores de votos para cada candidato
contador_henrique = 0
contador_gabriel = 0
contador_carlos = 0
contador_pedro = 0

while True:
    voto_usuario = input("Qual seu voto?: ")

    if voto_usuario == '1':
        contador_henrique += 1
    elif voto_usuario == '2':
        contador_gabriel += 1
    elif voto_usuario == '3':
        contador_carlos += 1
    elif voto_usuario == '4':
        contador_pedro += 1
    else:
        print("Voto inválido. Tente novamente.")
        continue

    pergunta_sair = input('Deseja parar de votar? (s/n): ').strip().lower()
    if pergunta_sair == 's':
        print('SAINDO...')
        sleep(1.3)
        break
    elif pergunta_sair == 'n':
        print('CONTINUANDO...')
        sleep(1)
    else:
        print("Resposta inválida. Tente novamente.")

# Determinando o candidato com mais votos
candidatos = {
    'Henrique': contador_henrique,
    'Gabriel': contador_gabriel,
    'Carlos': contador_carlos,
    'Pedro': contador_pedro
}

mais_votos = max(candidatos, key=candidatos.get)
quantidade_votos = candidatos[mais_votos]

print(f'O candidato com mais votos é o {
      mais_votos}, com {quantidade_votos} votos.')

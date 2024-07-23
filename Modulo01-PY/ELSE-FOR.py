# ELSE COM FOR
for i in range(10):  # Pega item por item do range (0 até 9)
    if i == 2:  # Se o i for 2, ele pula por causa do 'continue'
        print("i é 2, pulando...")
        continue
    if i == 8:  # Quando o 'i' for 8, ele vai parar a execução por causa do 'break'
        print("i é 8, seu else não vai executar!")
        break
    for j in range(1, 3):  # Aqui eu to falando o início e o fim (1 ao 2, porque o ultimo não é incluido)
        print(i, j)
else:  # Else com 'for', idêntico ao while praticamente.
    print("For completo com sucesso!")

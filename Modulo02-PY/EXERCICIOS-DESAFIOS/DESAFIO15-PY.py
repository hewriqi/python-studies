"""
Crie um código que seja capaz de encontrar e exibir a maior e a menor palavra da lista (em número de caracteres).
"""
palavras = ["python", "asimov", "código", "web", "programação"]
maior_palavra = max(palavras, key=len)
menor_palavra = min(palavras, key=len)
print(maior_palavra)
print(menor_palavra)

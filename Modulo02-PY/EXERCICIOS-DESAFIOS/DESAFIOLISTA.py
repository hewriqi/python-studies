"""
Exercício: Manipulação de Lista de Números
    Crie uma lista de números inteiros.
    Calcule e imprima a soma dos números na lista.
    Encontre e imprima o maior número da lista.
    Encontre e imprima o menor número da lista.
    Crie uma nova lista contendo apenas os números pares da lista original e imprima essa nova lista.
"""
numeros = [8, 4, 1, 9, 7, 6, 3, 2, 5]

soma_lista = sum(numeros)
print()
print(f'O resultado da soma dos números da lista é de: {soma_lista} ')

print()

maiorNUM_lista = max(numeros)
print(f'O maior número da lista é o: {maiorNUM_lista} ')

print()

menorNUM_lista = min(numeros)
print(f'O menor número da lista é o: {menorNUM_lista} ')

print()

lista_pares = [numero for numero in numeros if numero % 2 == 0]
print(lista_pares)

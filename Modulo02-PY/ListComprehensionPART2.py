def divisaoFn(x, y):
    return x / y


def multiplicacao(x, y):
    return x * y


def potenciacao2(x, y):
    return x ** y


numeros = [1, 2, 3, 4, 5]
divisao = [divisaoFn(numero, 2) for numero in numeros]
mult = [multiplicacao(numero, 2) for numero in numeros]
quadrado = [potenciacao2(numero, 2) for numero in numeros]

# novos_numeros = []
# for numero in numeros:
#     novos_numeros.append(numero)
print(numeros)
print(divisao)
print(mult)
print(quadrado)
print('=' * 40)
# ---- condicionais ----
print('=' * 40)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [number for number in numbers if number > 5]

impares = [number for number in numbers if number % 2 != 0]
pares = [number for number in numbers if number % 2 == 0]
other_if = [
    number
    if number != 6 else 600
    for number in pares
]

print(numbers)
print(new_numbers)
print(impares)
print(pares)
print(other_if)
print('=' * 40)
# ---- Linhas e colunas ----
print('=' * 40)
for x in range(1, 11):
    for y in range(1, 6):
        print(x, y)

# como fazer o metodo acima usando list comprehension

linhas_e_colunas = [
    (x, y)
    if y != 2 else (x, y * 2000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]

print(linhas_e_colunas)

print('=' * 40)
# ---- strings ----
print('=' * 40)
string = 'Henrique Junior'
numero_de_quantas_letras_quero_pegar = 2
nova_string = '.'.join([
    string[indice:indice + numero_de_quantas_letras_quero_pegar]
    for indice in range(0, len(string), 2)
])
print(nova_string)

print('=' * 40)
# ---- com listas ----
print('=' * 40)
nomes = ['henrique', 'luiz', 'joana', 'roberto', 'maria']
# Deixando ultima letra maiúscula
novos_nomes = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes]

print(novos_nomes)

print('=' * 40)
# ---- flat ----

numeros_flat = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros_flat)
print(flat)

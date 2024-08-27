# Fatorial de um número em python
def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


numero = int(
    input("Digite um número inteiro não-negativo para calcular o fatorial: "))
print(f"O fatorial de {numero} é {fatorial(numero)}")

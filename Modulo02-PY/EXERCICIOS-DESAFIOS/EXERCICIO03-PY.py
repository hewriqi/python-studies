# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
def multiplicacao():
    numero_usuario = int(input('Digite um número: '))
    numero_multiplicar = int(input(
        'Digite um outro número para fazer a multiplicação (Dobrar, triplicar, quadruplicar, etc...): '))
    conta = numero_usuario * numero_multiplicar
    return conta


print(multiplicacao())

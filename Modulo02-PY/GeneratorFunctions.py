# Introdução às Generator functions em PYTHON

# def generator(n=0):
#     yield 1  # Pausa
#     print('Continuando...')
#     yield 2  # Pausa
#     print('Continua...')
#     yield 3  # Pausa
#     print('Vou terminar')
#     return 'ACABOU'


# gen = generator(n=0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


def generador(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n > maximum:
            return 'ACABOU'


genn = generador(n=5, maximum=9)
for n in genn:
    print(n)

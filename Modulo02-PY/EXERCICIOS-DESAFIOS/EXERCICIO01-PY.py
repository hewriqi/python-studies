total = 1
while True:
    nums = int(input('Digite os números para ser multiplicados:  '))
    total *= nums
    question = str(input('Deseja sair? [s/n]: '))
    if question == 's':
        break
    elif question == 'n':
        continue

print(total)

# -------------- OU -----------------


def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


mult = multiplicacao(10, 2, 3, 5, 64, 3)
print(mult)

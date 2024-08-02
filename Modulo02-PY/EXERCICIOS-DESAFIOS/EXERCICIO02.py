# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.
def par_impar(numero):
    resto_0 = numero % 2 == 0

    if resto_0:  # SE O 'RESTO_0' FOR TRUE, ELE CAI NESSE RETURN DENTRO DO 'IF'
        return f'{numero} é par'
    return f'{numero} é ímpar'


print(par_impar(2))
print(par_impar(15))
print(par_impar(22))
print(par_impar(3))
print(par_impar(4))
print(par_impar(158))

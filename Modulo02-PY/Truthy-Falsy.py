# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


def falsy(valor):
    # se o valor for falsy, retorna 'falsy', senão ele retorna 'truthy'.
    return 'falsy' if not valor else 'truthy'


# AQUI DEU TRUTHY, PORQUE É UMA STRING QUE TEM 'VALOR'.
print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(1))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))
# O RESTO ESTÁ COMO 'FALSY', POIS NÃO TEM VALOR ATRIBUIDO A NENHUM DELES

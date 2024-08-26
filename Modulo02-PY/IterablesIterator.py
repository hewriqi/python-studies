# Iterables and Iterator in Python
import sys


iteravel = ['Eu', 'Tenho', '__iter__']
iterator = iter(iteravel)  # tem __iter__ e __next__
print(next(iterator))
lista = [numero for numero in range(100000)]
generator = (numero for numero in range(100000))
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(lista[5000])

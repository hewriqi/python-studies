# dir, hasattr e getttr em Python
string = 'Henrique'
metodo = 'len'

if hasattr(string, metodo):
    print('Existe lower')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)

try:
    print('ABRIR O ARQUIVO')
    8/0
except ZeroDivisionError:
    print('DIVIDIU POR ZERO!')
finally:
    print('FECHAR ARQUIVO')

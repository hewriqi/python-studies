# Try, except, else e finally
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    print('LINHA 1'[10000])
    c = a / b
    print('LINHA 2')

except ZeroDivisionError:
    print('Dividiu por 0')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('NAME:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.  ')

print('CONTINUAR')

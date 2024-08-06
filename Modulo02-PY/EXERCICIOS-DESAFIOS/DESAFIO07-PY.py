def digitos(numero):
    str(numero)
    dig_numeros = len(numero)
    return dig_numeros


numero_usuario = input('Digite um número: ')
resultado = digitos(numero_usuario)
print(f'O número de dígitos de {numero_usuario} é {resultado} ')

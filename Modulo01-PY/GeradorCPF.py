import random
import sys
# for _ in range(100) --> POSSO FAZER UM GERADOR DE 100 CPF'S
nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9))

print(nove_digitos)

contador_regressivo = 10
resultado_conta = 0
print(' ')
# PARA CADA NUMERO NO CPF GUARDADO NA VARIAVEL 'NOVE_DIGITOS', EU VOU FAZER O SEGUINTE:
for numero in nove_digitos:
    conta = int(numero) * contador_regressivo
    print(f'{numero} x {contador_regressivo} = {conta} ')
    resultado_conta += conta
    contador_regressivo -= 1
print(f'\nO resultado da soma de todos os valores das multiplicações acima é de: [ {
      resultado_conta} ]')

multiplicacao_por_10 = resultado_conta * 10
resultado_final = multiplicacao_por_10 % 11
digito = resultado_final if resultado_final <= 9 else 0

print(f'\nO valor do primeiro digito é de: [ {digito} ] ')

dez_digitos = nove_digitos + str(digito)
print(dez_digitos)
contagem_regressiva_2 = 11
resultado_conta_2 = 0
for numero_2 in dez_digitos:
    conta_2 = int(numero_2) * contagem_regressiva_2
    print(f"{numero_2} x {contagem_regressiva_2} = {conta_2}")
    contagem_regressiva_2 -= 1
    resultado_conta_2 += conta_2

print(f'O resultado da soma de todas as multiplicações acima é de: [ {
      resultado_conta_2} ]')

multiplicacao_por_10_2 = resultado_conta_2 * 10
resultado_final_2 = multiplicacao_por_10_2 % 11
digito_2 = resultado_final_2 if resultado_final_2 <= 9 else 0

print(f'\nO valor do 2º dígito é de: [ {digito_2} ]\n')
cpf_certo = dez_digitos + str(digito_2)
print('')
print(cpf_certo)
print('\nFIM')

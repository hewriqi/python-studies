"""
Cálculo dos dígitos do CPF:

CPF: 697.079.500-48
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10.

Ex:  697.079.500-48 (697079500)
    10  9  8  7  6  5  4  3  2
     6  9  7  0  7  9  5  0  0
    60 81 56  0 42  45 20 0  0

Somar todos os resultados:
60+81+56+0+42+45+20+0+0 = RESULTADO

Multiplicar o resultado anterior por 10:
RESULTADO * 10 = XXXX

Obter o resto da divisão da conta anterior por 11:
XXXX % 11 = X

Se o resultado anterior foi maior que 9:
    resultado é 0
Senão:
    resultado é o valor da conta

O primeiro digito do CPF é: NESSE CASO TEM QUE SER [ ' 4 ' ]
"""
# 697.079.500-48
cpf_pessoa = input("Digite seu CPF: ")  # PEDIR CPF PRA PESSOA
juntar_cpf = cpf_pessoa.replace('.', '').replace(
    '-', '')  # RETIRAR OS PONTOS E TRAÇO
print(f'\n{juntar_cpf}')  # MOSTRAR NA TELA

# FATIAR O CPF PARA PEGAR SOMENTE OS PRIMEIROS 9 DÍGITOS
nove_digitos = juntar_cpf[:9]
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


print('FIM')

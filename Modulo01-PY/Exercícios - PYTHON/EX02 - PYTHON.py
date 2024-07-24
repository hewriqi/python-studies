from time import sleep
contador_quantos_numeros = 0
# OS NUMEROS DIGITADOS PELO USUARIO, VÃO SER ADICIONADOS AQUI DENTRO DESSA LISTA
lista_numeros_usuario = []
while True:
    numero_digitado_usuario = int(
        input("Digite um número qualquer. Se caso deseja sair, digite [ 999 ]:  "))
    if numero_digitado_usuario != 999:
        lista_numeros_usuario.append(numero_digitado_usuario)
        continue
    elif numero_digitado_usuario == 999:
        quantos_numeros_tem_na_lista = len(lista_numeros_usuario)
        soma_da_lista_de_numeros = sum(lista_numeros_usuario)
        print('SAINDO...')
        sleep(1.75)
        break

print(f'Foram digitados {quantos_numeros_tem_na_lista} números.')
print(f'A soma de todos os números digitados foi de: [ {
      soma_da_lista_de_numeros} ]')

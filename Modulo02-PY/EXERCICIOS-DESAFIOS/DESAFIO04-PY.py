"""
Faça um Programa que peça a idade e a altura 
de 5 pessoas, armazene cada informação na sua 
respectiva lista. Imprima a idade e a altura 
na ordem inversa a ordem lida.
"""
altura = []
idade = []

for i in range(5):
    print(f'Pessoa {i+1}')
    pedir_altura = float(input("Digite sua altura: "))
    altura.append(pedir_altura)
    pedir_idade = int(input("Digite sua idade: "))
    idade.append(pedir_idade)

print("INVERSO DAS RESPOSTAS: ")
print('-' * 30)
inverso_altura = reversed(altura)
inverso_idade = reversed(idade)

print(inverso_altura)
print(inverso_idade)

"""
Cuidados com dados mutáveis
USANDO O SINAL DE ' = ' COM DADOS IMUTAVEIS, VOCÊ COPIA O VALOR E ETC - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Henrique'
# outra_var = nome
# nome = 'Caio'
# print(nome)
# print(outra_var)

lista_a = ['Henrique', 'Junior']
lista_b = lista_a  # <--- AQUI EU NÃO ESTOU FAZENDO O VALOR B TER O MESMO VALOR QUE O A, E SIM OS DOIS APONTAREM PARA O MESMO VALOR NA MEMÓRIA
lista_a[0] = 'Qualquer coisa'
print(lista_b)

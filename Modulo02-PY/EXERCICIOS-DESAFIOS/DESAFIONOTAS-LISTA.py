"""
Exercício: Estatísticas de Notas
    Crie uma lista com as notas de uma turma de estudantes. X
    Calcule e imprima a média das notas. X
    Crie uma lista com as notas que estão acima da média e imprima essa lista.
    Encontre e imprima a nota mais alta e a nota mais baixa da turma.
    Crie uma lista com a classificação das notas em categorias: 'Aprovado' para notas maiores ou iguais a 7, e 'Reprovado' para notas abaixo de 7. Imprima a lista com as classificações.
"""
notas = [5.5, 8.0, 6.5, 7.5, 9.0, 4.0, 6.0, 7.0, 8.5]

media = (sum(notas)) / len(notas)
print(f'A média das notas dessa turma de estudantes é de: {media}')

print()

lista_acima_da_media = [nota for nota in notas if nota >= 7.0]
print(f'A lista das notas acima da média: {lista_acima_da_media}')

print()

maior_nota = max(notas)
menor_nota = min(notas)

print()

lista_aprovados = []
lista_reprovados = []

for nota in notas:
    if nota >= 7.0:
        lista_aprovados.append(nota)
        print()
        print(f'{nota}: Aprovado!')
    else:
        lista_reprovados.append(nota)
        print()
        print(f'{nota}: Reprovado!')


print('*' * 30)
print(lista_aprovados)
print()
print(lista_reprovados)

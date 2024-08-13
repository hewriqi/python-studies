# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome'

pessoa[chave] = 'Henrique Barros'
pessoa['sobrenome'] = 'Junior'

print(pessoa[chave])

pessoa[chave] = 'Luiz'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('NAO EXISTE!')
else:
    print(pessoa['sobrenome'])

##
##

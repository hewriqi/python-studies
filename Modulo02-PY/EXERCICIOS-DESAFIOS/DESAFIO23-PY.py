# Dada uma lista de frutas, crie uma nova lista com o comprimento de cada fruta, apenas para as frutas com mais de 5 letras.
frutas = ['Maça', 'Banana', 'Pera', 'Abacaxi', 'Manga', 'Jabuticaba']

frutas_lista_nova = [fruta for fruta in frutas if len(fruta) > 5]

print(frutas_lista_nova)

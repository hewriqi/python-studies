"""
Crie um programa que tenha uma função
chamada voto() que via receber como parâmetro 
o ano de nascimento de uma pessoa, retornando
um valor literal indicando se uma pessoa tem 
voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.

Create a program that has a function
call vote() that via receive as a parameter 
the year of birth of a person, returning
a literal value indicating whether a person has 
DENIED, OPTIONAL or MANDATORY vote in elections.
"""
from datetime import date


def voto(ano):
    atual = date.today().year
    idade = atual - nasc
    if idade < 16:
        return f'Você tem {idade} anos e seu voto foi NEGADO'
    elif idade >= 16 and idade < 18 or idade >= 65:
        return f'Você tem {idade} anos e seu voto é OPCIONAL'
    else:
        return f'Você tem {idade} anos e seu voto é OBRIGATÓRIO, vá votar!'


nasc = int(input('Em que ano você nasceu?: '))
print(voto(nasc))

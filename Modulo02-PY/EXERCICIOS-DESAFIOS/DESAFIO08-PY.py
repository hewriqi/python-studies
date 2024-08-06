"""
Construa uma função que receba uma string como parâmetro 
e devolva outra string com os carateres embaralhados. 
Por exemplo: se função receber a palavra python, pode retornar
npthyo, ophtyn ou qualquer outra combinação possível, de forma
aleatória. Padronize em sua função que todos os caracteres 
serão devolvidos em caixa alta ou caixa baixa, independentemente 
de como foram digitados.
"""
import random


def embaralhar_strings(string_usuario):
    lista_caracteres = list(string_usuario)
    random.shuffle(lista_caracteres)

    return lista_caracteres


string_digitada = input("Digite uma palavra: ").strip().upper()
resultado = embaralhar_strings(string_digitada)
print("Palavra embaralhada: ", resultado)

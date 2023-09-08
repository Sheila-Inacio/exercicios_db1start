# Escreva um programa que execute uma função que multiplique todos os números de uma lista passada por parâmetro

lista_numeros = [1, 2, 3, 4, 5, 6]

def multi_lista(lista):
    multi_numeros = 1
    for x in range(len(lista)):
        multi_numeros *= lista[x]     
    return multi_numeros

print (multi_lista(lista_numeros))

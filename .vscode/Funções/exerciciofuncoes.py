# Escreva um programa que execute uma função que
# encontre o maior número de uma lista passada por
# parâmetro

lista1 = [12, 24, 3, 47, 51, 50]
lista2 = [1, 42, 8, 65, 85, 42]
maior = 0

def maior_numero (lista):
    for x in range(len(lista)):
        if x == 0:
            maior = lista[x]
        if lista[x] > maior:
            maior = lista[x]
    return maior
    

print (maior_numero(lista2))
print (maior_numero(lista1))
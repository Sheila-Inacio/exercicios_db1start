# Escreva um programa que retorne o maior e o menor
# número de uma lista

lista = [10, 20, 30, 0, 8, 50, 41]
maior = 0
menor = 0
for x in lista:
    if maior == 0 and menor == 0:
        maior = x
        menor = x
    if x >= maior:
        maior = x
    if x <= menor:
        menor = x


# for x in range(len(lista)):
#     if x == 0:
#         maior = lista[x]
#         menor = lista[x]
#     if lista[x] >= maior:
#         maior = lista[x]
#     if lista[x] <= menor:
#         menor = lista[x]
print(f" O numero maior é: {maior}, o numero menor é: {menor}")
# Escreva um programa que ordene em ordem
# crescente uma lista de tuplas informadas, pelo último
# item da tupla (Ex: [(2,5), (1,2), (4,4), (2,3), (2,1)]
# Resultado esperado: [(2,1), (1,2), (2,3), (4,4), (2,5)])]

lista_de_tuplas = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

lista_ordenada = sorted(lista_de_tuplas, key = lambda x : x[1])
print(lista_ordenada)

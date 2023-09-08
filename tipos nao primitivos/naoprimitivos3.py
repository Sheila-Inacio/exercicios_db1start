# Escreva um programa que conte o número de
# caracteres em uma string (Ex: 'google.com' Resultado
# esperado: {'o':3, 'g':2, '.':1, 'e':1, 'l':1, 'm':1, 'c':'})

nome = 'google.com'
caracteres = {}
lista_ordenada = {}
for letra in nome:
    if letra in caracteres.keys():
        caracteres[letra] = caracteres[letra] + 1
    else:
        caracteres[letra] = 1
for x in sorted(caracteres, key = caracteres.get, reverse=True):
    lista_ordenada[x] = caracteres[x]
print(lista_ordenada)


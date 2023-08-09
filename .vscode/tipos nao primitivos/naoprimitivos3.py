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


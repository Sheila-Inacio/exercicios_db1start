lista = ['sheila', 'daniel', 'mari', 'laica', 'daniel', 'mari']
iguais = []
for x in range(len(lista)):
    for i in range(x+1,len(lista)):
        if lista[x] == lista[i]:
            iguais.append(lista[x])
print(iguais)

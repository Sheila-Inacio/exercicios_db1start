# Escreva um programa que remova itens duplicados
# de uma lista


lista = ['sheila', 'daniel', 'mari', 'laica', 'daniel', 'mari']
iguais = []
for x in range(len(lista)):
    for i in range(x+1,len(lista)):
        if lista[x] == lista[i]:
            iguais.append(lista[x])
    
for x in iguais:
    lista.remove(x)    

print(lista)



# lista = ['sheila', 'daniel', 'mari', 'laica', 'daniel', 'mari']


# meu_set = set(lista)
# print(meu_set)
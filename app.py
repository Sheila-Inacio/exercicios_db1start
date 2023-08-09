nomes = {'cachorro':2, 'gato':3, 'elefante':1 }

for i in sorted(nomes, key = nomes.get):
    print(i, nomes[i])
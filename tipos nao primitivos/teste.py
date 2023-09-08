lista = ['sheila', 'daniel', 'mari', 'laica', 'pitucha', 'tob']
# peça ao usuário o nome que ele deseja procurar dentro da lista 
# ao final imprima a posição que o nome está na lista, ex: mari == 2
nome = input("Digite um nome:")
iguais = []

for x in range(len(lista)):
    if nome == lista [x]:
        iguais = x
            
print(f"{nome} == {iguais}")
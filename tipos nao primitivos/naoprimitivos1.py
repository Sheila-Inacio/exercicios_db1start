# Escreva um programa que multiplique todos os itens
# de uma lista

lista = [10, 20, 30]
multip = 0
for x in lista:
    if multip == 0:
        multip = x
    else:
        multip = x * multip 

print(multip)
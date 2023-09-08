# Escreva um programa que execute uma função que some todos os itens de uma lista passada por parâmetro

lista_numeros = [1, 2, 3, 4, 5, 6]

def soma_lista(lista):
    soma_numeros = 0
    for x in range(len(lista)):
        soma_numeros += lista[x]
        
      
    return soma_numeros

print (soma_lista(lista_numeros))

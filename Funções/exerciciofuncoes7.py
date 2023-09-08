# Escreva um programa que execute uma função que valide de um número informado é um número perfeito ou não

numero_informado = int(input("Informe um numero: "))

soma_numeros = 0

def numero_divisivel(numero):
    lista_numeros = []
    for x in range(1, numero_informado - 1):
        if numero_informado % x == 0 :
            lista_numeros.append(x)
    return lista_numeros

def soma_lista(lista):
    soma_numeros = 0
    for x in range(len(lista)):
        soma_numeros += lista[x] 
    return soma_numeros

lista = numero_divisivel(numero_informado)
soma = soma_lista(lista)
if soma == numero_informado:
    print("É um numero perfeito!")
else:
    print("Não é um numero perfeito.")


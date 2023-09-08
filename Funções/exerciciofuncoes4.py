# Escreva um programa que execute uma função que calcule o fatorial de um número passado por parâmetro
numero = int(input("Fatorial de: ") )

def fatorial_numero(unidade):
    fatorial = 1
    for x in range(1, unidade + 1):
       fatorial *=  x
          
    return fatorial

print(fatorial_numero(numero))

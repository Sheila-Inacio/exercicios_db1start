# Escreva um programa que execute uma função que conte o número de letras maiúsculas e minúsculas de um texto e que ao final 
#chame outra função para imprimir o resultado

texto = "Ola Pessoal de Tecnologia"

def contar_letras_maiusculas(letras):
    letra_maiuscula = 0

    for x in (letras):
       if x.isupper():
            letra_maiuscula += 1

    return letra_maiuscula

def contar_letras_minusculas(letras):
    letra_minusculas = 0

    for x in (letras):
       if x.islower():
            letra_minusculas += 1        

    return letra_minusculas

maiusculo = contar_letras_maiusculas(texto)
print(f"Numero de letras maiusculas {maiusculo}")
print(f"Numero de letras minusculas {contar_letras_minusculas(texto)}")
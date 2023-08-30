# Escreva um programa que execute uma função que receba um número informado no console como
# parâmetro e verifique se o número informado é primo ou não

numero_informado = int(input("Informe um numero: "))

def num_primo(valor):
    numero_primo = True
    for x in range(2, numero_informado - 1):
        if numero_informado % x == 0 :
            numero_primo = False
            break
    return numero_primo

print(num_primo(numero_informado))
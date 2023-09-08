numero = 0
maior = 0
for x in range(3):
    numero = int(input("Digite um numero: "))
    if numero > maior:
        maior = int(numero)
    

print (f" O numero maior é {maior}")
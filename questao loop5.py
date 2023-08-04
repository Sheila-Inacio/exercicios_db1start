numero = 0
maior = 0
menor = 0
for x in range(4):
    numero = int(input("Digite um numero: "))
    if x == 0:
        menor = int(numero)
        maior = int(numero)
    if numero > maior:
        maior = int(numero)
    if numero < menor:
        menor = int(numero)
     
print (f" O numero maior é {maior}, e o menor é {menor}")
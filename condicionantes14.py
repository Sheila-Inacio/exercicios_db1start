numero = input(" Digite um numero menor que 1000: ")
import math
if len(numero) > 0 and len(numero) < 4:
    if int(numero) > 100:
        centena = math.trunc(int(numero) /100)
        print(centena, "Centenas")
        numero = int(numero) - (centena * 100)
    if int(numero) > 10:
        dezena = math.trunc(int(numero) /10)
        print(dezena, "Dezenas")
        numero = int(numero) - (dezena * 10)
    if int(numero) > 0:
        print(numero, "Unidades")

else:
    print("numero inválido ")
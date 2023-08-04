a = int(input("Digite primeiro numero : "))
b = int(input("Digite segundo numero: "))
c = int(input("Digite terceiro numero: "))
if (a > b) and (a > c):
    print(a, "é MAIOR que todos!")
elif (b > a) and (b > c):
    print(b, "é MAIOR que todos!")
else:
    print(c, "é MAIOR que todos!")
if (a < b) and (a < c):
    print(a, "é MENOR que todos!")
elif (b < a) and (b < c):
    print(b, "é MENOR que todos!")
else:
    print(c, "é MENOR que todos!")

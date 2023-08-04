a = int(input("Digite primeiro numero : "))
b = int(input("Digite segundo numero: "))
c = int(input("Digite terceiro numero: "))
if (a > b) and (a > c):
    print(a)
elif (b > a) and (b > c):
    print(b)
else:
    print(c)

if (a < b) and (a < c):
    print(a)
elif (b < a) and (b < c):
    print(b)
else:
    print(c)
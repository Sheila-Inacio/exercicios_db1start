a = int(input("Digite primeiro lado: "))
b = int(input("Digite segundo lado: "))
c = int(input("Digite terceiro lado: "))
if (a == b) and (a == c):
    print("Equilátero ")
elif (a!=b) and (b != c) and (c != a):
    print("Escaleno ")
else:
    print("Isósceles ")
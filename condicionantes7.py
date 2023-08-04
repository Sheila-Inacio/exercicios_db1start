a = int(input("Digite primeiro numero : "))
b = int(input("Digite segundo numero: "))
c = int(input("Digite terceiro numero: "))
if (a >= b) and (a >= c) and (b >= c):
    print(f'A ordem decrescente é {a}, {b}, {c}')
elif (a >= b) and (a >= c) and (c >= b):
    print(f'A ordem decrescente é {a}, {c}, {b}')
elif (b >= a) and (b >= c) and (a >= c):
    print(f'A ordem decrescente é {b}, {a}, {c}')
elif (b >= a) and (b >= c) and (c >= a):
    print(f'A ordem decrescente é {b}, {c}, {a}')
elif (c >= a) and (c >= b) and (b >= a):
    print(f'A ordem decrescente é {c}, {b}, {a}')
elif (c >= a) and (c >= b) and (a >= b):
    print(f'A ordem decrescente é {c}, {a}, {b}')
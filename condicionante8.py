list = []
a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o segundo numero: "))
list.append(a)
list.append(b)
list.append(c)
list.sort(reverse=True)

print(f'A ordem decrescente é {list}')
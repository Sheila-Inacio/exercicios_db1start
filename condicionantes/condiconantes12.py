ano = int(input(" Digite um ano "))
resultado = (ano % 4)
if resultado == 0:
    print("Este ano é bissexto! ")
else:
    print("Esse ano não é bissexto")
def calcular_soma(num):
    soma = 0
    for i in range(0, num + 1, 2):
      soma += i
          
    return soma

print(calcular_soma(10))
     
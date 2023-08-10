# Escreva um programa que conte quantas strings
# tenham tamanho maior que 2 e o primeiro e último
# caracteres sejam iguais (Ex: ['acb', 'xyz', 'aba', '1221']
# Resultado esperado:2)


lista = ['acb', 'xyz', 'aba', '1221']
iguais = 0
for x in lista:    
   posicao = len(x)-1
   if x[0] == x[posicao]:
      iguais += 1

print(iguais)
# Escreva um programa que concatene os dicionários
# abaixo e crie um novo
# Ex:
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
# Resultado esperado: {1:10, 2:20, 3:30, 4:40, 5:50,
# 6:60}



dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}
nova_lista = {}


nova_lista.update(dic1)
nova_lista.update(dic2)
nova_lista.update(dic3)

print(nova_lista)
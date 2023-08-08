numero_caes = int(input("Informe o numero de cachorros que você tem: "))
lista_nomes = []
lista_gramas = []
semana = 0
mes = 0
for x in range(numero_caes):
    nome = input("Informe o nome do seu cachorro: ")
    gramas = int(input (f"Quantas gramas {nome} come por dia: "))
    lista_nomes.append(nome)
    lista_gramas.append(gramas)
    
for x in range(numero_caes):
    print(f"- {lista_nomes[x]} => {lista_gramas[x]} -  por semana: {(lista_gramas[x]) * 7}g - por mês: {(lista_gramas[x] * 30)}g ")
    semana += lista_gramas [x] * 7
    mes += lista_gramas[x] * 30
print(f"Total => {semana} gramas/semana {mes} gramas/mês")
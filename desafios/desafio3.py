print(" ----------------- Aposta da mega-sena! Boa sorte. ----------------- ")

numeros_aposta = int(input("Informe quantos numeros quer apostar de 6 à 10: "))
numero_escolha = 0
numero_jaescolhido = False
lista = []

while numeros_aposta < 6 or numeros_aposta > 10:
    print("Numero inválido! ")
    numeros_aposta = int(input("Informe quantos numeros quer apostar de 6 à 10: "))

while len(lista) < numeros_aposta:
    numero_escolha = int(input(f"Informe {len(lista) + 1} numero da aposta, deve ser entre 1 à 60: "))
    if numero_escolha < 0:
       print('Numero invalido!')
       continue
    if numero_escolha > 60:
        print('Numero invalido!')
        continue
    for x in lista:
        if x == numero_escolha :
            numero_jaescolhido = True
    if numero_jaescolhido:
        print(f'Numero {numero_escolha} já escolhido!')
        numero_jaescolhido = False
        continue
    lista.append(numero_escolha)
if numeros_aposta == 6:
    print(" O valor da aposta é 5 Reais ")      
elif numeros_aposta == 7:
    print(" O valor da aposta é 31,50 Reais ")     
elif numeros_aposta == 8:
    print(" O valor da aposta é 126,00 Reais ")   
elif numeros_aposta == 9:
    print(" O valor da aposta é 378,00 Reais ")   
elif numeros_aposta == 10:
    print(" O valor da aposta é 945,00 Reais ") 

print(lista)
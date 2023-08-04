print(" ----------------- Aposta da mega-sena! Boa sorte. ----------------- ")

numeros_aposta = int(input("Informe quantos numeros quer apostar de 6 à 10: "))
numeros_escolha = 0
x = 1

while numeros_aposta < 6 or numeros_aposta > 10:
    print("Numero inválido! ")
    numeros_aposta = int(input("Informe quantos numeros quer apostar de 6 à 10: "))




if numeros_escolha > 1 or numeros_escolha < 61:
    numeros_escolha = int(input(f"Informe {x} numero da aposta, deve ser entre 1 à 60: "))
    x = x + 1

    
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

#  print(" [] ")  

# 6 == [({'5 Reais']
# 7 == ['31.50 Reais']  
# 8 == ['126,00 Reais']
# 9 == ['378,00 Reais']
# 10 == ['945,00 Reais']
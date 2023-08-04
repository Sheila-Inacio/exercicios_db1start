media_doacoes = float(input("Informe a média de doações dos últimos 3 anos: "))  
doacoes_atual = float(input("Informe o total de doações deste ano: "))

total = doacoes_atual * 2  

if doacoes_atual > media_doacoes: 
    excedente = doacoes_atual - media_doacoes 
    total += excedente * 3 
print(f"O total em doações será R$ {total:.2f}")
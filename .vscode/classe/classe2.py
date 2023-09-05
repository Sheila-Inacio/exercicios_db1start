# Escreva uma classe em Python que leia dois números e implemente uma exponenciação

class Expoente_num:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def exponenciacao(self): 
        numero_expoente = (self.num1) ** (self.num2)
  
        return  numero_expoente
    
n = Expoente_num(9, 3)
print(n.exponenciacao())

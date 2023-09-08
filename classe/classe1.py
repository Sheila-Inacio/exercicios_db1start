# Escreva uma classe em Python para converter um numeral romano em um número inteiro

class Numero_Inteiro:
    def __init__(self, input:str):
        self.input = input

    def int_to_inteiro(self): 
        nums = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        soma = 0
        numero_romano = self.input

        for i in range(len(nums)):
            letra = nums[i]
            while numero_romano.startswith(letra):
                soma += ints[i]
                numero_romano = numero_romano[len(letra):]  
        return soma
    

n = Numero_Inteiro('MMXXIII')
print(n.int_to_inteiro())

# Escreva uma classe em Python para converter um número inteiro em um numeral romano
class Numero_Romano:
    def __init__(self, input):
        self.input = input

    def int_to_roman(self): 
        ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        nums = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = []

        for i in range(len(ints)):
            count = int(self.input / ints[i])
            result.append(nums[i] * count)
            self.input -= ints[i] * count
        return ''.join(result)
    

n = Numero_Romano(2023)
print(n.int_to_roman())

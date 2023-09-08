# Crie uma classe chamada Ponto3D que herde de Object. Na classe Ponto3D, crie um construtor que receba 3 números e armazene-os 
# em 3 variáveis. Crie uma forma para que ao exibir o conteúdo da instancia a informação apresentada seja: (<num1>;<num2>;<num3>)

class Ponto3D(object):
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3
    def __str__(self):
        return f'(<{self.num1}>;<{self.num2}>;<{self.num3}>)'
    
dado = Ponto3D(33, 55, 66)
print(dado)

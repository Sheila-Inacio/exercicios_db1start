# Crie uma classe Triangulo que receba no seu construtor 3 medidas de ângulos. Crie um método check_angulo que valide as 
# informações dos 3 ângulos informados na criação da classe. Instancie a classe Triangulo e imprima os ângulos informados e
# imprima se o triângulo é um triângulo ou não. O método check_angulo deverá retornar True se a soma dos valores for igual a
# 180 e false em qualquer outra possibilidade

class Triangulo:
    def __init__(self, angulo1, angulo2, angulo3):
        self.angulo1 = angulo1
        self.angulo2 = angulo2
        self.angulo3 = angulo3

    def check_angulo(self):
        soma = self.angulo1 + self.angulo2 + self.angulo3
        isTriangulo = soma == 180
        return isTriangulo
    
    def imprimir(self):
        print(self.angulo1, self.angulo2, self.angulo3)
       
        if self.check_angulo():
            print('É um triangulo! ')
        else:
            print('Não é um triangulo! ')

forma = Triangulo(60, 60, 60)
forma1 = Triangulo(60, 60, 50)

forma.imprimir()
forma1.imprimir()

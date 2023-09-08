# Escreva uma classe em Python que possua 2 métodos: um chamado 'adicionar_string' e outro
# chamado 'inverter_string'. O primeiro deverá receber uma string como parâmetro e armazená-la em um
# array. O segundo deverá listar as strings invertidas  no seu conteúdo e também na sua ordem de inclusão

class Listas:
    def __init__(self):
        self.lista1 = []
        self.lista_inv = []

    def adicionar_string(self, texto):
        self.lista1.append(texto)

               
    def inverter_string(self):
        for x in range(len(self.lista1)-1, -1, -1):
            nome = self.lista1[x]
            nome_invertido = nome[::-1]
            self.lista_inv.append(nome_invertido)
        return  self.lista_inv
 
s = Listas()
s.adicionar_string("Daniel")
s.adicionar_string("Sheila")
s.adicionar_string("Laica")

print(s.inverter_string())
# Escreva uma classe em Python que receba como argumentos um ID, um nome e a turma de um estudante, sendo que o nome e a 
# turma não são obrigatórios no momento da instanciação da classe. Crie um método que imprima o ID do aluno e se houver 
# um nome imprima o nome, e se houver turma imprima a turma também. 

class Escola:
    def __init__(self, id:int, nome = '', turma = ''):
        self.id = id
        self.nome = nome
        self.turma = turma
    def imprimir(self):
        texto = 'ID: ' + str(self.id)
        if self.nome != '':
            texto += ' Nome: ' + self.nome
        if self.turma != '':
            texto += ' Turma: ' + self.turma
        print(texto)

# dados = Escola(98, 'Daniel', '4 ano')
# dados2 = Escola(99, 'Sheila', '')
# dados3 = Escola(100, '', '')

# dados.imprimir()
# dados2.imprimir()
# dados3.imprimir()

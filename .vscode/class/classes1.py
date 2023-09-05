class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome


Daniel = Pessoa('Daniel')
print(Daniel)
Sheila = Pessoa('Sheila')
print(Sheila)
# Criar uma classe Musica, que deverá receber como  parâmetro de criação uma lista de string com as estrofes de uma música. 
# Essa classe deverá conter um método chamado cante_para_mim que imprima todas as estrofes, uma em cada linha. Para executar
# instancie a classe e execute o método

class Musica:
    def __init__(self, lista: str):
        self.letra = lista

    def cante_para_mim(self):
        for i in range(len(self.letra)):
            print(self.letra[i])


lista = ['Exagerado', 'Jogado aos teus pés', 'Eu sou mesmo exagerado', 'Adoro um amor inventado']
exagerado = Musica(lista)
exagerado.cante_para_mim()

print(' ------------------------------------- ')

lista2 = ['Você está me dando umas olhadas', 'E deixando minha cabeça a mil, puta que pariu', 'E o pior é que cê nem disfarça', 'Tem maldade na sua cara']
canudinho = Musica(lista2)
canudinho.cante_para_mim()
# Utilizando a classe criada no exercício 5 imprima o tipo da classe, as chaves e valores do atributo __dict__

from classe4 import Escola

dados = Escola(98, 'Daniel', '4 ano')
print('Dict', vars(dados))

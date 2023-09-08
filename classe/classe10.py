# Crie uma classe que representará outro tipo de aeronave militar, com o nome JatoMilitar2Lugares. O método construtor deverá receber
# duas informações:o modelo e a base onde a aeronave está. Crie um métododo chamado designar_piloto que deverá conter o nome do 
# piloto. Por regra, o primeiro piloto será considerado o piloto principal e o segundo seu co-piloto. Depois de informados os dois 
# nomes, não poderá ser inserido mais nenhum nome. Crie um método rebasear_aeronave que receberá como parâmetro o nome da base parra 
# onde a aeronave deverá ser enviada. Antes de registrar é necessário validar se dois pilotos foram designados para a aeronave, e 
# somente se ambos tiverem sido designados, registrar o rebaseamento com a data e hora da movimentação. Sobrescreva o método
# __str__ da classe para imprimir o seguinte conteúdo
# Jato: <nome da aeronave>
# Base inicial: <nome da base de origem>
# Piloto: <nome dos pilotos designados>
# Histórico de transferências: <listagem das bases pelas quais a aeronave passou mostrando a data, hora e base>

from classe9 import JatoMilitar1Lugar
class JatoMilitar2Lugares(JatoMilitar1Lugar):

    def designar_piloto(self, nome_piloto, nome_co_piloto):
        self.nome_piloto = nome_piloto
        self.nome_co_piloto = nome_co_piloto

    def __str__(self):
        return f'(Jato:<{self.modelo}>\n Base inicial: <{self.base}> \n Piloto: <{self.nome_piloto, self.nome_co_piloto}> \n Histórico de tranferências: < {self.destino}> )'
    


aviao = JatoMilitar2Lugares('f250', 'Londres')
aviao.designar_piloto('Daniel', 'Sheila')
aviao.rebasear_aeronave('EUA')
aviao.rebasear_aeronave('Brasil')
aviao.rebasear_aeronave('México')
print(aviao)
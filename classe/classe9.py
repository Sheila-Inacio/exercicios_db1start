# Crie uma classe que representará uma aeronave militar com o nome JatoMilitar1Lugar. O método construtor deverá receber duas 
# informações iniciais:o modelo e a base onde a aeronave está. Crie um método designar_piloto que deverá receber o nome do piloto
# como parâmetro. Crie um método rebasear_aeronave que deverá receber de parâmetro o nome da base para onde a aeronave deverá ser 
# enviada. Antes de registrar, é necessário validar se o piloto foi designado para a aeronave e somente se houver piloto, registrar
# a informação de rebaseamento, a data e hora que a movimentação foi realizada deverá ser registrada também. Sobrescreva o 
# métod __str__ da classe, para imprimir o seguinte conteúdo:
# Jato: <nome da aeronave>
# Base inicial: <nome da base de origem>
# Piloto: <nome do piloto designado>
# Histórico de transferências: <listagem das bases pelas quais a aeronave passou mostrando a data, hora e base>

import datetime
import time

class JatoMilitar1Lugar:
    def __init__(self, modelo, base):
        self.modelo = modelo
        self.base = base
        self.nome_piloto = ''
        self.destino = []

    def designar_piloto(self, nome_piloto):
        self.nome_piloto = nome_piloto

    def rebasear_aeronave(self, destino):
        if self.nome_piloto != '':
            self.destino.append(destino + ' - ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            time.sleep(2)
        else:
            print("Piloto não designado.")
    def __str__(self):
        return f'(Jato:<{self.modelo}>\n Base inicial: <{self.base}> \n Piloto: <{self.nome_piloto}> \n Histórico de tranferências: < {self.destino}> )'
    
 
# aviao = JatoMilitar1Lugar('f250', 'Londres')
# aviao.designar_piloto('Daniel')
# aviao.rebasear_aeronave('EUA')
# aviao.rebasear_aeronave('Brasil')
# aviao.rebasear_aeronave('México')
# print(aviao)
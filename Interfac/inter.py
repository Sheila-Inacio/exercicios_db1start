from abc import ABC, abstractmethod

# Definindo a interface Veiculo
class Veiculo(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def buzinar(self):
        pass

# Classe que implementa a interface Veiculo para Carros
class Carro(Veiculo):

    def ligar(self):
        print("Carro ligado")

    def desligar(self):
        print("Carro desligado")

    def acelerar(self):
        print("Carro acelerando")

    def buzinar(self):
        print("Carro Buzinando")

# Classe que implementa a interface Veiculo para Motos
class Moto(Veiculo):

    def ligar(self):
        print("Moto ligada")

    def desligar(self):
        print("Moto desligada")

    def acelerar(self):
        print("Moto acelerando")

    def buzinar(self):
        print("Moto buzinando")

# Função para operar um veículo
def operar_veiculo(veiculo: Veiculo):
    veiculo.ligar()
    veiculo.acelerar()
    veiculo.desligar()
    veiculo.buzinar()

# Criando instâncias de Carro e Moto
carro = Carro()
moto = Moto()

# Operando os veículos
operar_veiculo(carro)
operar_veiculo(moto)
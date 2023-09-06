class Car: 

    def __init__(self, marca: str, modelo: str, ano: int, consumo: float): 
        self.marca = marca 
        self.modelo = modelo 
        self.ano = ano 
        self.consumo = consumo 
        self.combustivel = 0 
        self.kilometragem = 0 

    def abastecer(self, qtde: float) -> bool: 
        if self.__validar_tanque(qtde): 
            self.combustivel += qtde 
            return True 
        return False       

    def percorrer_percurso(self, distancia: float): 
        self.kilometragem += distancia 
        self.__consumir_combustivel(distancia) 
 
    def __validar_tanque(self, qtde: float): 
        return self.combustivel + qtde > 50 
  
    def __consumir_combustivel(self, distancia: float): 
        consumo = distancia / self.consumo 
        self.combustivel -= consumo 
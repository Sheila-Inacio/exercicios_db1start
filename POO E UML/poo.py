class ExemploA: 
    def calcular()-> int: #A
    def verificar(x:int, y:int)-> boolean:#B
    def tratarEntradas(s: String):   #C
  
class ExemploB (ExemploA):
    def executarCalculo() -> double: #D
    def verificar(x: double)-> boolean:#E
    def verificar(x:int, y:int)-> boolean:#F
    def tratarEntradas(x: double): #G
        
class ExemploC (ExemploA):
    def processar()-> String:#H
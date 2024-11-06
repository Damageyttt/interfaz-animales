from .interfaces.Respirar import RespirAble
from .interfaces.Terrestre import TerrestreAble

class Elefante(RespirAble, TerrestreAble):
    
    def respirar(self):
        print("El elefante respira")
        
    def desplazar(self):
        print("El elefante se desplaza")
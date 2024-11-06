from .interfaces.Volar import VolarAble
from .interfaces.Respirar import RespirAble
from .interfaces.Terrestre import TerrestreAble
from .interfaces.Nadar import NadAble

class Pato(VolarAble, RespirAble, NadAble, TerrestreAble):
    
    def volar(self):
        print("El pato vuela")
        
    def respirar(self):
        print("El pato respira")
        
    def nadar(self):
        print("El pato nada")
        
    def desplazar(self):
        print("El pato se desplaza")
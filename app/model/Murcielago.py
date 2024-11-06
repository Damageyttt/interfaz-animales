from .interfaces.Volar import VolarAble
from .interfaces.Respirar import RespirAble

class Murcielago(VolarAble, RespirAble):
    
    def volar(self):
        print("El murciélago vuela")
        
    def respirar(self):
        print("El murciélago respira")
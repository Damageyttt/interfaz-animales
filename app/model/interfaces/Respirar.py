from abc import ABC, abstractmethod

class RespirAble(ABC):
    
    @abstractmethod
    def respirar(self):
        pass
from abc import ABC, abstractmethod

class EntidadBase(ABC):

    @abstractmethod
    def obtener_id(self):
        pass

    @abstractmethod
    def validar(self):
        pass

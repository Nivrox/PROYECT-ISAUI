from abc import ABC, abstractmethod

class RepositorioBase(ABC):

    @abstractmethod
    def guardar(self, entidad):
        pass

    @abstractmethod
    def modificar(self, entidad):
        pass

    @abstractmethod
    def eliminar(self, id_entidad):
        pass

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id_entidad):
        pass

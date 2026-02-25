from Modelo.Entidad_base import EntidadBase

class Producto(EntidadBase):
    def __init__(self, id=None, nombre=None, precio=None):
        super().__init__(id)
        self.nombre = nombre
        self.precio = precio

    def obtener_tipo(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
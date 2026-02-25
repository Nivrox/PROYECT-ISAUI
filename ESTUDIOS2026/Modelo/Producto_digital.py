from Modelo.Producto import Producto

class ProductoDigital(Producto):
    def __init__(self, id=None, nombre=None, precio=None, tamaño_archivo=None):
        super().__init__(id, nombre, precio)
        self.tamaño_archivo = tamaño_archivo

    def obtener_tipo(self):
        return "digital"
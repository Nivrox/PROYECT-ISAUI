from Modelo.Producto import Producto

class ProductoFisico(Producto):
    def __init__(self, id=None, nombre=None, precio=None, peso=None):
        super().__init__(id, nombre, precio)
        self.peso = peso

    def obtener_tipo(self):
        return "fisico"
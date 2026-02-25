from Persistencia.Repositorio_producto import RepositorioProducto
from Modelo.Producto_digital import ProductoDigital
from Modelo.Producto_fisico import ProductoFisico

class ServicioProducto:

    @staticmethod
    def validar(nombre, precio):
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")

        try:
            precio = float(precio)
        except ValueError:
            raise ValueError("El precio debe ser numérico")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        return True

    @staticmethod
    def crear_producto(tipo, nombre, precio, atributo):
        ServicioProducto.validar(nombre, precio)

        if tipo == "digital":
            producto = ProductoDigital(None, nombre, float(precio), atributo)
        else:
            producto = ProductoFisico(None, nombre, float(precio), atributo)

        RepositorioProducto.guardar(producto)

    @staticmethod
    def obtener_productos():
        return RepositorioProducto.listar()
    

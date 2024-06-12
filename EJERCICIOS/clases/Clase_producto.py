class Producto:
    def __init__(self, nombre_prod, cantidad, precio):
        self.nombre_prod = nombre_prod
        self.cantidad = cantidad
        self.precio = precio
    def getnombreProd(self):
        return self.nombre_prod
    def getcantidad(self):
        return self.cantidad
    def getprecio(self):
        return self.precio
  
    def mostrarInfoProducto(self):
        print ("\n el producto ingresado fue: ", str(self.nombre_prod) + "\n cantidad: ", str(self.cantidad) + 
            "\n precio: ", str(self.precio))
        return self.nombre_prod, self.cantidad, self.precio

resultado = Producto("secadora de pelo", 3, "$15000")
resultado.mostrarInfoProducto()

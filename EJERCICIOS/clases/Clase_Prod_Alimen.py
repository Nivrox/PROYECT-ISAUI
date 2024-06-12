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

class Alimento(Producto):
        def __init__(self, nombre, cantidad, precio, fecha_expiracion):
            super().__init__(nombre, cantidad, precio)
            self.fecha_expiracion = fecha_expiracion
            self.nombre_aliment = nombre
        
        def getfechaDeExpiracion(self):
            return self.fecha_expiracion
        
        def mostrarInfoProducto(self):
            super().mostrarInfoProducto()
            print (" expira: ", str(self.getfechaDeExpiracion()))

respuesta = Alimento ("arroz", 3, "$1000", "12/03/24")
respuesta.mostrarInfoProducto()

class Producto:
    def __init__(self, nombre , cantidad, precio):
        self.nombre_prod = nombre
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
class Electronico(Producto):

        def __init__(self, nombre, cantidad, precio, marca, modelo,):
            super().__init__(nombre, cantidad, precio)
            self.marca = marca
            self.modelo = modelo
            self.nombre = nombre
            self.cantidad = cantidad
        def getmarca(self):
            return self.marca
        def getmodelo(self):
            return self.modelo
        def getnombre (self):
            return self.nombre
        def getcantidad (self):
            return self.cantidad 
        def mostrarInfoProducto(self):
            super().mostrarInfoProducto()
            print (" la marca de tu producto electronico es: ", str(self.getmarca()) 
                   +"\n y su modelo es: ", str (self.getmodelo()))
            
respuesta = Electronico ("Smartphone", 3, "$20000", "Samsung", "galaxy s3")
respuesta.mostrarInfoProducto()

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
    def notificacion (self):
        if self.cantidad >= 10:
            print ("Parece que tienes muchos!")
    def mostrarInfoProducto(self):
        print ("\n el producto ingresado fue: ", str(self.nombre_prod) + "\n cantidad: ", str(self.cantidad) + 
            "\n precio: ", str(self.precio))
        return self.nombre_prod, self.cantidad, self.precio
    class Electronico:

        def __init__(self, nombre, marca, modelo, cantidad):
            self.marca = marca
            self.modelo = modelo
            self.nombre = nombre
            self.cantidad = cantidad
        def ingresar_prod_electronico (self):
            self.nombre = input("ingrese el nombre del producto electronico ")
        def getmarca(self):
            return self.marca
        def getmodelo(self):
            return self.modelo
        
        def mostrarInfoProductoElectronico(self):
            print ("\n la marca de tu producto electronico es: ", str(self.getmarca) 
                   +"\n y su modelo es: ", str (self.getmodelo))
            
    class alimento:
        def __init__(self, fecha_expiracion):
            self.fecha_expiracion = fecha_expiracion
        def getfechaDeExpiracion(self):
            return self.fecha_expiracion


nombreProd = input ("ingrese el nombre del producto:")
cantidad = input ("ingrese la cantidad: ")
precio = input ("ingrese el precio: ")
alimento = input ("ingrese un alimento")


respuesta = Producto(nombreProd,cantidad, precio)
respuesta.mostrarInfoProducto()

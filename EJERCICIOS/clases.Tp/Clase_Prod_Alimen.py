#Creamos La Clase Producto Con sus Metodos y Atributos
class Producto:
    #Le Damos Un valor Respectivo a cada Self Para Que Se Interconecten
    def __init__(self, nombre_prod, cantidad, precio):
        self.nombre_prod = nombre_prod
        self.cantidad = cantidad
        self.precio = precio
    #Hacemos funciones para acceder a la informacion dentro de cada self 
    def getNombreProd(self):
    
        return self.nombre_prod
    
    def getCantidad(self):
    
        return self.cantidad
    
    def getPrecio(self):
    
        return self.precio

    def mostrarInfoProducto(self):
        print ("\n el producto ingresado fue: ", str(self.nombre_prod) + "\n cantidad: ", str(self.cantidad) + 
            "\n precio: ", str(self.precio))
        return self.nombre_prod, self.cantidad, self.precio
#Creamos Una Clase Heredada Llamada 'Alimento' Con un Atributo Extra
class Alimento(Producto):
        #Le Damos Un valor Respectivo a cada Self Para Que Se Interconecten
        def __init__(self, nombre, cantidad, precio, fecha_expiracion):

            #Usamos super() para Traer los Atributos de la Clase Madre Hacia Nuestra Clase Hija 
            super().__init__(nombre, cantidad, precio)

            self.fecha_expiracion = fecha_expiracion
            self.nombre_aliment = nombre

        #Hacemos funciones para acceder a la informacion dentro de cada self 
        
        def getFechaDeExpiracion(self):
            return self.fecha_expiracion
        
        #Definimos una Funcion Para Mostrar La Informacion Dentro De La Clase Madre y la Clase Heredada
        def mostrarInfoProducto(self):
            #Usamos super() para Mostrar La Informacion De La Clase Madre Junto a La clase Hija 
            super().mostrarInfoProducto()
            #Llamamos a Cada self. Mediante get para Acceder a la Informacion y Mostrarla Mediante un print
            print (" expira: ", str(self.getFechaDeExpiracion()))

#Creamos Una Instancia Para Darle Valores a los Atributos de 'Electronico' y Producto, y luego los mostramos
respuesta = Alimento ("arroz", 5, "$1000", "12/03/24")
respuesta.mostrarInfoProducto()
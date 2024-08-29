#Creamos La Clase Producto Con sus Metodos y Atributos
class Producto:
    #Le Damos Un valor Respectivo a cada Self Para Que Se Interconecten
    def __init__(self, nombre_prod, cantidad, precio):
        self.nombre_prod = nombre_prod
        self.cantidad = cantidad
        self.precio = precio
    
    def getNombreProd(self):
    
        return self.nombre_prod
    
    def getCantidad(self):
    
        return self.cantidad
    
    def getPrecio(self):
    
        return self.precio
        #creamos una instancia para mostrar la informacion de los productos ingresados
    def mostrarInfoProducto(self):
        print ("\n el producto ingresado fue: ", str(self.getNombreProd()) + "\n cantidad: ", str(self.getCantidad()) + 
            "\n precio: ", str(self.getPrecio()))
        return self.nombre_prod, self.cantidad, self.precio


#Generamos Una instancia Para darle valor a los Atributos
resultado = Producto("secadora de pelo", 3, "$15000")
#Los Mostramos La Informacion Dentro De La Clase Producto
resultado.mostrarInfoProducto()

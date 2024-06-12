#Crear un programa que permita la existencia de la clase Vehiculo,
#capaz de procesar la información básica de los vehículos de un concesionario. Suponga
#que los atributos de un vehículo son: (ver paddlet)

class Vehiculo: #crear nuestra CLASE PADRE
    def __init__(self, marca, anio, patente,color) : #CONSTRUCTOR
      #self. (atributo) = (parametro)
       self.marca = marca
       self.anio = anio
       self.patente = patente
       self.color = color
   
    #metodos/funciones de acceso a los atributos
    def getPatente(self):
       return self.patente
    #es lo mismo para cada atributo que posea el objeto
    def getColor(self):
       return self.color
    
    def getMarca(self):
       return self.marca
    
    def getAnio(self):
       return self.anio
    
    #metodo para mostrar la info del objeto en consola 
    def mostrarInfoVehiculo(self):
         print ("\n Los datos ingresados son: " + "\n" "\n Patente: "+ str(self.getPatente())
                +"\n marca: ", str(self.marca) + "\n año: ", str(self.anio) + "\n color: ", str(self.color))
        
       #agregar el resto de los get que hemos creado según los atributos tiene nuestro objeto vehiculo

    

patente = input("Ingrese la Patente: ")
marca = input("Ingresame la marca: ")
anio = input("Ingresame el anio: ")
color = input("Ingresame el color: ")

    #solicitar el resto de atributos

e= Vehiculo( marca , anio, patente, color) #añadir todos los parametros que espera mi metodo(funcion)
e.mostrarInfoVehiculo()
from conexion import *

class Ppersonas:
    def mostrarPersonas():
        try:
            cone= CConexion.ConexionBd()
            cursor = cone.cursor()
            cursor.execute ("SELECT Nombres, Apellidos, Sexo, Dni FROM Personas;")
            miResultado = cursor.fetchall()

            #La variable valores tiene que ser una tupla 
            #Como minima expresion es: (valor,) La coma hace que sea una tupla
            #Las tuplas son listas inmutables (No se pueden modificar)
            cone.commit()
            print (cursor.rowcount, "Datos Insertados Correctamente")
            cone.close()
            return miResultado
        except mysql.connector.Error as error:
            print("Error al mostrar datos: {}".format(error))
            return False
        
    def ingresarPersonas(nombres, apellidos, sexo, dni):
        try:
            cone= CConexion.ConexionBd()
            cursor = cone.cursor()
            sql = "INSERT INTO Personas ( Nombres, Apellidos, Sexo, Dni) VALUES (%s, %s, %s, %s)"

            #La variable valores tiene que ser una tupla 
            #Como minima expresion es: (valor,) La coma hace que sea una tupla
            #Las tuplas son listas inmutables (No se pueden modificar)

            valores = (nombres, apellidos, sexo, dni)
            cursor.execute(sql,valores)
            cone.commit()
            print (cursor.rowcount, "Datos Insertados Correctamente")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error al insertar datos: {}".format(error))
            return False
        
    def modificarPersonas(nombres, apellidos, sexo, dni, id):
        
        try:
            cone= CConexion.ConexionBd()
            cursor = cone.cursor()
            sql = "UPDATE Personas SET Nombres = %s, Apellidos = %s, Sexo = %s, dni = %s, WHERE id = %s;"

            #La variable valores tiene que ser una tupla 
            #Como minima expresion es: (valor,) La coma hace que sea una tupla
            #Las tuplas son listas inmutables (No se pueden modificar)

            valores = (nombres, apellidos, sexo, dni, id)
            cursor.execute(sql,valores)
            cone.commit()
            print (cursor.rowcount, "Datos Modificados Correctamente")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error al modificar datos: {}".format(error))
            return False
        
    def eliminarPersonas(dni):
        
        try:
            cone= CConexion.ConexionBd()
            cursor = cone.cursor()
            sql = "delete from Personas where Personas.dni = %s;"

            #La variable valores tiene que ser una tupla 
            #Como minima expresion es: (valor,) La coma hace que sea una tupla
            #Las tuplas son listas inmutables (No se pueden modificar)

            valores = (dni,)
            cursor.execute(sql,valores)
            cone.commit()
            print (cursor.rowcount, "Datos Eliminados Correctamente")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error al eliminar datos: {}".format(error))
            return False
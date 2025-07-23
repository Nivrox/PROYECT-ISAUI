import mysql.connector

class CConexion:
    def ConexionBd():
        try:
            conexion = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='',
                database='Personasdb',
                port=3306
            )
            print ("Conexion Exitosa")
            return conexion
        except mysql.connector.Error as error:
            print("Error al conectar a la base de datos: {}".format(error))
            return conexion
            
        
    ConexionBd()
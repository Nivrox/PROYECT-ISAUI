import mysql.connector

class Conexion:

    @staticmethod
    def obtener_conexion():
        try:
            conexion = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="sistema_abm",
                port=3306
            )
            return conexion
        except mysql.connector.Error as error:
            raise Exception(f"Error de conexión: {error}")

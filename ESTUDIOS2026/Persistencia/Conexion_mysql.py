import mysql.connector

class ConexionMySQL:

    @staticmethod
    def obtener_conexion():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="abm_productos"
        )
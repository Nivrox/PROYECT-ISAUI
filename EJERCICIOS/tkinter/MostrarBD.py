import mysql.connector
from mysql.connector import Error

def mostrar_datos():
    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(
            host='localhost',         # Cambia 'localhost' por tu servidor
            database='isaui',     # Nombre de la base de datos
            user='root',           # Usuario de MySQL
            password='bru455no'     # Contraseña del usuario
        )

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")

            # Crear cursor para ejecutar consultas
            cursor = conexion.cursor()

            # Consulta SQL para seleccionar los datos de una tabla
            consulta = "SELECT * FROM personas ;"  # Cambia 'nombre_tabla' por el nombre de tu tabla

            # Ejecutar la consulta
            cursor.execute(consulta)

            # Obtener todos los registros
            registros = cursor.fetchall()

            # Mostrar los registros obtenidos
            print("Datos almacenados en la tabla:")
            for registro in registros:
                print(registro)  # Cada 'registro' es una tupla que representa una fila en la tabla

    except Error as e:
        print("Error al conectar a MySQL:", e)

    finally:
        # Cerrar la conexión
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("Conexión a MySQL cerrada")

# Llamar a la función para mostrar los datos
mostrar_datos()


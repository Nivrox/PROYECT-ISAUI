from ConexionBDBiblioteca import *   
class Prestamos:
    
    def mostrarPrestamos():
        try: 
            conexion = Cconexion.conexion()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT 
                    s.Nombre,
                    s.Apellido,
                    s.DNI,
                    l.isbn,
                    p.fecha_devolucion,
                    p.estado_prestamo
                    
                FROM 
                    prestamos p
                JOIN 
                    socios s ON p.id_socios = s.id_socios
                JOIN 
                    libros l ON p.id_libros = l.id_libros;
            """)
            conexion.commit
            miresultado = cursor.fetchall()
            conexion.close()
            return miresultado
        except mysql.connector.Error as error:
            print("Error de muestreo {}".format(error))
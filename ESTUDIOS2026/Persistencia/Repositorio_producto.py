from Persistencia.Conexion_mysql import ConexionMySQL
from Modelo.Producto_digital import ProductoDigital
from Modelo.Producto_fisico import ProductoFisico

class RepositorioProducto:

    @staticmethod
    def guardar(producto):
        conexion = ConexionMySQL.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO productos (nombre, precio, tipo, atributo_extra)
        VALUES (%s, %s, %s, %s)
        """

        if producto.obtener_tipo() == "digital":
            atributo = producto.tamaño_archivo
        else:
            atributo = producto.peso

        cursor.execute(sql, (
            producto.nombre,
            producto.precio,
            producto.obtener_tipo(),
            atributo
        ))

        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def listar():
        conexion = ConexionMySQL.obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("SELECT id, nombre, precio, tipo, atributo_extra FROM productos")
        registros = cursor.fetchall()

        productos = []

        for id, nombre, precio, tipo, atributo in registros:
            if tipo == "digital":
                producto = ProductoDigital(id, nombre, precio, atributo)
            else:
                producto = ProductoFisico(id, nombre, precio, atributo)

            productos.append(producto)

        cursor.close()
        conexion.close()

        return productos
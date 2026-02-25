from persistencia.conexion import Conexion
from persistencia.repositorio_base import RepositorioBase
from modelo.cliente import Cliente
from persistencia.persona_dao import PersonaDAO

class ClienteDAO(RepositorioBase):

    def guardar(self, entidad):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        if entidad.id_persona is None:
            sql_persona = "INSERT INTO personas (dni, nombres, apellidos, sexo) VALUES (%s, %s, %s, %s)"
            valores_persona = (entidad.dni, entidad.nombres, entidad.apellidos, entidad.sexo)
            cursor.execute(sql_persona, valores_persona)
            conexion.commit()
            entidad._id_persona = cursor.lastrowid

        sql_cliente = "INSERT INTO clientes (id_persona, fecha_alta, estado) VALUES (%s, %s, %s)"
        valores_cliente = (entidad.id_persona, entidad.fecha_alta, entidad.estado)
        cursor.execute(sql_cliente, valores_cliente)
        conexion.commit()

        entidad._id_cliente = cursor.lastrowid
        conexion.close()
        return entidad

    def modificar(self, entidad):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql_persona = "UPDATE personas SET dni=%s, nombres=%s, apellidos=%s, sexo=%s WHERE id_persona=%s"
        valores_persona = (entidad.dni, entidad.nombres, entidad.apellidos, entidad.sexo, entidad.id_persona)
        cursor.execute(sql_persona, valores_persona)

        sql_cliente = "UPDATE clientes SET estado=%s WHERE id_cliente=%s"
        valores_cliente = (entidad.estado, entidad.id_cliente)
        cursor.execute(sql_cliente, valores_cliente)

        conexion.commit()
        conexion.close()

    def eliminar(self, id_entidad):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql_cliente = "DELETE FROM clientes WHERE id_persona=%s"
        cursor.execute(sql_cliente, (id_entidad,))

        sql_persona = "DELETE FROM personas WHERE id_persona=%s"
        cursor.execute(sql_persona, (id_entidad,))

        conexion.commit()
        conexion.close()

    def listar(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT p.id_persona, c.id_cliente, p.dni, p.nombres, p.apellidos, p.sexo, c.fecha_alta, c.estado
        FROM personas p
        INNER JOIN clientes c ON p.id_persona = c.id_persona
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conexion.close()

        lista_clientes = []

        for fila in resultados:
            cliente = Cliente(
                dni=fila[2],
                nombres=fila[3],
                apellidos=fila[4],
                sexo=fila[5],
                fecha_alta=fila[6],
                estado=fila[7],
                id_persona=fila[0],
                id_cliente=fila[1]
            )
            lista_clientes.append(cliente)

        return lista_clientes

    def obtener_por_id(self, id_entidad):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
        SELECT p.id_persona, c.id_cliente, p.dni, p.nombres, p.apellidos, p.sexo, c.fecha_alta, c.estado
        FROM personas p
        INNER JOIN clientes c ON p.id_persona = c.id_persona
        WHERE c.id_cliente=%s
        """
        cursor.execute(sql, (id_entidad,))
        fila = cursor.fetchone()
        conexion.close()

        if fila:
            return Cliente(
                dni=fila[2],
                nombres=fila[3],
                apellidos=fila[4],
                sexo=fila[5],
                fecha_alta=fila[6],
                estado=fila[7],
                id_persona=fila[0],
                id_cliente=fila[1]
            )

        return None
    
    def buscar_por_persona(self, id_persona):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM clientes WHERE id_persona = %s", (id_persona,))
        resultado = cursor.fetchone()

        cursor.close()
        conexion.close()
        return resultado
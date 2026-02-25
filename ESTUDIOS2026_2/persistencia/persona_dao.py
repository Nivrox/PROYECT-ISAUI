from persistencia.conexion import Conexion
from persistencia.repositorio_base import RepositorioBase
from modelo.persona import Persona

class PersonaDAO(RepositorioBase):

    def guardar(self, entidad):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO personas (dni, nombres, apellidos, sexo) VALUES (%s, %s, %s, %s)"
        valores = (entidad.dni, entidad.nombres, entidad.apellidos, entidad.sexo)
        cursor.execute(sql, valores)
        conexion.commit()
        entidad._id_persona = cursor.lastrowid
        conexion.close()
        return entidad

    def modificar(self, entidad):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE personas SET dni=%s, nombres=%s, apellidos=%s, sexo=%s WHERE id_persona=%s"
        valores = (entidad.dni, entidad.nombres, entidad.apellidos, entidad.sexo, entidad.id_persona)
        cursor.execute(sql, valores)
        conexion.commit()
        conexion.close()

    def eliminar(self, id_entidad):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM personas WHERE id_persona=%s"
        cursor.execute(sql, (id_entidad,))
        conexion.commit()
        conexion.close()

    def listar(self):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = "SELECT id_persona, dni, nombres, apellidos, sexo FROM personas"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        conexion.close()
        lista_personas = []
        for fila in resultados:
            persona = Persona(
                dni=fila[1],
                nombres=fila[2],
                apellidos=fila[3],
                sexo=fila[4],
                id_persona=fila[0]
            )
            lista_personas.append(persona)
        return lista_personas

    def obtener_por_id(self, id_entidad):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()
        sql = "SELECT id_persona, dni, nombres, apellidos, sexo FROM personas WHERE id_persona=%s"
        cursor.execute(sql, (id_entidad,))
        fila = cursor.fetchone()
        conexion.close()
        if fila:
            return Persona(
                dni=fila[1],
                nombres=fila[2],
                apellidos=fila[3],
                sexo=fila[4],
                id_persona=fila[0]
            )
        return None
    
    def buscar_por_dni(self, dni):
        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM personas WHERE dni = %s", (dni,))
        resultado = cursor.fetchone()

        cursor.close()
        return resultado
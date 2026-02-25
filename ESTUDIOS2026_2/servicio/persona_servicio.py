from persistencia.persona_dao import PersonaDAO
from modelo.persona import Persona

class PersonaServicio:

    def __init__(self):
        self._persona_dao = PersonaDAO()

    def crear_persona(self, dni, nombres, apellidos, sexo):
        persona = Persona(dni=dni, nombres=nombres, apellidos=apellidos, sexo=sexo)

        if not persona.validar():
            raise ValueError("Datos inválidos")
        
        existente = self._persona_dao.buscar_por_dni(dni)
        if existente:
            raise ValueError("El DNI ya está registrado")

        return self._persona_dao.guardar(persona)

    def actualizar_persona(self, id_persona, dni, nombres, apellidos, sexo):
        persona = Persona(dni=dni, nombres=nombres, apellidos=apellidos, sexo=sexo, id_persona=id_persona)

        if not persona.validar():
            raise ValueError("Datos inválidos")

        self._persona_dao.modificar(persona)

    def eliminar_persona(self, id_persona):
        self._persona_dao.eliminar(id_persona)

    def listar_personas(self):
        return self._persona_dao.listar()

    def obtener_persona(self, id_persona):
        return self._persona_dao.obtener_por_id(id_persona)

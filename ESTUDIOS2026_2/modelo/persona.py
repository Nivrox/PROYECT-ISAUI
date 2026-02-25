import re
from modelo.entidad_base import EntidadBase

class Persona(EntidadBase):

    def __init__(self, dni, nombres, apellidos, sexo, id_persona=None):
        self._id_persona = id_persona
        self.dni = dni
        self.nombres = nombres
        self.apellidos = apellidos
        self.sexo = sexo

    @property
    def id_persona(self):
        return self._id_persona

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, value):
        if not value.isdigit() or len(value) > 10:
            raise ValueError("DNI inválido")
        self._dni = value

    @property
    def nombres(self):
        return self._nombres

    @nombres.setter
    def nombres(self, value):
        patron = r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$"
        if not re.match(patron, value):
            raise ValueError("Nombre inválido")
        self._nombres = value

    @property
    def apellidos(self):
        return self._apellidos

    @apellidos.setter
    def apellidos(self, value):
        patron = r"^[A-Za-zÁÉÍÓÚáéíóúñÑ ]+$"
        if not re.match(patron, value):
            raise ValueError("Apellido inválido")
        self._apellidos = value

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, value):
        if value not in ["Masculino", "Femenino", "Otro"]:
            raise ValueError("Sexo inválido")
        self._sexo = value

    def obtener_id(self):
        return self._id_persona

    def validar(self):
        return True

from datetime import date
from modelo.persona import Persona

class Cliente(Persona):

    def __init__(self, dni, nombres, apellidos, sexo, fecha_alta=None, estado="Activo", id_persona=None, id_cliente=None):
        super().__init__(dni, nombres, apellidos, sexo, id_persona)
        self._fecha_alta = fecha_alta if fecha_alta else date.today()
        self._estado = estado
        self._id_cliente = id_cliente

    @property
    def id_cliente(self):
        return self._id_cliente

    @property
    def fecha_alta(self):
        return self._fecha_alta

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        if value not in ["Activo", "Inactivo"]:
            raise ValueError("Estado inválido")
        self._estado = value

    def validar(self):
        if not super().validar():
            return False

        if self._estado not in ["Activo", "Inactivo"]:
            return False

        return True

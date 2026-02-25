from persistencia.cliente_dao import ClienteDAO
from modelo.cliente import Cliente
from modelo.persona import Persona
from persistencia.persona_dao import PersonaDAO


class ClienteServicio:

    def __init__(self):
        self._persona_dao = PersonaDAO()
        self._cliente_dao = ClienteDAO()

    def crear_cliente(self, dni, nombres, apellidos, sexo, estado):

    
        persona_existente = self._persona_dao.buscar_por_dni(dni)

        if not persona_existente:
            raise ValueError("No existe una persona con ese DNI. Primero debe crear la persona.")

        id_persona = persona_existente["id_persona"]

        cliente_existente = self._cliente_dao.buscar_por_persona(id_persona)

        if cliente_existente:
            raise ValueError("Esta persona ya es cliente.")
        
        cliente = Cliente(
            dni=dni,
            nombres=nombres,
            apellidos=apellidos,
            sexo=sexo,
            estado=estado,
            id_persona=id_persona
        )

        return self._cliente_dao.guardar(cliente)

    def actualizar_cliente(self, id_cliente, dni, nombres, apellidos, sexo, estado):

        
        cliente_existente = self._cliente_dao.obtener_por_id(id_cliente)

        if not cliente_existente:
            raise ValueError("Cliente no encontrado")

        
        cliente_existente.dni = dni
        cliente_existente.nombres = nombres
        cliente_existente.apellidos = apellidos
        cliente_existente.sexo = sexo
        cliente_existente.estado = estado

        if not cliente_existente.validar():
            raise ValueError("Datos inválidos")

        self._cliente_dao.modificar(cliente_existente)


    def eliminar_cliente(self, id_persona):
        self._cliente_dao.eliminar(id_persona)

    def listar_clientes(self):
        return self._cliente_dao.listar()

    def obtener_cliente(self, id_persona):
        return self._cliente_dao.obtener_por_id(id_persona)

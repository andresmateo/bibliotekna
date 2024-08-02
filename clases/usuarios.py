from datetime import datetime

class Usuario:
    def __init__(self, nombre, apellido, documento_id, registro = datetime.now(), bloqueado="NO"):
        self.nombre = nombre
        self.apellido = apellido
        self.documento_id = documento_id
        self.registro = registro # Esta es la fecha de registro del usuario
        self.bloqueado = bloqueado # Este es verdadero o falso

    def actualizar_usuario(self, nombre=None, apellido=None, documento_id=None, bloqueado=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if documento_id:
            self.documento_id = documento_id
        if bloqueado:
            self.bloqueado = bloqueado # Este es año de publicación
        # TODO: Implementar la manera de guardar los cambios realizados en el usuario modificado.
   
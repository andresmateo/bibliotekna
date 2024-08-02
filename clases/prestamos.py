from datetime import datetime

class Prestamo:
    def __init__(self, documento_id, libro, fecha=datetime.now(), retorno="-"):
        self.documento_id = documento_id
        self.libro = libro
        self.fecha = fecha # Fecha en la que se prestó el libro
        self.retorno = retorno # Fecha en la que retorna el libro

    def actualizar_prestamo(self, retorno=datetime.now()):
        if retorno:
            self.retorno=retorno
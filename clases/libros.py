
class Libro:
    def __init__(self, tematica, titulo, autor, editorial, publicacion, ejemplar, prestado="NO"):
        self.tematica = tematica # Es la categoría a la que pertenece EJ. Historia, Geografía, Cristianismo
        self.titulo = titulo
        self.autor = autor
        self.editorial = editorial
        self.publicacion = publicacion # Este es año de publicación
        self.ejemplar = ejemplar # Este es número de ejemplar idéntico con el mismo titulo y autor
        self.prestado = prestado

    def actualizar_libro(self, tematica=None, titulo=None, autor=None, editorial=None, publicacion=None, ejemplar=None, prestado=None):
        if tematica:
            self.tematica = tematica
        if titulo:
            self.titulo = titulo
        if autor:
            self.autor = autor
        if editorial:
            self.editorial = editorial
        if publicacion:
            self.publicacion = publicacion # Este es año de publicación
        if ejemplar:
            self.ejemplar = ejemplar # Este es número de ejemplar de los libros idéntico con el mismo titulo y autor
        if prestado:
            self.prestado = prestado
        # TODO: Implementar la manera de guardar los cambios realizados en el libro modificado.
    
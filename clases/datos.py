import csv
import os.path

from clases.libros import Libro
from clases.usuarios import Usuario
from clases.prestamos import Prestamo

# ===LIBROS=============================================================================

def guardar_libros(libros):
    # Escribir en el archivo
    with open("libros.csv", "w", newline="") as archivo_libros:
        escritor = csv.writer(archivo_libros)
        escritor.writerow(["Temática","Título","Autor","Editorial","Año_Publicación","Ejemplar","Prestado"])
        for libro in libros:
            escritor.writerow([libro.tematica,libro.titulo,libro.autor,libro.editorial,libro.publicacion,libro.ejemplar,libro.prestado])
            #print([libro.tematica, libro.titulo, libro.autor, libro.editorial, libro.publicacion, libro.ejemplar])

def leer_libros():
    libros = []
    nombre_archivo = "libros.csv"

    # Verificar que exista el archivo
    if os.path.exists(nombre_archivo):
        # Leer el archivo
        with open(nombre_archivo, "r") as archivo_libros:
            lector = csv.reader(archivo_libros)
            for fila in lector:
                tematica = fila[0]
                titulo = fila[1]
                autor = fila[2]
                editorial = fila[3]
                publicacion = fila[4]
                ejemplar = fila[5]
                prestado = fila[6]
                libro = Libro(tematica, titulo, autor, editorial, publicacion, ejemplar,prestado)
                libros.append(libro)
        del libros[0] # Eliminar el encabezado del archivo para que no se duplique al guardar
        return libros
    else:
        print(f"El archivo '{nombre_archivo}' no existe. Puede empezar a llenar los datos de los libros ahora.")
        return []


# ===USUARIOS=============================================================================

def guardar_usuarios(usuarios):
    # Escribir en el archivo
    with open("usuarios.csv", "w", newline="") as archivo_usuarios:
        escritor = csv.writer(archivo_usuarios)
        escritor.writerow(["Nombre","Apellido","DocumentoID","Registro","Bloqueado"])
        for usuario in usuarios:
            escritor.writerow([usuario.nombre,usuario.apellido,usuario.documento_id,usuario.registro,usuario.bloqueado])

def leer_usuarios():
    usuarios = []
    nombre_archivo = "usuarios.csv"

    # Verificar que exista el archivo
    if os.path.exists(nombre_archivo):
        # Leer el archivo
        with open(nombre_archivo, "r") as archivo_usuarios:
            lector = csv.reader(archivo_usuarios)
            for fila in lector:
                nombre = fila[0]
                apellido = fila[1]
                documento_id = fila[2]
                registro = fila[3]
                bloqueado = fila[4]
                usuario = Usuario(nombre, apellido, documento_id,registro,bloqueado)
                usuarios.append(usuario)
        
        usuarios.pop(0) # Eliminar el encabezado del archivo para que no se duplique al guardar
        return usuarios
    else:
        print(f"El archivo '{nombre_archivo}' no existe. Puede empezar a llenar los datos de los usuarios ahora.")
        return []

# ===PRESTAMOS==============================================================================

def guardar_prestamos(prestamos):
    # Escribir en el archivo
    with open("prestamos.csv", "w", newline="") as archivo_prestamos:
        escritor = csv.writer(archivo_prestamos)
        escritor.writerow(["DocumentoID","Libro","Fecha","Retorno"])
        for prestamo in prestamos:
            escritor.writerow([prestamo.documento_id,prestamo.libro,prestamo.fecha,prestamo.retorno])

def leer_prestamos():
    array_prestamos = []
    nombre_archivo = "prestamos.csv"

    # Verificar que exista el archivo
    if os.path.exists(nombre_archivo):
        # Leer el archivo
        with open(nombre_archivo, "r") as archivo_prestamos:
            lector = csv.reader(archivo_prestamos)
            for fila in lector:
                documento_id = fila[0]
                libro=fila[1]
                fecha=fila[2]
                retorno=fila[3]
                prestamo = Prestamo(documento_id, libro, fecha, retorno)
                array_prestamos.append(prestamo)
        
        array_prestamos.pop(0) # Eliminar el encabezado del archivo para que no se duplique al guardar
        return array_prestamos
    else:
        print(f"El archivo '{nombre_archivo}' no existe. Puede empezar a llenar los datos de los préstamos ahora.")
        return []
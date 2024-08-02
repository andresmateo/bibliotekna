from curses.ascii import isalpha, isdigit
from datetime import datetime
from clases import datos
from clases.libros import Libro
from clases.usuarios import Usuario
from clases.prestamos import Prestamo

rojo     ="\033[31m"
verde    ="\033[32m"
amarillo ="\033[33m"
azul     ="\033[34m"
s_c      ="\033[0m" #sin color

# fondos
fr="\033[41m" # Fondo Rojo
fa="\033[43m" # Fondo Amarillo

# ===LIBROS=============================================================================
def registrar_libro():
    tematica = input("Ingrese la temática que trata el libro: ").strip().upper()
    titulo = input("Ingrese el título del libro: ").strip().upper()
    autor = input("Ingrese el autor del libro: ").strip().upper()
    editorial = input("Ingrese la editorial del libro: ").strip().upper()
    publicacion = input("Ingrese el año de la publicación del libro: ").strip().upper() #AÑO DE PUBLICACION
    ejemplar = input("Ingrese el número de ejemplar correspondiente del libro: ").strip()

    nuevo_libro = Libro(tematica, titulo, autor, editorial, publicacion, ejemplar)
    return nuevo_libro

def mostrar_libros(libros):
    print(f"{azul}LIBROS REGISTRADOS:{s_c}")
    print("================================================================================================================")
    for libro in libros:
        si_o_no = f"{rojo}SI{s_c}" if libro.prestado=="SI" else f"{verde}NO{s_c}"
        print(f"{azul}Temática:{s_c} {libro.tematica} {azul}Título:{s_c} {libro.titulo} {azul}Autor:{s_c} {libro.autor} {azul}Editorial:{s_c} {libro.editorial}\n{azul}Publicación:{s_c} {libro.publicacion} {azul}Ejemplar:{s_c} {libro.ejemplar} Prestado?: {si_o_no}")
        print("================================================================================================================")

def mostrar_info_libro(libros):
        buscado = input("Ingresa el título del libro que estás buscando: ").strip().upper()

        for libro in libros:
            if libro.titulo == buscado:
                si_o_no = f"{rojo}SI{s_c}" if libro.prestado=="SI" else f"{verde}NO{s_c}"

                return f"""{azul}DATOS DEL LIBRO:{s_c}\n
                    {azul}Temática:{s_c} {libro.tematica},
                    {azul}Título:{s_c} {libro.titulo},
                    {azul}Autor:{s_c} {libro.autor},
                    {azul}Editorial:{s_c} {libro.editorial},
                    {azul}Año de Publicación:{s_c} {libro.publicacion},
                    {azul}Ejemplar No.:{s_c} {libro.ejemplar},
                    {azul}Prestado?:{s_c} {si_o_no}"""
        
        return f"{fr}No se encontró el libro que buscabas.{s_c}"

def retorno_libro(libros,usuarios,prestamos):
    usuario_buscado = input("Ingrese la ID de la persona que develve el libro: ").strip()
    for usuario in usuarios:
        if usuario.documento_id == usuario_buscado:
            print(f"{fa}LIBROS PEDIDOS POR {usuario.nombre} {usuario.apellido}:{s_c}")
            i=0
            for prestamo in prestamos:
                if prestamo.documento_id == usuario_buscado and prestamo.retorno == "-":
                    i+=1
                    print(f"{i}. {azul}Documento ID:{s_c} {prestamo.documento_id}, {azul}Libro:{s_c} {prestamo.libro}, {azul}Fecha:{s_c} {prestamo.fecha}")
                if i==0:
                    return f"{rojo}No existen libros pendientes de entregar.{s_c}"
                
            libro_buscado = input("Ingrese el nombre del libro que retorna a la biblioteca: ").strip().upper()
            for libro in libros:
                if libro.titulo==libro_buscado:
                    libro.prestado="NO"
                    datos.guardar_libros(libros)
                    #prestamos[prestamos.index(prestamo)]
                    for prestamo in prestamos:
                        if prestamo.documento_id == usuario_buscado and prestamo.libro == libro_buscado and prestamo.retorno=="-":
                            prestamo.retorno = datetime.now()
                            datos.guardar_prestamos(prestamos)
                            return f"{amarillo}El retorno del libro {libro.titulo} ha sido registrado exitosamente.{s_c}"
            return f"{rojo}El libro seleccionado no se encontró en la lista de prestados.{s_c}"
    return f"{rojo}El usuario seleccionado no se encontró.{s_c}"

# ===USUARIOS=============================================================================
def registrar_usuario():
    nombre = input("Ingrese la nombre del usuario: ").strip().upper()
    apellido = input("Ingrese el apellido del usuario: ").strip().upper()
    documento_id = input("Ingrese el documento de identidad del usuario: ").strip()

    nuevo_usuario = Usuario(nombre, apellido, documento_id)
    return nuevo_usuario

def mostrar_usuarios(usuarios):
    print(f"{azul}USUARIOS REGISTRADOS:{s_c}")
    print("================================================================================================================")
    for usuario in usuarios:
        print(f"{azul}Nombre:{s_c} {usuario.nombre} {azul}Apellido:{s_c} {usuario.apellido} {azul}DocumentoID:{s_c} {usuario.documento_id} {azul}Registro:{s_c} {usuario.registro} {azul}Bloqueado:{s_c} {usuario.bloqueado}")
        print("================================================================================================================")

def mostrar_info_usuarios(usuarios):
        buscado = input("Ingresa el Documento ID del usuario que estás buscando: ").strip()

        for usuario in usuarios:
            if usuario.documento_id == buscado:
                return f"""{azul}DATOS DEL USUARIO:{s_c}\n
                    {azul}Nombre:{s_c} {usuario.nombre},
                    {azul}Apellido:{s_c} {usuario.apellido},
                    {azul}Documento ID:{s_c} {usuario.documento_id},
                    {azul}Fecha de Registro:{s_c} {usuario.registro},
                    {azul}Bloqueado?:{s_c} {usuario.bloqueado}"""

        return f"{fr}No se encontró el usuario que buscabas.{s_c}"
            
# ===PRESTAMOS DE LIBROS====================================================================
def registrar_prestamos(usuarios, libros):
    documento_id = input("Ingrese la ID del usuario: ").strip()
    # TODO: verificar si la cadena contiene solo numeros
    for usuario in usuarios:
        if usuario.documento_id == documento_id:
            libro = input("Ingrese el nombre del libro: ").strip().upper()
            for lib in libros:
                if lib.titulo == libro:
                    nuevo_prestamo = Prestamo(documento_id, libro)
                    lib.actualizar_libro(prestado = "SI")
                    return nuevo_prestamo
                
            print(f"{fr}El libro seleccionado no se encuentra en la biblioteca.{s_c}")
            return None
        
    print(f"{fr}El usuario seleccionado no se encuentra registrado.{s_c}")
    return None

def mostrar_prestamos(prestamos):
    print(f"{azul}PRESTAMOS DE LIBROS REGISTRADOS:{s_c}")
    print("================================================================================================================")
    for prestamo in prestamos:
        print(f"{azul}Documento ID:{s_c} {prestamo.documento_id} {azul}Libro:{s_c} {prestamo.libro} {azul}Fecha:{s_c} {prestamo.fecha} {azul}Retorno:{s_c} {prestamo.retorno}")
        print("================================================================================================================")

def mostrar_info_prestamos(prestamos):
        buscado = input(f"Ingresa el {verde}Documento ID del usuario{s_c} o el {verde}nombre del libro{s_c} que estás buscando: ").strip()

        if isdigit(buscado):
            for prestamo in prestamos:
                if prestamo.documento_id == buscado:
                    return f"""{azul}DATOS DEL PRESTAMO REALIZADO:{s_c}\n
                        {azul}Documento ID:{s_c} {prestamo.documento_id},
                        {azul}Libro:{s_c} {prestamo.libro},
                        {azul}Fecha:{s_c} {prestamo.fecha},
                        {azul}Retorno:{s_c} {prestamo.retorno}"""
        elif isalpha(buscado):
            for prestamo in prestamos:
                if prestamo.libro == buscado:
                    return f"""{azul}DATOS DEL PRESTAMO REALIZADO:{s_c}\n
                        {azul}Documento ID:{s_c} {prestamo.documento_id},
                        {azul}Libro:{s_c} {prestamo.libro},
                        {azul}Fecha:{s_c} {prestamo.fecha},
                        {azul}Retorno:{s_c} {prestamo.retorno}"""

        return f"{fr}No se encontró el usuario que buscabas.{s_c}"

# ===MENÚ DEL SISTEMA===============================================================
def mostrar_menu():
    print("\033[92m\n============================================ \033[0m")
    print("\033[92m --- BIBLIOTEKNA Una biblioteca moderna! --- \033[0m")
    print("\033[92m ---           Menú de gestión           --- \033[0m")
    print("\033[92m============================================ \033[0m")
    print("1. Registrar Libro")
    print("2. Registrar Usuario")
    print("3. Registrar Préstamo de un Libro")
    print("4. Consultar Libros Registrados")
    print("5. Consultar Info de un Libro")
    print("6. Consultar Usuarios Registrados")
    print("7. Consultar Info de un Usuario")
    print("8. Consultar Préstamos Registrados")
    print("9. Registrar la devolución de un libro")
    print("0. Salir")

# ===PRINCIPAL (MAIN)===============================================================
def main():
    libros=datos.leer_libros()
    usuarios=datos.leer_usuarios()
    prestamos =datos.leer_prestamos()

    while True:
         mostrar_menu()
         opcion = input("Selecciona una opción: ")

         match opcion:
            case "0":
                print("¡Gracias por utilizar BiblioTekna!\n¡El sistema se ha cerrado!")
                break
            case "1":
                nuevo_libro = registrar_libro()
                if nuevo_libro:
                    libros.append(nuevo_libro)
                    datos.guardar_libros(libros)
                print(f"{amarillo}¡Libro guardado con éxito!{s_c}")
            case "2":
                nuevo_usuario = registrar_usuario()
                if nuevo_usuario:
                    usuarios.append(nuevo_usuario)
                    datos.guardar_usuarios(usuarios)
                print(f"{amarillo}¡Usuario guardado con éxito!{s_c}")
            case "3":
                nuevo_prestamo = registrar_prestamos(usuarios,libros)
                if nuevo_prestamo:
                    prestamos.append(nuevo_prestamo)
                    datos.guardar_prestamos(prestamos)
                    datos.guardar_libros(libros)
                    print(f"{amarillo}¡Préstamo de libro guardado con éxito!{s_c}")
            case "4":
                mostrar_libros(libros)
            case "5":
                print("================================================================================================================")
                print(mostrar_info_libro(libros))
                print("================================================================================================================")
            case "6":
                mostrar_usuarios(usuarios)
            case "7":
                print("================================================================================================================")
                print(mostrar_info_usuarios(usuarios))
                print("================================================================================================================")
            case "8":
                mostrar_prestamos(prestamos)
            case "9":
                print(retorno_libro(libros,usuarios,prestamos))


if __name__ == "__main__":
    main()
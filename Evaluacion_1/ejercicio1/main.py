# Importa la clase Biblioteca desde la carpeta clases
from clases.biblioteca import Biblioteca

# Función principal: muestra ejemplos de registro, búsqueda y préstamo de libros
def main():
    b = Biblioteca("Biblioteca Central")

    print(b.registrar_libro("El Hombre Invisible", "H. G. Wells", 3))
    print(b.registrar_libro("Soy Leyenda", "Richard Matheson", 2))
    print(b.registrar_libro("El Cielo De Octubre", "Homer Hickam", 1))

    print("\nCATÁLOGO INICIAL:")
    print(*b.mostrar_catalogo(), sep="\n- ")

    print("\nBUSCAR EXISTENTE:")
    libro = b.buscar_libro("Soy Leyenda")
    print(libro.info() if libro else "No existe")

    print("\nBUSCAR INEXISTENTE:")
    libro = b.buscar_libro("Libro Inventado")
    print(libro.info() if libro else "No existe")

    print("\nPRÉSTAMO:")
    print(b.prestar_libro("El Cielo De Octubre"))  # pasa a 0
    print(b.prestar_libro("El Cielo De Octubre"))  # sin copias

    print("\nDEVOLUCIÓN:")
    print(b.devolver_libro("El Cielo De Octubre"))

    print("\nESTADO ESPECÍFICO:")
    libro = b.buscar_libro("El Cielo De Octubre")
    print(libro.info() if libro else "No existe")

    print("\nCATÁLOGO FINAL:")
    print(*b.mostrar_catalogo(), sep="\n- ")

if __name__ == "__main__":
    main()

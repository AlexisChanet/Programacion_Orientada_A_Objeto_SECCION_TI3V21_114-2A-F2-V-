# Importa la clase Catalogo desde la carpeta clases
from clases.catalogo import Catalogo

# Función principal: muestra ejemplos de registro, búsqueda y filtrado de películas
def main():
    c = Catalogo()

    print(c.agregar("Volver Al Futuro 2", "Ciencia Ficcion", 1989))
    print(c.agregar("La Mosca", "Horror", 1986))
    print(c.agregar("El Padrino", "Drama", 1972))
    print(c.agregar("Volver Al Futuro 2", "Ciencia Ficcion", 1989))  # repetida

    print("\nCATÁLOGO COMPLETO:")
    print(*c.mostrar_catalogo(), sep="\n- ")

    print("\nBUSCAR PELÍCULA:")
    print(c.buscar("La Mosca"))
    print(c.buscar("Matrix"))

    print("\nFILTRAR POR GÉNERO:")
    for linea in c.filtrar_por_genero("Horror"):
        print(linea)
    for linea in c.filtrar_por_genero("Comedia"):
        print(linea)

if __name__ == "__main__":
    main()

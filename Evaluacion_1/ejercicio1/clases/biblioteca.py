# Importa la clase libro desde el módulo correspondiente
from .libro import Libro

#Clase principal que gestiona el catalogo de libros
class Biblioteca:

    # Constructor: inicializa el nombre de la biblioteca y el catálogo vacio
    def __init__(self, nombre):
        self.nombre = nombre.strip().title()
        self.catalogo = {}

    # Registra un nuevo libro en el catálogo
    def registrar_libro(self, titulo, autor, copias):
        if titulo.lower() in self.catalogo:
            return "El libro ya está registrado."
        try:
            libro = Libro(titulo, autor, copias)
        except ValueError as e:
            return str(e)
        self.catalogo[titulo.lower()] = libro
        return "Libro registrado correctamente."
    
    # Buscar un libro por el catálago por su título
    def buscar_libro(self, titulo):
        return self.catalogo.get(titulo.lower())
    
    # Realiza el préstamo de un libro, si hay copias disponibles
    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if not libro:
            return "No existe ese libro."
        if libro.prestar():
            return "Préstamo realizado con éxito."
        return "No hay copias disponibles."

    # Registra la devolución de un libro prestado
    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if not libro:
            return "No existe ese libro."
        libro.devolver()
        return "Devolución registrada."

    # Devuelve una lista con la información de todos los libros del catálogo 
    def mostrar_catalogo(self):
        if not self.catalogo:
            return ["El catálogo está vacío."]
        return [libro.info() for libro in self.catalogo.values()]

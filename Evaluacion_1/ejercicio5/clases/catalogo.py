# Importa la clase Pelicula desde el módulo correspondiente
from .pelicula import Pelicula

# Clase que gestiona un catálogo de películas
class Catalogo:

    # Constructor: inicializa el diccionario vacío del catálogo
    def __init__(self):
        self.catalogo = {}

    # Agrega una nueva película al catálogo, validando duplicados y datos
    def agregar(self, titulo, genero, anio):
        k = titulo.strip().lower()
        if k in self.catalogo:
            return "La película ya existe."
        try:
            p = Pelicula(titulo, genero, anio)
        except ValueError as e:
            return str(e)
        self.catalogo[k] = p
        return "Película agregada correctamente."

    # Busca una película por título y devuelve su información
    def buscar(self, titulo):
        p = self.catalogo.get(titulo.strip().lower())
        return p.info() if p else "No se encontró la película."

    # Filtra las películas por género y devuelve las coincidencias
    def filtrar_por_genero(self, genero):
        g = genero.strip().lower()
        resultados = [p.info() for p in self.catalogo.values() if p.genero.lower() == g]
        return resultados if resultados else ["No se encontraron películas de ese género."]

    # Devuelve una lista con todas las películas registradas en el catálogo
    def mostrar_catalogo(self):
        if not self.catalogo:
            return ["El catálogo está vacío."]
        return [p.info() for p in self.catalogo.values()]

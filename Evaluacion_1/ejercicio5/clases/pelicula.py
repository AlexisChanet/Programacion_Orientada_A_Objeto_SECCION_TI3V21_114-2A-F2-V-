# Clase que define una película dentro del catálogo
class Pelicula:
     
    # Constructor: valida los datos y asigna los atributos principales
    def __init__(self, titulo, genero, anio):
        if not titulo or not genero:
            raise ValueError("El título y el género son obligatorios.")
        a = int(anio)
        if a <= 0:
            raise ValueError("El año debe ser mayor que 0.")
        self.titulo = titulo.strip().title()
        self.genero = genero.strip().title()
        self.anio = a

    # Devuelve una cadena con la información formateada de la película
    def info(self):
        return f"{self.titulo} ({self.anio}) - Género: {self.genero}"

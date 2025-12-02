# Clase que representa un libro con su título, autor y número de copias disponibles
class Libro:
    def __init__(self, titulo, autor, copias):
        if not titulo or not autor:
            raise ValueError("El título y el autor son obligatorios.")
        if int(copias) < 0:
            raise ValueError("Las copias no pueden ser negativas.")
        self.titulo = titulo.strip().title()
        self.autor = autor.strip().title()
        self.copias = int(copias)

    def prestar(self):
        if self.copias > 0:
            self.copias -= 1
            return True
        return False

    def devolver(self):
        self.copias += 1

    def info(self):
        return f"{self.titulo} ({self.autor}) | Copias disponibles: {self.copias}"

# Clase que define a un alumno dentro de un curso
class Alumno:
    def __init__(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del alumno es obligatorio.")
        self.nombre = nombre.strip().title()

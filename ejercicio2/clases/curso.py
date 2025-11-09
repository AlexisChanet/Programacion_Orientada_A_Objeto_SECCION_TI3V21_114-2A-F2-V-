# Importa la clase Alumno desde el módulo correspondiente
from .alumno import Alumno

# Clase que representa un curso con su nombre y lista de alumnos inscritos
class Curso:

     # Constructor: inicializa el nombre del curso y el diccionario de inscritos
    def __init__(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del curso es obligatorio.")
        self.nombre = nombre.strip().title()
        self._inscritos = {}

    # Inscribe a un nuevo alumno del curso
    def inscribir(self, nombre):
        key = nombre.strip().lower()
        if key in self._inscritos:
            return "El alumno ya está inscrito."
        self._inscritos[key] = Alumno(nombre)
        return "Inscripción realizada."

    # Elimina un alumno del curso
    def remover(self, nombre):
        key = nombre.strip().lower()
        if key not in self._inscritos:
            return "El alumno no está inscrito."
        del self._inscritos[key]
        return "Alumno removido."

    # Devuelve una lista ordenada con los nombres de los alumnos inscritos
    def listar(self):
        return sorted(a.nombre for a in self._inscritos.values())

    # Muestra el estado actual del curso con sus alumnos
    def estado(self):
        lista = ", ".join(self.listar()) if self._inscritos else "Sin alumnos inscritos."
        return f"Curso: {self.nombre} | Alumnos: {lista}"

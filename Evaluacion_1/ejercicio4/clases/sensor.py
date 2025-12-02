# Clase que representa un sensor que almacena mediciones numéricas
class Sensor:

    # Constructor: inicializa el nombre del sensor y la lista vacía de mediciones
    def __init__(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del sensor es obligatorio.")
        self.nombre = nombre.strip().title()
        self.mediciones = []

     # Registra una nueva medición en la lista
    def registrar(self, valor):
        v = float(valor)
        self.mediciones.append(v)
        return "Medición registrada."

    # Calcula el promedio de las mediciones registradas
    def promedio(self):
        if not self.mediciones:
            return 0.0
        return sum(self.mediciones) / len(self.mediciones)

    # Obtiene el valor máximo registrado
    def maximo(self):
        if not self.mediciones:
            return 0.0
        return max(self.mediciones)

    # Obtiene el valor mínimo registrado
    def minimo(self):
        if not self.mediciones:
            return 0.0
        return min(self.mediciones)

    # Devuelve un resumen con el promedio, máximo y mínimo de las mediciones
    def resumen(self):
        p = self.promedio()
        mx = self.maximo()
        mn = self.minimo()
        return f"Sensor: {self.nombre} | Promedio: {p:.2f} | Máximo: {mx:.2f} | Mínimo: {mn:.2f}"

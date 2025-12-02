from .contacto import Contacto

class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar(self, nombre, telefono, correo):
        k = nombre.strip().lower()
        if k in self.contactos:
            return "El contacto ya existe."
        try:
            self.contactos[k] = Contacto(nombre, telefono, correo)
        except ValueError as e:
            return str(e)
        return "Contacto agregado correctamente."

    def buscar(self, nombre):
        c = self.contactos.get(nombre.strip().lower())
        return c.ficha() if c else "No se encontró el contacto."

    def eliminar(self, nombre):
        k = nombre.strip().lower()
        if k in self.contactos:
            del self.contactos[k]
            return "Contacto eliminado."
        return "No se encontró el contacto."

    def listar(self):
        if not self.contactos:
            return ["(sin contactos en la agenda)"]
        return [c.ficha() for c in self.contactos.values()]
    
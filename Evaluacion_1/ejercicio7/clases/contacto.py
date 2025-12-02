class Contacto:
    def __init__(self, nombre, telefono, correo):
        if not nombre or not telefono or not correo:
            raise ValueError("Nombre, teléfono y correo son obligatorios.")
        self.nombre = nombre.strip().title()
        self.telefono = str(telefono).strip()
        self.correo = correo.strip()

    def ficha(self):
        return f"{self.nombre} | Teléfono: {self.telefono} | Correo: {self.correo}"

#Clase que define un ítem dentro de un pedido
class Item:
    def __init__(self, nombre, precio, cantidad):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre del ítem es obligatorio.")
        p = float(precio)
        c = int(cantidad)
        if p < 0 or c < 0:
            raise ValueError("Precio y cantidad no pueden ser negativos.")
        self.nombre = nombre.strip().title()
        self.precio = p
        self.cantidad = c

      # Calcula el subtotal multiplicando precio por cantidad
    def subtotal(self):
        return self.precio * self.cantidad

     # Devuelve una cadena con toda la información del ítem
    def info(self):
        return f"{self.nombre} | Precio: {self.precio:.2f} | Cantidad: {self.cantidad} | Subtotal: {self.subtotal():.2f}"

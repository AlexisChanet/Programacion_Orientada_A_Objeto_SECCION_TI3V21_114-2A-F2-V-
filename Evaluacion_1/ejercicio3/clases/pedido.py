#Importa la clase Item desde el módulo correspondiente
from .item import Item

# Clase que representa un pedido con varios ítems
class Pedido:
    # Constructor: crea una lista vacía para almacenar los ítems del pedido
    def __init__(self):
        self.items = []

    # Agrega un nuevo ítem al pedido    
    def agregar_item(self, nombre, precio, cantidad):
        self.items.append(Item(nombre, precio, cantidad))
        return "Ítem agregado."

    # Devuelve una lista con la información de todos los ítems
    def listar(self):
        if not self.items:
            return ["(sin ítems)"]
        return [i.info() for i in self.items]

    # Calcula el total del pedido sumando los subtotales de cada ítem
    def total(self):
        return sum(i.subtotal() for i in self.items)

    # Devuelve el detalle completo del pedido, incluyendo el total general
    def detalle(self):
        lineas = self.listar()
        lineas.append(f"TOTAL: {self.total():.2f}")
        return lineas

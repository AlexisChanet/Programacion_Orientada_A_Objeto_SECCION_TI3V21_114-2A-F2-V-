# Importa la clase Pedido desde la carpeta clases
from clases.pedido import Pedido

# Función auxiliar para mostrar valores en formato CLP 
def clp(v):
    return f"${v:,.0f} CLP".replace(",", ".")

# Función principal: crea un pedido y muestra ejemplos de uso
def main():
    p = Pedido()
    print(p.agregar_item("Pan", 1200, 2))
    print(p.agregar_item("Leche", 950, 3))
    print(p.agregar_item("Queso", 3200, 1))

    print("\nÍTEMS:")
    for i in p.items:
        print(f"{i.nombre} | Precio: {clp(i.precio)} | Cantidad: {i.cantidad} | Subtotal: {clp(i.subtotal())}")

    print("\nTOTAL:")
    print(clp(p.total()))

    print("\nDETALLE COMPLETO:")
    for linea in p.detalle()[:-1]:
        nombre = linea.split(" | ")[0]
        precio = float(linea.split("Precio: ")[1].split(" | ")[0])
        cantidad = int(linea.split("Cantidad: ")[1].split(" | ")[0])
        subtotal = float(linea.split("Subtotal: ")[1])
        print(f"{nombre} | Precio: {clp(precio)} | Cantidad: {cantidad} | Subtotal: {clp(subtotal)}")
    print("TOTAL:", clp(p.total()))

if __name__ == "__main__":
    main()

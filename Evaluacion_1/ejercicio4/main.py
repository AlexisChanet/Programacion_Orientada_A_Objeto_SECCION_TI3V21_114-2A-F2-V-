# Importa la clase Sensor desde la carpeta clases
from clases.sensor import Sensor

# Función principal: crea un sensor y muestra sus mediciones y cálculos
def main():
    s = Sensor("Temperatura")

    print(s.registrar(21.5))
    print(s.registrar(23.0))
    print(s.registrar(19.8))
    print(s.registrar(22.1))

    print("\nMEDICIONES (ORDENADAS):")
    for m in sorted(s.mediciones):
        print(f"- {m}")

    print("\nCÁLCULOS:")
    print(f"Promedio: {s.promedio():.2f}")
    print(f"Máximo: {s.maximo():.2f}")
    print(f"Mínimo: {s.minimo():.2f}")

    print("\nRESUMEN:")
    print(s.resumen())

if __name__ == "__main__":
    main()

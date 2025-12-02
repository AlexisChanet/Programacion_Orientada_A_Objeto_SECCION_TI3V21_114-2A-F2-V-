from clases.agenda import Agenda

def main():
    print("=== AGENDA DE 31 MINUTOS ===")

    a = Agenda()

    print(a.agregar("Juan Carlos Bodoque", "987654321", "bodoque@teleserie.cl"))
    print(a.agregar("Juanin Juan Harry", "912345678", "juanin@noticias.cl"))
    print(a.agregar("Tulio Triviño", "900000000", "tulio@noticias.cl"))
    print(a.agregar("Juan Carlos Bodoque", "999999999", "duplicado@correo.cl"))

    print("\nLISTA DE CONTACTOS:")
    for contacto in a.listar():
        print(f"- {contacto}")

    print("\nBUSCAR CONTACTO:")
    print(a.buscar("Juan Carlos Bodoque"))
    print(a.buscar("Policarpo Avendaño"))

    print("\nELIMINAR CONTACTO:")
    print(a.eliminar("Policarpo Avendaño"))
    print(a.eliminar("Juanin Juan Harry"))

    print("\nLISTA FINAL:")
    for contacto in a.listar():
        print(f"- {contacto}")

    print("\nAgenda actualizada. ¡Listos para una nueva edición de 31 Minutos!")

if __name__ == "__main__":
    main()

# Importa la clase Auth desde la carpeta clases
from clases.auth import Auth

# Función principal: muestra ejemplos de registro, listado y login de usuarios
def main():

    # Crear instancia del sistema de autenticación
    sistema = Auth()

    # Registrar varios usuarios
    print(sistema.registrar("Juan Carlos Bodoque", "1234"))
    print(sistema.registrar("Juanin Juan Harry", "abcd"))
    print(sistema.registrar("Juan Carlos Bodoque", "4321"))  # usuario duplicado

    # Mostrar lista de usuarios registrados
    print("\nLISTA DE USUARIOS:")
    for usuario in sistema.listar_usuarios():
        print(f"- {usuario}")


    # Probar inicio de sesión con diferentes casos
    print("\nPRUEBAS DE LOGIN:")
    print(sistema.login("Juan Carlos Bodoque", "1234"))   # correcto
    print(sistema.login("Juanin Juan Harry", "zzz"))      # contraseña incorrecta
    print(sistema.login("Tulio Triviño", "0000"))         # usuario no existe


if __name__ == "__main__":
    main()
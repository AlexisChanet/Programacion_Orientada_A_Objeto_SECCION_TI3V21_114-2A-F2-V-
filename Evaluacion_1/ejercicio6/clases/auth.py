# Importa la clase Usuario desde el módulo correspondiente
from .usuario import Usuario


# Clase principal que maneja el registro y login de usuarios
class Auth:
    
    # Constructor: crea el diccionario vacío de usuarios registrados
    def __init__(self):
        self.usuarios = {}

    # Registra un nuevo usuario, validando duplicados
    def registrar(self, username, password):
        key = username.strip().lower()
        if key in self.usuarios:
            return "El usuario ya existe."
        try:
            u = Usuario(username, password)
        except ValueError as e:
            return str(e)
        self.usuarios[key] = u
        return "Usuario registrado correctamente."

    # Verifica las credenciales de inicio de sesión
    def login(self, username, password):
        key = username.strip().lower()
        u = self.usuarios.get(key)
        if not u:
            return "Usuario no encontrado."
        return "Inicio de sesión exitoso." if u.password == str(password) else "Contraseña incorrecta."

    # Devuelve la lista de usuarios registrados en orden alfabético
    def listar_usuarios(self):
        if not self.usuarios:
            return ["(sin usuarios registrados)"]
        return sorted(u.username for u in self.usuarios.values())
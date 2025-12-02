# Clase que define un usuario dentro del sistema
class Usuario:
    
    # Constructor: valida los datos y guarda nombre y contraseña
    def __init__(self, username, password):
        if not username or not password:
            raise ValueError("Usuario y contraseña son obligatorios.")
        self.username = username.strip().lower()
        self.password = str(password)
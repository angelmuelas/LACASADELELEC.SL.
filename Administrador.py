# Administrador.py
class Administrador:
    def __init__(self, id: int, nombre: str, email: str, contrasena: str):
        self._id = id
        self._nombre = nombre
        self._email = email
        self._contrasena = contrasena
    
    def get_id(self) -> int:
        return self._id
    
    def set_id(self, id: int):
        self._id = id
    
    def get_nombre(self) -> str:
        return self._nombre
    
    def set_nombre(self, nombre: str):
        self._nombre = nombre
    
    def get_email(self) -> str:
        return self._email
    
    def set_email(self, email: str):
        self._email = email
    
    def get_contrasena(self) -> str:
        return self._contrasena
    
    def set_contrasena(self, contrasena: str):
        self._contrasena = contrasena

    def __repr__(self) -> str:
        return (f"Administrador(ID={self._id}, Nombre='{self._nombre}', "
                f"Email='{self._email}')")

# Cliente.py
class Cliente:
    def __init__(self, id: int, nombre: str, email: str, contrasena: str, direccion: str, 
                 telefono: str, dni: str, genero: str, fechaNacimiento: str, 
                 fechaRegistro: str, categoria: str, historial: str):
        self._id = id
        self._nombre = nombre
        self._email = email
        self._contrasena = contrasena
        self._direccion = direccion
        self._telefono = telefono
        self._dni = dni
        self._genero = genero
        self._fechaNacimiento = fechaNacimiento
        self._fechaRegistro = fechaRegistro
        self._categoria = categoria
        self._historial = historial
    
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
    
    def get_direccion(self) -> str:
        return self._direccion
    
    def set_direccion(self, direccion: str):
        self._direccion = direccion
    
    def get_telefono(self) -> str:
        return self._telefono
    
    def set_telefono(self, telefono: str):
        self._telefono = telefono
    
    def get_dni(self) -> str:
        return self._dni
    
    def set_dni(self, dni: str):
        self._dni = dni
    
    def get_genero(self) -> str:
        return self._genero
    
    def set_genero(self, genero: str):
        self._genero = genero
    
    def get_fechaNacimiento(self) -> str:
        return self._fechaNacimiento
    
    def set_fechaNacimiento(self, fechaNacimiento: str):
        self._fechaNacimiento = fechaNacimiento
    
    def get_fechaRegistro(self) -> str:
        return self._fechaRegistro
    
    def set_fechaRegistro(self, fechaRegistro: str):
        self._fechaRegistro = fechaRegistro
    
    def get_categoria(self) -> str:
        return self._categoria
    
    def set_categoria(self, categoria: str):
        self._categoria = categoria
    
    def get_historial(self) -> str:
        return self._historial
    
    def set_historial(self, historial: str):
        self._historial = historial

    def __repr__(self) -> str:
        return (
            f"Cliente(ID={self._id}, Nombre='{self._nombre}', Email='{self._email}', "
            f"Categoria='{self._categoria}')"
        )

from dataclasses import dataclass

@dataclass
class Cliente:
    id: int
    nombre: str
    email: str
    contrasena: str
    direccion: str
    telefono: str
    dni: str
    genero: str
    fechaNacimiento: str
    fechaRegistro: str
    categoria: str
    historial: str

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_nombre(self) -> str:
        return self.nombre

    def set_nombre(self, nombre: str):
        self.nombre = nombre

    def get_email(self) -> str:
        return self.email

    def set_email(self, email: str):
        self.email = email

    def get_contrasena(self) -> str:
        return self.contrasena

    def set_contrasena(self, contrasena: str):
        self.contrasena = contrasena

    def get_direccion(self) -> str:
        return self.direccion

    def set_direccion(self, direccion: str):
        self.direccion = direccion

    def get_telefono(self) -> str:
        return self.telefono

    def set_telefono(self, telefono: str):
        self.telefono = telefono

    def get_dni(self) -> str:
        return self.dni

    def set_dni(self, dni: str):
        self.dni = dni

    def get_genero(self) -> str:
        return self.genero

    def set_genero(self, genero: str):
        self.genero = genero

    def get_fechaNacimiento(self) -> str:
        return self.fechaNacimiento

    def set_fechaNacimiento(self, fechaNacimiento: str):
        self.fechaNacimiento = fechaNacimiento

    def get_fechaRegistro(self) -> str:
        return self.fechaRegistro

    def set_fechaRegistro(self, fechaRegistro: str):
        self.fechaRegistro = fechaRegistro

    def get_categoria(self) -> str:
        return self.categoria

    def set_categoria(self, categoria: str):
        self.categoria = categoria

    def get_historial(self) -> str:
        return self.historial

    def set_historial(self, historial: str):
        self.historial = historial

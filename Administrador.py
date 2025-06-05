from dataclasses import dataclass

@dataclass
class Administrador:
    id: int
    nombre: str
    email: str
    contrasena: str

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

from dataclasses import dataclass

@dataclass
class Producto:
    id: int
    tipo: str
    marca: str
    precio: float
    color: str

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_tipo(self) -> str:
        return self.tipo

    def set_tipo(self, tipo: str):
        self.tipo = tipo

    def get_marca(self) -> str:
        return self.marca

    def set_marca(self, marca: str):
        self.marca = marca

    def get_precio(self) -> float:
        return self.precio

    def set_precio(self, precio: float):
        self.precio = precio

    def get_color(self) -> str:
        return self.color

    def set_color(self, color: str):
        self.color = color

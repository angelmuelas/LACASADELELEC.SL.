from dataclasses import dataclass

@dataclass
class Carrito:
    id: int
    productoTotal: int
    fechaCreacion: str
    estado: str
    precioTotal: float
    descuentoTotal: float
    precioFinal: float

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_productoTotal(self) -> int:
        return self.productoTotal

    def set_productoTotal(self, productoTotal: int):
        self.productoTotal = productoTotal

    def get_fechaCreacion(self) -> str:
        return self.fechaCreacion

    def set_fechaCreacion(self, fechaCreacion: str):
        self.fechaCreacion = fechaCreacion

    def get_estado(self) -> str:
        return self.estado

    def set_estado(self, estado: str):
        self.estado = estado

    def get_precioTotal(self) -> float:
        return self.precioTotal

    def set_precioTotal(self, precioTotal: float):
        self.precioTotal = precioTotal

    def get_descuentoTotal(self) -> float:
        return self.descuentoTotal

    def set_descuentoTotal(self, descuentoTotal: float):
        self.descuentoTotal = descuentoTotal

    def get_precioFinal(self) -> float:
        return self.precioFinal

    def set_precioFinal(self, precioFinal: float):
        self.precioFinal = precioFinal

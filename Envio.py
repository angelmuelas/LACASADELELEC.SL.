from dataclasses import dataclass

@dataclass
class Envio:
    id: int
    pedido: str
    fechaEnvio: str
    fechaEntrega: str
    estado: str
    transportista: str
    peso: float
    volumen: float

    def get_id(self) -> int:
        return self.id

    def set_id(self, id: int):
        self.id = id

    def get_pedido(self) -> str:
        return self.pedido

    def set_pedido(self, pedido: str):
        self.pedido = pedido

    def get_fechaEnvio(self) -> str:
        return self.fechaEnvio

    def set_fechaEnvio(self, fechaEnvio: str):
        self.fechaEnvio = fechaEnvio

    def get_fechaEntrega(self) -> str:
        return self.fechaEntrega

    def set_fechaEntrega(self, fechaEntrega: str):
        self.fechaEntrega = fechaEntrega

    def get_estado(self) -> str:
        return self.estado

    def set_estado(self, estado: str):
        self.estado = estado

    def get_transportista(self) -> str:
        return self.transportista

    def set_transportista(self, transportista: str):
        self.transportista = transportista

    def get_peso(self) -> float:
        return self.peso

    def set_peso(self, peso: float):
        self.peso = peso

    def get_volumen(self) -> float:
        return self.volumen

    def set_volumen(self, volumen: float):
        self.volumen = volumen

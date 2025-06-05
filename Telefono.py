from dataclasses import dataclass
from Producto import Producto

@dataclass
class Telefono(Producto):
    pulgadas: float
    sistemaOperativo: str

    def get_pulgadas(self) -> float:
        return self.pulgadas

    def set_pulgadas(self, pulgadas: float):
        self.pulgadas = pulgadas

    def get_sistemaOperativo(self) -> str:
        return self.sistemaOperativo

    def set_sistemaOperativo(self, sistemaOperativo: str):
        self.sistemaOperativo = sistemaOperativo

from dataclasses import dataclass
from Producto import Producto

@dataclass
class Television(Producto):
    conectividad: str
    pulgadas: float

    def get_conectividad(self) -> str:
        return self.conectividad

    def set_conectividad(self, conectividad: str):
        self.conectividad = conectividad

    def get_pulgadas(self) -> float:
        return self.pulgadas

    def set_pulgadas(self, pulgadas: float):
        self.pulgadas = pulgadas

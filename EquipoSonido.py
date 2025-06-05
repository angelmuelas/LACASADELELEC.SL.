from dataclasses import dataclass
from Producto import Producto

@dataclass
class EquipoSonido(Producto):
    potencia: int

    def get_potencia(self) -> int:
        return self.potencia

    def set_potencia(self, potencia: int):
        self.potencia = potencia

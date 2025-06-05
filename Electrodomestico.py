from dataclasses import dataclass
from Producto import Producto

@dataclass
class Electrodomestico(Producto):
    etiquetaDeConsumo: str

    def get_etiquetaDeConsumo(self) -> str:
        return self.etiquetaDeConsumo

    def set_etiquetaDeConsumo(self, etiquetaDeConsumo: str):
        self.etiquetaDeConsumo = etiquetaDeConsumo

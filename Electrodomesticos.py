# Electrodomesticos.py
from typing import List
from ProductosGen import ProductosGen
from Electrodomestico import Electrodomestico

class Electrodomesticos(ProductosGen[Electrodomestico]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Electrodomestico) -> str:
        return str(elemento)
    
    def agruparPorEtiquetaConsumo(self, etiquetaConsumo: str) -> List[Electrodomestico]:
        return [elemento for elemento in self._elementos 
                if elemento.get_etiquetaDeConsumo().lower() == etiquetaConsumo.lower()]
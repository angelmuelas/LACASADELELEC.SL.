# Electrodomesticos.py
from typing import List
from ProductosGen import ProductosGen
from Electrodomestico import Electrodomestico

class Electrodomesticos(ProductosGen[Electrodomestico]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Electrodomestico) -> str:
        return f"ID: {elemento.get_id()}, Tipo: {elemento.get_tipo()}, Marca: {elemento.get_marca()}, Precio: {elemento.get_precio()}€, Etiqueta: {elemento.get_etiquetaDeConsumo()}"
    
    def agruparPorEtiquetaConsumo(self, etiquetaConsumo: str) -> List[Electrodomestico]:
        return [elemento for elemento in self._elementos 
                if elemento.get_etiquetaDeConsumo().lower() == etiquetaConsumo.lower()]
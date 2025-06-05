# EquiposSonido.py
from typing import List
from ProductosGen import ProductosGen
from EquipoSonido import EquipoSonido

class EquiposSonido(ProductosGen[EquipoSonido]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: EquipoSonido) -> str:
        return f"ID: {elemento.get_id()}, Tipo: {elemento.get_tipo()}, Marca: {elemento.get_marca()}, Precio: {elemento.get_precio()}€, Potencia: {elemento.get_potencia()}W"
    
    def agruparPorPotencia(self, potencia: int) -> List[EquipoSonido]:
        return [elemento for elemento in self._elementos 
                if elemento.get_potencia() >= potencia]
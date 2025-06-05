# Televisiones.py
from typing import List
from ProductosGen import ProductosGen
from Television import Television

class Televisiones(ProductosGen[Television]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Television) -> str:
        return f"ID: {elemento.get_id()}, Tipo: {elemento.get_tipo()}, Marca: {elemento.get_marca()}, Precio: {elemento.get_precio()}€, Pulgadas: {elemento.get_pulgadas()}\", Conectividad: {elemento.get_conectividad()}"
    
    def agruparPorConectividad(self, conectividad: str) -> List[Television]:
        return [elemento for elemento in self._elementos 
                if conectividad.lower() in elemento.get_conectividad().lower()]
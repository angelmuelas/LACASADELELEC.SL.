# Televisiones.py
from typing import List
from ProductosGen import ProductosGen
from Television import Television

class Televisiones(ProductosGen[Television]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Television) -> str:
        return str(elemento)
    
    def agruparPorConectividad(self, conectividad: str) -> List[Television]:
        return [elemento for elemento in self._elementos 
                if conectividad.lower() in elemento.get_conectividad().lower()]
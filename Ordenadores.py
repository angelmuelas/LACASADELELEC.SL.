# Ordenadores.py
from typing import List
from ProductosGen import ProductosGen
from Ordenador import Ordenador

class Ordenadores(ProductosGen[Ordenador]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Ordenador) -> str:
        return str(elemento)
    
    def agruparPorProcesador(self, procesador: str) -> List[Ordenador]:
        return [elemento for elemento in self._elementos 
                if procesador.lower() in elemento.get_procesador().lower()]
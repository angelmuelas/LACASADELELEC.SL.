# PedidosGen.py
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from ListaGen import ListaGen

D = TypeVar('D')

class PedidosGen(ListaGen[D], ABC, Generic[D]):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def mostrarElemento(self, elemento: D) -> str:
        pass
    
    def agruparPorEstado(self, estado: str) -> List[D]:
        return [elemento for elemento in self._elementos 
                if hasattr(elemento, 'get_estado') and elemento.get_estado().lower() == estado.lower()]
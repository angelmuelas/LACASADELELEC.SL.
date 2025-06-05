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
        """Return elements with the requested state."""
        return [elemento for elemento in self._elementos
                if getattr(elemento, 'estado', '').lower() == estado.lower()]

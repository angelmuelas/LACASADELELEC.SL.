# ProductosGen.py
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from ListaGen import ListaGen

P = TypeVar('P')

class ProductosGen(ListaGen[P], ABC, Generic[P]):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def mostrarElemento(self, elemento: P) -> str:
        pass
    
    def agruparPorPrecio(self, precio: float) -> List[P]:
        """Return elements with a price lower or equal to ``precio``."""
        return [elemento for elemento in self._elementos
                if getattr(elemento, 'precio', None) is not None and elemento.precio <= precio]
    
    def agruparPorMarca(self, marca: str) -> List[P]:
        """Return elements matching the provided brand."""
        return [elemento for elemento in self._elementos
                if getattr(elemento, 'marca', '').lower() == marca.lower()]
    
    def buscarPorTipo(self, tipo: str) -> List[P]:
        """Return elements matching the provided type."""
        return [elemento for elemento in self._elementos
                if getattr(elemento, 'tipo', '').lower() == tipo.lower()]

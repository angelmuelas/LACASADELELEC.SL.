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
        return [elemento for elemento in self._elementos 
                if hasattr(elemento, 'get_precio') and elemento.get_precio() <= precio]
    
    def agruparPorMarca(self, marca: str) -> List[P]:
        return [elemento for elemento in self._elementos 
                if hasattr(elemento, 'get_marca') and elemento.get_marca().lower() == marca.lower()]
    
    def buscarPorTipo(self, tipo: str) -> List[P]:
        return [elemento for elemento in self._elementos 
                if hasattr(elemento, 'get_tipo') and elemento.get_tipo().lower() == tipo.lower()]
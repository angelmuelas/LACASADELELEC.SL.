# UsuariosGen.py
from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from ListaGen import ListaGen

U = TypeVar('U')

class UsuariosGen(ListaGen[U], ABC, Generic[U]):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def mostrarElemento(self, elemento: U) -> str:
        pass
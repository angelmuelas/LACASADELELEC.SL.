# ListaGen.py
from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')

class ListaGen(ABC, Generic[T]):
    def __init__(self):
        self._elementos: List[T] = []
    
    def agregar(self, elemento: T) -> bool:
        """Add an element to the internal list."""
        self._elementos.append(elemento)
        return True
    
    def eliminar(self, id: int) -> bool:
        """Remove an element by its id if present."""
        for i, elemento in enumerate(self._elementos):
            if hasattr(elemento, 'get_id') and elemento.get_id() == id:
                del self._elementos[i]
                return True
        return False
    
    def buscar(self, id: int) -> Optional[T]:
        for elemento in self._elementos:
            if hasattr(elemento, 'get_id') and elemento.get_id() == id:
                return elemento
        return None
    
    def mostrarTodos(self) -> List[T]:
        return self._elementos.copy()
    
    def estaVacia(self) -> bool:
        return len(self._elementos) == 0
    
    def cantidadElementos(self) -> int:
        return len(self._elementos)
    
    @abstractmethod
    def mostrarElemento(self, elemento: T) -> str:
        pass
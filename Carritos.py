# Carritos.py
from typing import List
from PedidosGen import PedidosGen
from Carrito import Carrito

class Carritos(PedidosGen[Carrito]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Carrito) -> str:
        return str(elemento)
    
    def agruparPorDescuentoTotal(self, descuento: float) -> List[Carrito]:
        return [elemento for elemento in self._elementos 
                if elemento.get_descuentoTotal() >= descuento]
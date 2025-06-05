# Envios.py
from typing import List
from PedidosGen import PedidosGen
from Envio import Envio

class Envios(PedidosGen[Envio]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Envio) -> str:
        return str(elemento)
    
    def agruparPorTransportista(self, transportista: str) -> List[Envio]:
        return [elemento for elemento in self._elementos 
                if transportista.lower() in elemento.get_transportista().lower()]
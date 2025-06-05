# Envios.py
from typing import List
from PedidosGen import PedidosGen
from Envio import Envio

class Envios(PedidosGen[Envio]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Envio) -> str:
        return f"ID: {elemento.get_id()}, Pedido: {elemento.get_pedido()}, Estado: {elemento.get_estado()}, Transportista: {elemento.get_transportista()}"
    
    def agruparPorTransportista(self, transportista: str) -> List[Envio]:
        return [elemento for elemento in self._elementos 
                if transportista.lower() in elemento.get_transportista().lower()]
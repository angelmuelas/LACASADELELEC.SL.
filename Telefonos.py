# Telefonos.py
from typing import List
from ProductosGen import ProductosGen
from Telefono import Telefono

class Telefonos(ProductosGen[Telefono]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Telefono) -> str:
        return f"ID: {elemento.get_id()}, Tipo: {elemento.get_tipo()}, Marca: {elemento.get_marca()}, Precio: {elemento.get_precio()}€, Pulgadas: {elemento.get_pulgadas()}\", SO: {elemento.get_sistemaOperativo()}"
    
    def agruparPorSistemaOperativo(self, sistemaOperativo: str) -> List[Telefono]:
        return [elemento for elemento in self._elementos 
                if sistemaOperativo.lower() in elemento.get_sistemaOperativo().lower()]
# Clientes.py
from typing import List, Optional
from UsuariosGen import UsuariosGen
from Cliente import Cliente

class Clientes(UsuariosGen[Cliente]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Cliente) -> str:
        return f"ID: {elemento.get_id()}, Nombre: {elemento.get_nombre()}, Email: {elemento.get_email()}, Categoria: {elemento.get_categoria()}"
    
    def agruparPorCategoria(self, categoria: str) -> List[Cliente]:
        return [elemento for elemento in self._elementos 
                if elemento.get_categoria().lower() == categoria.lower()]
    
    def buscarPorHistorial(self, historial: str) -> Optional[Cliente]:
        for elemento in self._elementos:
            if historial.lower() in elemento.get_historial().lower():
                return elemento
        return None
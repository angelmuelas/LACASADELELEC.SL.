# Administradores.py
from UsuariosGen import UsuariosGen
from Administrador import Administrador

class Administradores(UsuariosGen[Administrador]):
    def __init__(self):
        super().__init__()
    
    def mostrarElemento(self, elemento: Administrador) -> str:
        return str(elemento)

# Ordenador.py
class Ordenador:
    def __init__(self, id: int, tipo: str, marca: str, precio: float, color: str, sistemaOperativo: str, procesador: str, memoriaRam: int):
        self._id = id
        self._tipo = tipo
        self._marca = marca
        self._precio = precio
        self._color = color
        self._sistemaOperativo = sistemaOperativo
        self._procesador = procesador
        self._memoriaRam = memoriaRam
    
    def get_id(self) -> int:
        return self._id
    
    def set_id(self, id: int):
        self._id = id
    
    def get_tipo(self) -> str:
        return self._tipo
    
    def set_tipo(self, tipo: str):
        self._tipo = tipo
    
    def get_marca(self) -> str:
        return self._marca
    
    def set_marca(self, marca: str):
        self._marca = marca
    
    def get_precio(self) -> float:
        return self._precio
    
    def set_precio(self, precio: float):
        self._precio = precio
    
    def get_color(self) -> str:
        return self._color
    
    def set_color(self, color: str):
        self._color = color
    
    def get_sistemaOperativo(self) -> str:
        return self._sistemaOperativo
    
    def set_sistemaOperativo(self, sistemaOperativo: str):
        self._sistemaOperativo = sistemaOperativo
    
    def get_procesador(self) -> str:
        return self._procesador
    
    def set_procesador(self, procesador: str):
        self._procesador = procesador
    
    def get_memoriaRam(self) -> int:
        return self._memoriaRam
    
    def set_memoriaRam(self, memoriaRam: int):
        self._memoriaRam = memoriaRam
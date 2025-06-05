# Electrodomestico.py
class Electrodomestico:
    def __init__(self, id: int, tipo: str, marca: str, precio: float, color: str, etiquetaDeConsumo: str):
        self._id = id
        self._tipo = tipo
        self._marca = marca
        self._precio = precio
        self._color = color
        self._etiquetaDeConsumo = etiquetaDeConsumo
    
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
    
    def get_etiquetaDeConsumo(self) -> str:
        return self._etiquetaDeConsumo
    
    def set_etiquetaDeConsumo(self, etiquetaDeConsumo: str):
        self._etiquetaDeConsumo = etiquetaDeConsumo
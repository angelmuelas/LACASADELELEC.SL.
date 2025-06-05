# Television.py
class Television:
    def __init__(self, id: int, tipo: str, marca: str, precio: float, color: str, conectividad: str, pulgadas: float):
        self._id = id
        self._tipo = tipo
        self._marca = marca
        self._precio = precio
        self._color = color
        self._conectividad = conectividad
        self._pulgadas = pulgadas
    
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
    
    def get_conectividad(self) -> str:
        return self._conectividad
    
    def set_conectividad(self, conectividad: str):
        self._conectividad = conectividad
    
    def get_pulgadas(self) -> float:
        return self._pulgadas
    
    def set_pulgadas(self, pulgadas: float):
        self._pulgadas = pulgadas

    def __repr__(self) -> str:
        return (
            f"Television(ID={self._id}, Tipo='{self._tipo}', Marca='{self._marca}', "
            f"Precio={self._precio}€, Pulgadas={self._pulgadas}\", Conectividad='{self._conectividad}')"
        )

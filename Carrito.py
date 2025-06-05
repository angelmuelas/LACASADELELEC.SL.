# Carrito.py
class Carrito:
    def __init__(self, id: int, productoTotal: int, fechaCreacion: str, estado: str, 
                 precioTotal: float, descuentoTotal: float, precioFinal: float):
        self._id = id
        self._productoTotal = productoTotal
        self._fechaCreacion = fechaCreacion
        self._estado = estado
        self._precioTotal = precioTotal
        self._descuentoTotal = descuentoTotal
        self._precioFinal = precioFinal
    
    def get_id(self) -> int:
        return self._id
    
    def set_id(self, id: int):
        self._id = id
    
    def get_productoTotal(self) -> int:
        return self._productoTotal
    
    def set_productoTotal(self, productoTotal: int):
        self._productoTotal = productoTotal
    
    def get_fechaCreacion(self) -> str:
        return self._fechaCreacion
    
    def set_fechaCreacion(self, fechaCreacion: str):
        self._fechaCreacion = fechaCreacion
    
    def get_estado(self) -> str:
        return self._estado
    
    def set_estado(self, estado: str):
        self._estado = estado
    
    def get_precioTotal(self) -> float:
        return self._precioTotal
    
    def set_precioTotal(self, precioTotal: float):
        self._precioTotal = precioTotal
    
    def get_descuentoTotal(self) -> float:
        return self._descuentoTotal
    
    def set_descuentoTotal(self, descuentoTotal: float):
        self._descuentoTotal = descuentoTotal
    
    def get_precioFinal(self) -> float:
        return self._precioFinal
    
    def set_precioFinal(self, precioFinal: float):
        self._precioFinal = precioFinal
# Envio.py
class Envio:
    def __init__(self, id: int, pedido: str, fechaEnvio: str, fechaEntrega: str, 
                 estado: str, transportista: str, peso: float, volumen: float):
        self._id = id
        self._pedido = pedido
        self._fechaEnvio = fechaEnvio
        self._fechaEntrega = fechaEntrega
        self._estado = estado
        self._transportista = transportista
        self._peso = peso
        self._volumen = volumen
    
    def get_id(self) -> int:
        return self._id
    
    def set_id(self, id: int):
        self._id = id
    
    def get_pedido(self) -> str:
        return self._pedido
    
    def set_pedido(self, pedido: str):
        self._pedido = pedido
    
    def get_fechaEnvio(self) -> str:
        return self._fechaEnvio
    
    def set_fechaEnvio(self, fechaEnvio: str):
        self._fechaEnvio = fechaEnvio
    
    def get_fechaEntrega(self) -> str:
        return self._fechaEntrega
    
    def set_fechaEntrega(self, fechaEntrega: str):
        self._fechaEntrega = fechaEntrega
    
    def get_estado(self) -> str:
        return self._estado
    
    def set_estado(self, estado: str):
        self._estado = estado
    
    def get_transportista(self) -> str:
        return self._transportista
    
    def set_transportista(self, transportista: str):
        self._transportista = transportista
    
    def get_peso(self) -> float:
        return self._peso
    
    def set_peso(self, peso: float):
        self._peso = peso
    
    def get_volumen(self) -> float:
        return self._volumen
    
    def set_volumen(self, volumen: float):
        self._volumen = volumen
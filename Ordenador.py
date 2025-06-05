from dataclasses import dataclass
from Producto import Producto

@dataclass
class Ordenador(Producto):
    sistemaOperativo: str
    procesador: str
    memoriaRam: int

    def get_sistemaOperativo(self) -> str:
        return self.sistemaOperativo

    def set_sistemaOperativo(self, sistemaOperativo: str):
        self.sistemaOperativo = sistemaOperativo

    def get_procesador(self) -> str:
        return self.procesador

    def set_procesador(self, procesador: str):
        self.procesador = procesador

    def get_memoriaRam(self) -> int:
        return self.memoriaRam

    def set_memoriaRam(self, memoriaRam: int):
        self.memoriaRam = memoriaRam

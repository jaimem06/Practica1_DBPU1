from enum import Enum

class EstadoProducto(Enum):
    BUEN_ESTADO = 'BUEN ESTADO'
    CADUCADO = 'CADUCADO'
    POR_CADUCAR = 'POR CADUCAR'

    def serialize(self):
        return self.name
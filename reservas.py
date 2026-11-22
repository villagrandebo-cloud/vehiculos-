import enum
import enum 

class reserva(cliente, enum): 
    def __init__(self, id_reserva, fecha_inicio, fecha_fin, EstadoReserva, nombre ,dni, telefono, correo): 
        super().__init__(nombre ,dni, telefono, correo, EstadoReserva)
        self.__id_reserva=id_reserva
        self.fecha_inicio=fecha_inicio
        self.fecha_fin=fecha_fin  

@property
def id_reserva(self):
    return self.__id_reserva

class RegistroHistorial:
    def __init__(self, estado: EstadoReserva, descripcion: str, momento: datetime | None = None):
        self.momento = momento or datetime.now()
        self.estado = estado
        self.descripcion = descripcion     

def calcular_costo_total(self):
        costo = self.vehiculo.calcular_costo(self.dias)
        if costo < 0:
            raise ("El costo total de un alquiler nunca puede ser negativo.")
        return round(costo, 2)

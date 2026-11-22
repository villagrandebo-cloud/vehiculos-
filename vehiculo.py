from enum import EstadoVehiculo, TipoVehiculo
class vehiculo:
    def __init__(self, patente,  marca, modelo, EstadoVehiculo, TipoVehiculo , tarifa_base):
        self.patente=patente
        self.marca=marca
        self.modelo=modelo
        self.EstadoVehiculo=EstadoVehiculo
        self.TipoVehiculo=TipoVehiculo
        self.__tarifa_base=tarifa_base

@property 
def tarifa_base(self):
    return self.__tarifa_base

@tarifa_base.setter
def tarifa_base(self, valor: float):
    if valor <= 0:
        raise ValueError("La tarifa base por día debe ser mayor que cero.")
    self.__tarifa_base = float(valor)

def calcular_costo(self, dias: int) -> float:
        if dias <= 0:
            raise ValueError("La cantidad de días debe ser mayor que cero.")
        costo = self.__tarifa_base * dias
        return max(0.0, round(costo,2)) #LIMITO LOS DECIMALES. 

class auto (vehiculo):
    def __init__(self, patente,  marca, modelo, estado, tipo, tarifa_base ):
        super().__init__(patente,  marca, modelo, estado, tipo, tarifa_base)

    def calcular_costo(self, dias: int):
        return super().calcular_costo(dias)

class Camioneta(vehiculo):
    def calcular_costo(self, dias):
        costo = (self.tarifa_base_por_dia * 0.20) * dias
        return costo
    
    def calcular_costo(self, dias: int):
        base = super().calcular_costo(dias)
        return max(0.0, round(base * 1.20, 2))

class Moto(vehiculo):
    def calcular_costo(self, dias: int):
        costo = (self.tarifa_base_por_dia * 0.15) * dias
        return costo

    def calcular_costo(self, dias: int):
        base = super().calcular_costo(dias)
        return max(0.0, round(base * 0.85, 2))
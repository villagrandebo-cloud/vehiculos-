from reservas import reserva

class cliente:
    def __init__(self, nombre, dni, telefono, correo, reservas):
        self.nombre=nombre
        self.dni=dni
        self.telefono=telefono
        self.correo=correo
        self.reservas = [ ]

@property
def reservas(self):
    return self._reservas

def agregar_reserva(self, reserva: "Reserva"):
    if reserva not in self._reservas:
        self._reservas.append(reserva)
    
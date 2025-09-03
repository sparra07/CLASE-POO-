class Motor:
    def __init__(self):
        self.encendido = False

    def encender(self):
        self.encendido = True
        print("Motor encendido.")

    def apagar(self):
        self.encendido = False
        print("Motor apagado.")
class Vehiculo:
    def __init__(self, placa):
        self.placa = placa
        self.en_servicio = True
        self.motor = Motor()

    def encender_motor(self):
        if self.en_servicio:
            self.motor.encender()
        else:
            print(f"Vehículo {self.placa} fuera de servicio. No se puede encender el motor.")

    def apagar_motor(self):
        self.motor.apagar()

    def poner_en_servicio(self):
        self.en_servicio = True
        print(f"Vehículo {self.placa} puesto en servicio.")

    def sacar_de_servicio(self):
        self.en_servicio = False
        self.apagar_motor()  # Apaga el motor si se saca de servicio
        print(f"Vehículo {self.placa} fuera de servicio.")
class Flota:
    def __init__(self):
        self.vehiculos = {}

    def agregar_vehiculo(self, vehiculo):
        if vehiculo.placa in self.vehiculos:
            print(f"Vehículo con placa {vehiculo.placa} ya existe en la flota.")
        else:
            self.vehiculos[vehiculo.placa] = vehiculo
            print(f"Vehículo {vehiculo.placa} agregado a la flota.")

    def remover_vehiculo(self, placa):
        if placa in self.vehiculos:
            vehiculo = self.vehiculos.pop(placa)
            print(f"Vehículo {placa} removido de la flota.")
            return vehiculo
        else:
            print(f"No se encontró un vehículo con placa {placa}.")
            return None

    def buscar_vehiculo(self, placa):
        return self.vehiculos.get(placa, None)

    def reporte(self):
        total = len(self.vehiculos)
        en_servicio = sum(1 for v in self.vehiculos.values() if v.en_servicio)
        fuera_servicio = total - en_servicio
        encendidos = sum(1 for v in self.vehiculos.values() if v.motor.encendido)

        print("=== Reporte de Flota ===")
        print(f"Total vehículos: {total}")
        print(f"En servicio: {en_servicio}")
        print(f"Fuera de servicio: {fuera_servicio}")
        print(f"Motores encendidos: {encendidos}")
# Crear vehículos
v1 = Vehiculo("ABC123")
v2 = Vehiculo("XYZ789")

# Crear flota y agregar vehículos
f = Flota()
f.agregar_vehiculo(v1)
f.agregar_vehiculo(v2)

# Operaciones sobre vehículos
v1.encender_motor()
v2.sacar_de_servicio()
v2.encender_motor()  # No debe encender

# Consultar reporte
f.reporte()

# Buscar vehículo
buscado = f.buscar_vehiculo("XYZ789")
if buscado:
    print(f"Vehículo encontrado: {buscado.placa}")
else:
    print("Vehículo no encontrado.")

# Remover un vehículo
f.remover_vehiculo("ABC123")

# Nuevo reporte
f.reporte()

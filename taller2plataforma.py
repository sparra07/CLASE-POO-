class Motor:
    def __init__(self):
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("Motor encendido")
        else:
            print("El motor ya estaba encendido")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("Motor apagado")
        else:
            print("El motor ya estaba apagado")


class Vehiculo:
    def __init__(self, placa):
        self.placa = placa
        self.en_servicio = True
        self.motor = Motor()

    def poner_servicio(self):
        self.en_servicio = True
        print("El vehiculo", self.placa, "esta en sevicio ")

    def sacar_servicio(self):
        self.en_servicio = False
        print("El vehiculo", self.placa, "esta fuera de sevicio ")


class Flota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print("Vehículo", vehiculo.placa, "agregado a la flota")

    def quitar_vehiculo(self, placa):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                self.vehiculos.remove(vehiculo)
                print("Vehículo", placa, "eliminado de la flota")
                return vehiculo
        print("Vehículo no encontrado en la flota")
        return None

    def buscar_vehiculo(self, placa):
        for vehiculo in self.vehiculos:
            if vehiculo.placa == placa:
                return vehiculo
        return None

    def reporte(self):
        print("REporte de la flota:", self.nombre)
        print("Total vehículos:", len(self.vehiculos))

        for vehiculo in self.vehiculos:
            if vehiculo.en_servicio:
                estado_servicio = "En servicio"
            else:
                estado_servicio = "Fuera de servicio"

            if vehiculo.motor.encendido:
                estado_motor = "Encendido"
            else:
                estado_motor = "Apagado"

            print("Placa", vehiculo.placa , estado_servicio, estado_motor)


flota = Flota("Flota Principal")

print("Sistema de Gestión de Flota")
while True:
    print("Menú:")
    print("1. Agregar vehículo")
    print("2. Quitar vehículo")
    print("3. Encender motor de un vehículo")
    print("4. Apagar motor de un vehículo")
    print("5. Poner vehículo en servicio")
    print("6. Sacar vehículo de servicio")
    print("7. Reporte de flota")
    print("0, Salir")

    opcion = int(input("Ingrese opción: "))

    if opcion == 1:
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo_nuevo = Vehiculo(placa)
        flota.agregar_vehiculo(vehiculo_nuevo)

    elif opcion == 2:
        placa = input("Ingrese la placa del vehículo a quitar: ")
        flota.quitar_vehiculo(placa)

    elif opcion == 3:
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo_encontrado = flota.buscar_vehiculo(placa)
        if vehiculo_encontrado:
            vehiculo_encontrado.motor.encender()
        else:
            print("Vehículo no encontrado")

    elif opcion == 4:
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo_encontrado = flota.buscar_vehiculo(placa)
        if vehiculo_encontrado:
            vehiculo_encontrado.motor.apagar()
        else:
            print("Vehículo no encontrado")

    elif opcion == 5:
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo_encontrado = flota.buscar_vehiculo(placa)
        if vehiculo_encontrado:
            vehiculo_encontrado.poner_servicio()
        else:
            print("Vehículo no encontrado")

    elif opcion == 6:
        placa = input("Ingrese la placa del vehículo: ")
        vehiculo_encontrado = flota.buscar_vehiculo(placa)
        if vehiculo_encontrado:
            vehiculo_encontrado.sacar_servicio()
        else:
            print("Vehículo no encontrado")

    elif opcion == 7:
        flota.reporte()

    elif opcion == 0:
        print("Fuera del sistema")
        break


    else:
        print("Opción inválida")

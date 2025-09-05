class Dsipositivo:
    def __init__(self,nombre):
        self.nombre=nombre
        self.estado= False

    def encender (self):
        self.estado = True
        print(self.nombre, "encendido")        

    def apagar (self):
        self.estado = False
        print(self.nombre, "apagado")        

class Espcio:
    def __init__(self,nombre):
        self.nombre = nombre
        self.__dispostivos =[]

    def agregar (self, dispositivo):
        self.__dispostivos.append(dispositivo)

    def mopstrad (self):
        for dispositivo in self.__dispostivos:
            print(dispositivo.nombre)

class Casa:
    def __init__(self, direccion):
        self.direccion = direccion 
        self.__espacios= []
        
    def agregre (self, nombre):
        self. __espacios.append(Espcio(nombre))
        print("espacio agregado")
    
    def buscare(self, nombre):
        for espacio in self.__espacios:
            if espacio.nombre == nombre:
                return espacio
        return None

    def mostare (self):
        for espacio in self.__espacios:
            print(espacio.nombre)

mi_casa= Casa("calle 123")
mi_casa.agregre("cocina")
mi_casa.agregre("habitacion")
mi_casa.agregre("baño")
television = Dsipositivo("television ")
mi_casa.buscare("habitacion").agregard(television)
mi_casa.buscare("habitacion").mostrard()

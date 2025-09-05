class Persona:
    def __init__(self, nombre, cedula, ti):
        self.nombre=nombre 
        self.__cedula =cedula
        self.__ti=ti

    def obtener_documento(self):
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__ti

person1= Persona("juan", 1111, None)
persona2= Persona("Maria", 2222, None)
niño1= Persona("Isac", None, 3333)  

print("el nombre de la primera persona es ", person1.nombre)

print("la docuento de la primera persona es ", person1.obtener_documento())

print("el nombre de la segunda persona es ", persona2.nombre)


print("la documento de la primera persona es ", persona2.obtener_documento)

print("el nombre del primer niño es ", niño1.nombre)
print("la docuento del primer niño es ", niño1.obtener_documento())





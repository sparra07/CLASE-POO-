class Persona:
    def __init__(self,nombre):
        self.nombre=nombre

    def orinar(self):
        pass

class estudiante(Persona):
    def __init__(self, nombre,programa_que_estudia):
        super().__init__(nombre)
        self.programa=programa_que_estudia

    def estudiar(self):
        print(f"{self.nombre} esta estudiando")

persona1=Persona("juan", "in sistemas")
persona1.orinar
        


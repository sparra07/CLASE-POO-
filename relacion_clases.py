class estudiantes:
    def __init__(self,nombre,edad, nota):
        self.nombre=nombre
        self.edad=edad
        self.nota=nota

class Profesor:
    def __init__(self,nombre,edad, experiencia):
        self.nombre=nombre
        self.edad=edad 
        self.experiencia=experiencia

class grupo_asignatura:
    def __init__(self, nombre, horario,codigo, profesor, ):
        self.nombre=nombre
        self.hora=horario
        self.profesor=profesor
        self.codigo=codigo
        self.estudiantes=[]
    
    def Agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print("estudintes agregado correctamente")

    def promedio(self):
        acumular =0
        for estudiante in self.estudiantes:
            acumular=acumular+estudiante.nota
        promedio= acumular/len(self.estudiantes)
        return promedio
    
    def consultar(self):
        for estudiante in self.Agregar_estudiante:
            print(estudiante.nombre)

    
profesor=Profesor("Juan estebam", 35, 5)  
poo= grupo_asignatura("programacion prientada a objeto,","M-V 10-12", 62, profesor)
estudiante1=estudiantes("esteban diaz",17, 5)
estudiante2=estudiantes("jorge",20,2.5)
estudiante3=estudiantes("luis",21,3)

poo.Agregar_estudiante(estudiante1)
poo.Agregar_estudiante(estudiante2)
poo.Agregar_estudiante(estudiante3)
print(poo.promedio())
poo.consultar()

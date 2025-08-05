class estudiantes:
    def __init__(self, nombre, edad, nota_1, nota_2, nota_3):
        self.nombre=nombre 
        self.edad=edad
        self.nota_1=nota_1
        self.nota_2=nota_2
        self.nota_3=nota_3

    def mostar_nota(self):
        print("nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota1: ", self.nota_1)
        print("Nota2: ", self.nota_2)
        print("Nota3: ", self.nota_3)

    def calcular_promedio(self):
        promedio=(self.nota_1+self.nota_2+self.nota_3)/3
        return promedio
    
print("Bienvenido a la gestion del estudiantes")
print("ingrese el nombre del estudiante")
nombre=input()
print("ingrese la edad del estudiante")
edad= int(input())
print("ingrese la nota 1 ")
nota_1= float(input())
print("ingrese la nota 2 ")
nota_2= float(input())
print("ingrese la nota 3 ")
nota_3= float(input())
estudiante= estudiantes(nombre, edad, nota_1, nota_2, nota_3)

promedio_estudiantes= estudiante.calcular_promedio()
print("el promedio de: ", estudiante.nombre, "es ", promedio_estudiantes)
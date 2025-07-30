class Perro:
    def __init__(self, nombre, raza):
        self.nombre=nombre
        self.raza=raza
    
    def ladrar(selft):
        print("el perro que esta ladrando es: ", selft.nombre)
    
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre=nombre 
        self.edad=edad
        self.sexo=sexo

# vamos instanciar un objeto desde la calse perro 
print("perro #1")
perro= Perro("Tobby", "Golden")
print(perro.nombre)
print(perro.raza)

print("perro #2")
perro2=Perro("Sara","Husky")
print(perro2.nombre)
print(perro2.raza)


nombre=input("ingrese le nombre ")
raza=input("ingrese la raza ")
print("perro #3")
perro3=Perro(nombre, raza)
print(perro3.nombre)
print(perro3.raza)

print("ahora los perros van a ladrar")
perro.ladrar()
perro2.ladrar()
perro3.ladrar()
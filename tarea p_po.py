# --------------------------
# Clase Computador
# --------------------------
class Computador:
    def __init__(self, id_pc):
        self.id_pc = id_pc
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"Computador {self.id_pc} encendido.")
        else:
            print(f"Computador {self.id_pc} ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"Computador {self.id_pc} apagado.")
        else:
            print(f"Computador {self.id_pc} ya estaba apagado.")


# --------------------------    
# Clase base Usuario
# --------------------------
class Usuario:
    def __init__(self, nombre, computador):
        self.nombre = nombre
        self.activo = True
        self.computador = computador

    def activar(self):
        self.activo = True
        print(f"Usuario {self.nombre} activado.")

    def desactivar(self):
        self.activo = False
        print(f"Usuario {self.nombre} desactivado.")

    def mostrar_info(self):
        estado_usuario = "Activo" if self.activo else "Inactivo"
        estado_pc = "Prendido" if self.computador.encendido else "Apagado"
        return f"{self.nombre} - {estado_usuario}, Computador {self.computador.id_pc} ({estado_pc})"


# --------------------------
# Subclases de Usuario
# --------------------------
class Disenador(Usuario):
    def hacer_diseno(self):
        print(f"{self.nombre} está haciendo un diseño.")

class Creador(Usuario):
    def programar(self):
        print(f"{self.nombre} está programando funciones.")

class Revisor(Usuario):
    def reportar(self):
        print(f"{self.nombre} está revisando sistemas.")

class Planificador(Usuario):
    def generar_plan(self):
        print(f"{self.nombre} está generando un plan.")


# --------------------------
# Clase Red
# --------------------------
class Red:
    def __init__(self):
        self.usuarios = []
        self.computadores = []

    def agregar_usuario(self, tipo, nombre_usuario, id_pc):
        computador = Computador(id_pc)
        self.computadores.append(computador)

        if tipo == "Disenador":
            usuario = Disenador(nombre_usuario, computador)
        elif tipo == "Creador":
            usuario = Creador(nombre_usuario, computador)
        elif tipo == "Revisor":
            usuario = Revisor(nombre_usuario, computador)
        elif tipo == "Planificador":
            usuario = Planificador(nombre_usuario, computador)
        else:
            usuario = Usuario(nombre_usuario, computador)

        self.usuarios.append(usuario)
        print(f"Usuario {nombre_usuario} ({tipo}) agregado con Computador {id_pc}.")

    def eliminar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                print(f"Usuario {usuario.nombre} eliminado (Computador {usuario.computador.id_pc} sigue en la red).")
                self.usuarios.remove(usuario)
                return
        print(f"Usuario {nombre_usuario} no encontrado.")

    def buscar_usuario(self, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                return usuario
        return None

    def reporte(self):
        print("\n--- REPORTE DE LA RED ---")
        print("Usuarios:")
        if self.usuarios:
            for usuario in self.usuarios:
                print("-", usuario.mostrar_info())
        else:
            print("No hay usuarios en la red.")

        print("\nComputadores:")
        for comp in self.computadores:
            estado_pc = "Prendido" if comp.encendido else "Apagado"
            print(f"- Computador {comp.id_pc}: {estado_pc}")
        print("------------------------\n")


# --------------------------
# Menú interactivo
# --------------------------
red = Red()

print("=== Sistema de Gestión de Red ===")

while True:
    print("\nMenú:")
    print("1. Agregar usuario")
    print("2. Eliminar usuario")
    print("3. Activar usuario")
    print("4. Desactivar usuario")
    print("5. Encender computador")
    print("6. Apagar computador")
    print("7. Reporte de red")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese nombre del usuario: ")
        tipo = input("Tipo (Disenador, Creador, Revisor, Planificador): ")
        id_pc = int(input("Ingrese ID del computador: "))
        red.agregar_usuario(tipo, nombre, id_pc)

    elif opcion == "2":
        nombre = input("Ingrese nombre del usuario a eliminar: ")
        red.eliminar_usuario(nombre)

    elif opcion == "3":
        nombre = input("Ingrese nombre del usuario: ")
        usuario = red.buscar_usuario(nombre)
        if usuario:
            usuario.activar()
        else:
            print("Usuario no encontrado.")

    elif opcion == "4":
        nombre = input("Ingrese nombre del usuario: ")
        usuario = red.buscar_usuario(nombre)
        if usuario:
            usuario.desactivar()
        else:
            print("Usuario no encontrado.")

    elif opcion == "5":
        id_pc = int(input("Ingrese ID del computador: "))
        for comp in red.computadores:
            if comp.id_pc == id_pc:
                comp.encender()
                break
        else:
            print("Computador no encontrado.")

    elif opcion == "6":
        id_pc = int(input("Ingrese ID del computador: "))
        for comp in red.computadores:
            if comp.id_pc == id_pc:
                comp.apagar()
                break
        else:
            print("Computador no encontrado.")

    elif opcion == "7":
        red.reporte()

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")


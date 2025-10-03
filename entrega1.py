class Computador:
    def __init__(self, id_pc):
        self.id_pc = id_pc
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print("Computador", self.id_pc, "encendido.")
        else:
            print("Computador", self.id_pc, "ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print("Computador", self.id_pc, "apagado.")
        else:
            print("Computador", self.id_pc, "ya estaba apagado.")


class Empleado:  
    def __init__(self, nombre, computador):
        self.nombre = nombre
        self.activo = True
        self.computador = computador
        self.tarea_actual = "Ninguna"

    def activar(self):
        self.activo = True
        print("Empleado", self.nombre, "activado.")

    def desactivar(self):
        self.activo = False
        print("Empleado", self.nombre, "desactivado.")

    def mostrar_info(self):
        if self.activo:
            estado_empleado = "Activo"
        else:
            estado_empleado = "Inactivo"
        if self.computador.encendido:
            estado_pc = "Prendido"
        else:
            estado_pc = "Apagado"
        return f"{self.nombre},{estado_empleado}, Computador: {self.computador.id_pc},({estado_pc}), Desarrollando: {self.tarea_actual}"


class DisenadorInterfaces(Empleado):   
    def hacer_diseno(self):
        self.tarea_actual = "Haciendo diseño"

    def organizar_web(self):
        self.tarea_actual = "Organizando web"


class CreadorFunciones(Empleado):
    def crear_funciones(self):
        self.tarea_actual = "Creando funciones"

    def guardar_datos(self):
        self.tarea_actual = "Guardando datos"


class ConectorWeb(Empleado):
    def conectar_partes(self):
        self.tarea_actual = "Conectando partes"

    def entregar_web(self):
        self.tarea_actual = "Entregando web"


class RevisorSistemas(Empleado):
    def revisar_sistema(self):
        self.tarea_actual = "Revisando sistema"

    def reportar_fallas(self):
        self.tarea_actual = "Reportando fallas"


class PlanificadorTareas(Empleado):
    def planear_tareas(self):
        self.tarea_actual = "Planeando tareas"

    def revisar_equipo(self):
        self.tarea_actual = "Revisando equipo"


class Red:
    def __init__(self):
        self.empleados = []
        self.computadores = []

    def agregar_empleado(self, tipo, nombre_empleado, id_pc):
        computador = Computador(id_pc)
        self.computadores.append(computador)

        if tipo == "DisenadorInterfaces":
            empleado = DisenadorInterfaces(nombre_empleado, computador)
            print("Seleccione tarea: 1. Hacer diseño  2. Organizar web")
            tarea = input("Opción: ")
            if tarea == "1":
                empleado.hacer_diseno()
            elif tarea == "2":
                empleado.organizar_web()

        elif tipo == "CreadorFunciones":
            empleado = CreadorFunciones(nombre_empleado, computador)
            print("Seleccione tarea: 1. Crear funciones  2. Guardar datos")
            tarea = input("Opción: ")
            if tarea == "1":
                empleado.crear_funciones()
            elif tarea == "2":
                empleado.guardar_datos()

        elif tipo == "ConectorWeb":
            empleado = ConectorWeb(nombre_empleado, computador)
            print("Seleccione tarea: 1. Conectar partes  2. Entregar web")
            tarea = input("Opción: ")
            if tarea == "1":
                empleado.conectar_partes()
            elif tarea == "2":
                empleado.entregar_web()

        elif tipo == "RevisorSistemas":
            empleado = RevisorSistemas(nombre_empleado, computador)
            print("Seleccione tarea: 1. Revisar sistema  2. Reportar fallas")
            tarea = input(" Opción: ")
            if tarea == "1":
                empleado.revisar_sistema()
            elif tarea == "2":
                empleado.reportar_fallas()

        elif tipo == "PlanificadorTareas":
            empleado = PlanificadorTareas(nombre_empleado, computador)
            print("Seleccione tarea: 1. Planear tareas  2. Revisar equipo")
            tarea = input("Opción: ")
            if tarea == "1":
                empleado.planear_tareas()
            elif tarea == "2":
                empleado.revisar_equipo()

        else:
            empleado = Empleado(nombre_empleado, computador)  

        self.empleados.append(empleado)
        print("Empleado ", nombre_empleado, tipo, "agregado con Computador", id_pc,)
        print("Tarea asignada:", empleado.tarea_actual)

    def eliminar_empleado(self, nombre_empleado):
        for empleado in self.empleados:
            if empleado.nombre == nombre_empleado:
                print("Empleado" ,empleado.nombre, "eliminado (Computador ",empleado.computador.id_pc, "sigue en la red")
                self.empleados.remove(empleado)
                return
        print("Empleado",nombre_empleado, "no encontrado")

    def buscar_empleado(self, nombre_empleado):
        for empleado in self.empleados:
            if empleado.nombre == nombre_empleado:
                return empleado
        return None

    def reporte(self):
        print("REPORTE DE LA RED")
        print("Empleados:")
        if self.empleados:
            for empleado in self.empleados:
                print(empleado.mostrar_info())
        else:
            print("No hay empleados en la red.")

        print("Computadores:")
        for comp in self.computadores:
            if comp.encendido:
                estado_pc = "Prendido" 
            else:
                estado_pc = "Apagado"
            print("Computador",comp.id_pc,":" ,estado_pc)
 


red = Red()

print("Gestión de Red ")

while True:
    print("Menú:")
    print("1. Agregar empleado")
    print("2. Eliminar empleado")
    print("3. Activar empleado")
    print("4. Desactivar empleado")
    print("5. Encender computador")
    print("6. Apagar computador")
    print("7. Reporte de red")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese nombre del empleado: ")
        tipo = input("Tipo (DisenadorInterfaces, CreadorFunciones, ConectorWeb, RevisorSistemas, PlanificadorTareas): ")
        id_pc = int(input("Ingrese ID del computador: "))
        red.agregar_empleado(tipo, nombre, id_pc)

    elif opcion == "2":
        nombre = input("Ingrese nombre del empleado a eliminar: ")
        red.eliminar_empleado(nombre)

    elif opcion == "3":
        nombre = input("Ingrese nombre del empleado: ")
        empleado = red.buscar_empleado(nombre)
        if empleado:
            empleado.activar()
        else:
            print("Empleado no encontrado.")

    elif opcion == "4":
        nombre = input("Ingrese nombre del empleado: ")
        empleado = red.buscar_empleado(nombre)
        if empleado:
            empleado.desactivar()
        else:
            print("Empleado no encontrado.")

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

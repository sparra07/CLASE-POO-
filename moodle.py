class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def presentarse(self):
        return f"Hola, soy {self.nombre}. Mi correo es {self.correo}"


class Empleado(Persona):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo)
        self.salario = salario

    def calcular_bono(self):
        return 0


class Desarrollador(Empleado):
    def __init__(self, nombre, correo, salario, lenguaje):
        super().__init__(nombre, correo, salario)
        self.lenguaje = lenguaje

    def calcular_bono(self, proyecto=None):
        bono = self.salario * 0.10
        if proyecto is not None and len(proyecto.tareas) > 5:
            bono += self.salario * 0.01
        return bono


class Analista(Empleado):
    def __init__(self, nombre, correo, salario, nivel):
        super().__init__(nombre, correo, salario)
        self.nivel = nivel

    def calcular_bono(self):
        bono = self.salario * 0.08
        if self.nivel.lower() == "senior":
            bono += self.salario * 0.03
        return bono


class Gerente(Empleado):
    def __init__(self, nombre, correo, salario):
        super().__init__(nombre, correo, salario)
        self.equipo = []

    def agregar_empleado(self, empleado):
        if empleado not in self.equipo and empleado is not self:
            self.equipo.append(empleado)


    def remover_empleado(self, empleado):
        if empleado in self.equipo:
            self.equipo.remove(empleado)

    def listar_equipo(self):
        return [empleado.nombre for empleado in self.equipo]

    def calcular_bono(self):
        return self.salario * 0.15


class Tarea:
    def __init__(self, id_tarea, descripcion, horas):
        if horas < 0:
            print("Error: no se pueden poner horas negativas")
            horas = 0
        self.id_tarea = id_tarea
        self.descripcion = descripcion
        self.horas = horas
        self.asignado_a = None


class Proyecto:
    def __init__(self, nombre, presupuesto):
        self.nombre = nombre
        self.presupuesto = presupuesto
        self.tareas = []
        self.contador_tareas = 0

    def agregar_tarea(self, descripcion, horas):
        self.contador_tareas += 1
        tarea = Tarea(self.contador_tareas, descripcion, horas)
        self.tareas.append(tarea)

    def asignar_empleado(self, id_tarea, empleado):
        for tarea in self.tareas:
            if tarea.id_tarea == id_tarea:
                tarea.asignado_a = empleado

    def listar_tareas(self):
        lista = []
        for tarea in self.tareas:
            if tarea.asignado_a:
                asignado = tarea.asignado_a.nombre 
            else:
                asignado="Nadie"
            texto = f"{tarea.id_tarea}: {tarea.descripcion} ({tarea.horas}h), {asignado}"
            lista.append(texto)
        return lista


class Empresa:
    def __init__(self):
        self.empleados = []
        self.proyectos = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def crear_proyecto(self, nombre, presupuesto):
        proyecto = Proyecto(nombre, presupuesto)
        self.proyectos.append(proyecto)
        return proyecto

    def asignar_empleado_a_proyecto(self, proyecto, id_tarea, empleado):
        proyecto.asignar_empleado(id_tarea, empleado)

print("Gestión de Empresa")

empresa = Empresa()

while True:
    print("Menú:")
    print("1. Agregar empleado")
    print("2. Crear proyecto")
    print("3. Agregar tarea")
    print("4. Asignar empleado a tarea")
    print("5. Listar empleados")
    print("6. Listar proyectos y tareas")
    print("7. Calcular bonos")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("Tipos de empleado:")
        print("1. Desarrollador")
        print("2. Analista")
        print("3. Gerente")
        tipo = input("Seleccione tipo: ")

        nombre = input("Ingrese nombre: ")
        correo = input("Ingrese correo: ")
        salario = float(input("Ingrese salario: "))

        if tipo == "1":
            lenguaje = input("Lenguaje principal que usa: ")
            empleado = Desarrollador(nombre, correo, salario, lenguaje)

        elif tipo == "2":
            nivel = input("Nivel (junior/senior): ")
            empleado = Analista(nombre, correo, salario, nivel)

        elif tipo == "3":
            empleado = Gerente(nombre, correo, salario)

        else:
            print("Tipo inválido.")
            continue

        empresa.agregar_empleado(empleado)
        print(f"Empleado {empleado.nombre} agregado.")

    elif opcion == "2":
        nombre = input("Nombre del proyecto: ")
        presupuesto = float(input("Presupuesto: "))
        proyecto = empresa.crear_proyecto(nombre, presupuesto)
        print(f"Proyecto '{proyecto.nombre}' creado.")

    elif opcion == "3":
        if not empresa.proyectos:
            print("Primero debe crear un proyecto.")
        else:
            proyecto = empresa.proyectos[0]   
            descripcion = input("Descripción de la tarea: ")
            horas = int(input("Horas estimadas: "))
            proyecto.agregar_tarea(descripcion, horas)
            print("Tarea agregada al proyecto.")

    elif opcion == "4":
        if not empresa.proyectos or not empresa.empleados:
            print("Debe existir al menos un proyecto y un empleado.")
        else:
            proyecto = empresa.proyectos[0]   

            for tarea in proyecto.listar_tareas():
                print(tarea)

            id_tarea = int(input("Ingrese ID de la tarea: "))

            for i in range(len(empresa.empleados)):
                empleado = empresa.empleados[i]
                print(f"{i+1}. {empleado.nombre}")

            indice_empleado = int(input("Seleccione empleado: ")) - 1
            empleado = empresa.empleados[indice_empleado]

            empresa.asignar_empleado_a_proyecto(proyecto, id_tarea, empleado)
            print(f"Empleado {empleado.nombre} asignado a la tarea {id_tarea}.")

    elif opcion == "5":
        if not empresa.empleados:
            print("No hay empleados registrados.")
        else:
            for i in range(len(empresa.empleados)):
                empleado = empresa.empleados[i]
                print(f"{empleado.nombre}")

    elif opcion == "6":
        if not empresa.proyectos:
            print("No hay proyectos creados.")
        else:
            for p in empresa.proyectos:
                print(f"\nProyecto: {p.nombre}")
                for tarea in p.listar_tareas():
                    print("  ", tarea)

    elif opcion == "7":
        if not empresa.empleados:
            print("No hay empleados registrados.")
        else:
            for i in range(len(empresa.empleados)):
                empleado = empresa.empleados[i]
                bono = empleado.calcular_bono()
                print(f"{empleado.nombre}, Bono: {bono}")

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")

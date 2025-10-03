from dataclasses import dataclass, field
@dataclass
class Computador:
    id_pc_: str
    encendido: bool= field(default=False)


@dataclass
class Empleado:
    nombre:str
    activo:bool=field(default=False)
    computador: computador
    tarea_actual= str= field(default="Ninguna")
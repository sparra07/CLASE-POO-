from dataclasses import dataclass, field
from typing import list

@dataclass
class Producto:
    codigo:int
    nombre:str
    categoria:str
    precio:float

@dataclass
class Cliente:
    id: int
    nombre: str
    vip:bool

@dataclass
class Linea_Factura:
    producto:(Producto)
    cantidad:int

    @property
    def subtotal(self)-> float:
        return self.producto.precio * self.cantidad
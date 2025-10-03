from abc import ABC, abstractmethod
from typing import List
from aplicacionventas.modelos import Cliente, Linea_Factura

class Impuesto(ABC):
    @abstractmethod
    def calcular(self,cliente: Cliente, linea: Linea_Factura)-> float:
        ...

class iva(Impuesto):
    def calcular(self,cliente: Cliente, linea: Linea_Factura)-> float:
        return linea.subtotal *0.19 if linea.producto.categoria !="alimentos" else 0.0
        
            
class Exentos(Impuesto):
    def calcular(self,cliente: Cliente, linea: Linea_Factura)-> float:    
        return linea.subtotal * 0.19 if linea.producto.categoria != "servicios" else 0.0

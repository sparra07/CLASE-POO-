from dataclasses import dataclass, field
from typing import List
from aplicacionventas.modelos import Cliente, Linea_Factura
from modelos import Cliente, Linea_Factura, Producto
from descunetos import Descuento
from impuestos import Impuesto

@dataclass 
class Factura:
    cliente:Cliente
    lineas:List[Linea_Factura]= field(default_factory=list)

    def agegar_linea(self, producto:Producto, cantidad=1):
        self.lineas.append(Linea_Factura(producto,cantidad))

    def calcular_descuento(self, descuento:Descuento):
        return sum(descuento.aplicar(self.cliente, 1) for l in self.lineas)
    
    def calcular_impuesto(self, impuesto: Impuesto):
        return sum(impuesto.aplicar(self.cliente, 1) for l in self.lineas)
    
    def calcular_total(self, descuneto: Descuento, impuesto:Impuesto):
        return sum(l.subtotal for l in self.lineas)+ self.calcular_impuesto(impuesto)-self.calcular_descuento(descuneto)

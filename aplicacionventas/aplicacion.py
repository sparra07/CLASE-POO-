from modelos import Producto, Cliente
from pedido import Factura
from descunetos import DescuentoVIP, DescuentoVolumen
from impuestos import iva, Exentos

cliente= Cliente(123, "juan", False)
prodcuto1=Producto(567, "arepas", "alimentos", 2000)
prodcuto2=Producto(949, "subscribcion netflix", "servivios", 25000)
prodcuto3 = Producto(111, "computador", "tecnologia", 2500000)

mi_factura =Factura(cliente)

mi_factura.agegar_linea(prodcuto1, 10)
descuento_a_aplicar =DescuentoVolumen()
impuesto_a_aplicar = iva()

print(mi_factura.calcular_total(descuento_a_aplicar, impuesto_a_aplicar))
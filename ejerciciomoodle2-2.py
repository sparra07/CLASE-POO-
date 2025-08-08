class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def compras(self, num_compras):
        if num_compras > 5:
            print("El sistema solo permite comprar 5 unidades de cada producto")
        elif self.cantidad_disponible >= num_compras:
            self.cantidad_disponible=self.cantidad_disponible - num_compras 
            print("Venta de", num_compras, "unidades de:", self.nombre)
        else:
            print("Venta inválida: no hay suficientes productos de:", self.nombre)

# Lista de productos
productos = [
    Producto("gaseosa", 3000, 3),
    Producto("papas", 2500, 5),
    Producto("cicles", 2000, 4),
    Producto("galletas oreo", 1500, 2)
]

#Productos con índice
print("Productos disponibles:")
print("0:", productos[0].nombre, "$",productos[0].precio, productos[0].cantidad_disponible, "unidades")
print("1:", productos[1].nombre, "$",productos[0].precio, productos[1].cantidad_disponible, "unidades")
print("2:", productos[2].nombre, "$",productos[0].precio, productos[2].cantidad_disponible, "unidades")
print("3:", productos[3].nombre, "$",productos[0].precio, productos[3].cantidad_disponible, "unidades")

# Elegir producto por índice
indice = int(input("Elige el índice del producto quieres comprar comprar: "))

if indice == 0:
    cantidad = int(input("¿cuantas unidadees quieres comprar?: "))
    productos[0].compras(cantidad)
elif indice == 1:
    cantidad = int(input("¿cuantas unidadees quieres comprar?: "))
    productos[1].compras(cantidad)
elif indice == 2:
    cantidad = int(input("¿cuantas unidadees quieres comprar?: "))
    productos[2].compras(cantidad)
elif indice == 3:
    cantidad = int(input("¿cuantas unidadees quieres comprar?: "))
    productos[3].compras(cantidad)
else:
    print("Índice incorrecto.")

print("Productos restantes:")
print("0:", productos[0].nombre, "$",productos[0].precio, productos[0].cantidad_disponible, "unidades")
print("1:", productos[1].nombre, "$",productos[0].precio, productos[1].cantidad_disponible, "unidades")
print("2:", productos[2].nombre, "$",productos[0].precio, productos[2].cantidad_disponible, "unidades")
print("3:", productos[3].nombre, "$",productos[0].precio, productos[3].cantidad_disponible, "unidades")

class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def ventas(self, num_ventas):
        if num_ventas > 5:
            print("El sistema solo permite vender 5 unidades de cada producto")
        elif self.cantidad_disponible >= num_ventas:
            self.cantidad_disponible - num_ventas 
            print("Venta de", num_ventas, "unidades de:", self.nombre)
        else:
            print("Venta inválida: no hay suficientes productos de:", self.nombre)

# Lista de productos
productos = [
    Producto("Pan", 3000, 3),
    Producto("Jugo", 2000, 5),
    Producto("Galletas", 5000, 4),
    Producto("Arroz", 3500, 2)
]

# Mostrar productos con índice y cantidad
print("Productos disponibles:")
print("Índice 0:", productos[0].nombre, "-", productos[0].cantidad_disponible, "unidades")
print("Índice 1:", productos[1].nombre, "-", productos[1].cantidad_disponible, "unidades")
print("Índice 2:", productos[2].nombre, "-", productos[2].cantidad_disponible, "unidades")
print("Índice 3:", productos[3].nombre, "-", productos[3].cantidad_disponible, "unidades")

# Elegir producto por índice
indice = int(input("Elige el índice del producto que deseas comprar: "))

if indice == 0:
    cantidad = int(input("¿Cuántas unidades de Pan quieres comprar?: "))
    productos[0].ventas(cantidad)
elif indice == 1:
    cantidad = int(input("¿Cuántas unidades de Jugo quieres comprar?: "))
    productos[1].ventas(cantidad)
elif indice == 2:
    cantidad = int(input("¿Cuántas unidades de Galletas quieres comprar?: "))
    productos[2].ventas(cantidad)
elif indice == 3:
    cantidad = int(input("¿Cuántas unidades de Arroz quieres comprar?: "))
    productos[3].ventas(cantidad)
else:
    print("Índice no válido.")

print(" cantidad de productos acutuales")
print("Índice 0:", productos[0].nombre, "-", productos[0].cantidad_disponible, "unidades")
print("Índice 1:", productos[1].nombre, "-", productos[1].cantidad_disponible, "unidades")
print("Índice 2:", productos[2].nombre, "-", productos[2].cantidad_disponible, "unidades")
print("Índice 3:", productos[3].nombre, "-", productos[3].cantidad_disponible, "unidades")
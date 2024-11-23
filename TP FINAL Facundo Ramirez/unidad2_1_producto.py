class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad_disponible = nueva_cantidad

    def ajustar_cantidad(self, cantidad):
        self.cantidad_disponible += cantidad

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad disponible: {self.cantidad_disponible}"

# Ejemplo de uso
producto = Producto("Laptop", 1200.00, 10)

# Mostrar información del producto
print(producto.mostrar_informacion())

# Actualizar la cantidad disponible
producto.actualizar_cantidad(5)
print("\nDespués de actualizar la cantidad:")
print(producto.mostrar_informacion())

# Ajustar la cantidad disponible (incrementar en 3)
producto.ajustar_cantidad(3)
print("\nDespués de ajustar la cantidad (incrementar en 3):")
print(producto.mostrar_informacion())

# Ajustar la cantidad disponible (decrementar en 2)
producto.ajustar_cantidad(-2)
print("\nDespués de ajustar la cantidad (decrementar en 2):")
print(producto.mostrar_informacion())

class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
    
    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad_disponible = nueva_cantidad
    
    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Disponibles: {self.cantidad_disponible}"
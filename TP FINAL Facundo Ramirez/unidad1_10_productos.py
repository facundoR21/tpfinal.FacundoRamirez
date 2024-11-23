class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_descuento(self):
        pass

class ProductoDescuento(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento

    def calcular_precio_descuento(self):
        return self.precio * (1 - self.descuento / 100)

class ProductoNormal(Producto):
    def calcular_precio_descuento(self):
        return self.precio

# Ejemplo de uso
producto_descuento = ProductoDescuento("Laptop", 1000, 10)  # 10% de descuento
producto_normal = ProductoNormal("Mouse", 50)

print(f"Precio con descuento de {producto_descuento.nombre}: ${producto_descuento.calcular_precio_descuento()}")
print(f"Precio de {producto_normal.nombre} sin descuento: ${producto_normal.calcular_precio_descuento()}")

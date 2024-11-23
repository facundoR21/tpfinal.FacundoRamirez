class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}: ${self.precio}"

class ProductoElectronico(Producto):
    def __init__(self, nombre, precio, garantia):
        super().__init__(nombre, precio)
        self.garantia = garantia

    def __str__(self):
        return f"{self.nombre} (Garantía: {self.garantia} años): ${self.precio}"

class CarritoCompra:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def eliminar_producto(self, nombre_producto):
        self.productos = [producto for producto in self.productos if producto.nombre != nombre_producto]

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)

    def mostrar_carrito(self):
        print("Carrito de Compra:")
        for producto in self.productos:
            print(producto)
        print(f"Total: ${self.calcular_total()}")

# Ejemplo de uso
producto1 = Producto("Manzanas", 3.50)
producto2 = Producto("Pan", 2.00)
producto3 = ProductoElectronico("Smartphone", 299.99, 2)

carrito = CarritoCompra()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)
carrito.agregar_producto(producto3)

carrito.mostrar_carrito()

carrito.eliminar_producto("Pan")
print("\nDespués de eliminar un producto:")
carrito.mostrar_carrito()

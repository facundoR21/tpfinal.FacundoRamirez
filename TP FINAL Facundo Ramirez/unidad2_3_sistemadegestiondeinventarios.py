class Producto:
    def __init__(self, id_producto, nombre, precio, proveedor):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.proveedor = proveedor

class Proveedor:
    def __init__(self, id_proveedor, nombre, contacto):
        self.id_proveedor = id_proveedor
        self.nombre = nombre
        self.contacto = contacto

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto.id_producto in self.productos:
            self.productos[producto.id_producto]['cantidad'] += cantidad
        else:
            self.productos[producto.id_producto] = {'producto': producto, 'cantidad': cantidad}

    def actualizar_existencias(self, id_producto, cantidad):
        if id_producto in self.productos:
            self.productos[id_producto]['cantidad'] = cantidad
        else:
            print("El producto no existe en el inventario.")

    def mostrar_inventario(self):
        for id_producto, info in self.productos.items():
            producto = info['producto']
            cantidad = info['cantidad']
            print(f"ID: {id_producto}, Nombre: {producto.nombre}, Cantidad: {cantidad}, Precio: {producto.precio}, Proveedor: {producto.proveedor.nombre}")

# Ejemplo de uso:
proveedor1 = Proveedor(1, "Proveedor 1", "contacto@proveedor1.com")
producto1 = Producto(101, "Producto 1", 50.0, proveedor1)

inventario = Inventario()
inventario.agregar_producto(producto1, 10)
inventario.mostrar_inventario()

inventario.actualizar_existencias(101, 20)
inventario.mostrar_inventario()

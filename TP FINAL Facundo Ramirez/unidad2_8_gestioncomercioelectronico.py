class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f'Producto(id={self.id_producto}, nombre={self.nombre}, precio={self.precio}, stock={self.stock})'

class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.productos.append((producto, cantidad))
            producto.stock -= cantidad
        else:
            print(f"No hay suficiente stock de {producto.nombre}.")

    def eliminar_producto(self, id_producto):
        self.productos = [item for item in self.productos if item[0].id_producto != id_producto]

    def total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self.productos)

    def __str__(self):
        return f'Carrito({[str(producto) for producto, cantidad in self.productos]})'

class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f'Usuario(id={self.id_usuario}, nombre={self.nombre}, email={self.email})'

class Cliente(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)
        self.carrito = Carrito()

    def realizar_pedido(self):
        pedido = Pedido(self, self.carrito)
        self.carrito = Carrito()  # Crear un nuevo carrito después de realizar el pedido
        return pedido

class Administrador(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)

    def agregar_producto(self, inventario, producto):
        inventario.append(producto)

    def eliminar_producto(self, inventario, id_producto):
        inventario = [producto for producto in inventario if producto.id_producto != id_producto]
        return inventario

class Pedido:
    def __init__(self, cliente, carrito):
        self.cliente = cliente
        self.productos = carrito.productos
        self.total = carrito.total()

    def __str__(self):
        return f'Pedido(cliente={self.cliente.nombre}, total={self.total}, productos={self.productos})'

# Ejemplo de uso:
inventario = []

admin = Administrador(1, 'Admin', 'admin@ecommerce.com')
cliente = Cliente(2, 'Facundo', 22, 'facundo@ejemplo.com')

producto1 = Producto(1, 'Laptop', 1000, 10)
producto2 = Producto(2, 'Smartphone', 500, 20)

admin.agregar_producto(inventario, producto1)
admin.agregar_producto(inventario, producto2)

cliente.carrito.agregar_producto(producto1, 1)
cliente.carrito.agregar_producto(producto2, 2)

pedido = cliente.realizar_pedido()
print(pedido)

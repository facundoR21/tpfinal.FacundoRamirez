class Vehiculo:
    def __init__(self, id_vehiculo, marca, modelo, capacidad):
        self.id_vehiculo = id_vehiculo
        self.marca = marca
        self.modelo = modelo
        self.capacidad = capacidad

    def __str__(self):
        return f'Vehiculo(id={self.id_vehiculo}, marca={self.marca}, modelo={self.modelo}, capacidad={self.capacidad})'

class Automovil(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, capacidad):
        super().__init__(id_vehiculo, marca, modelo, capacidad)

class Camion(Vehiculo):
    def __init__(self, id_vehiculo, marca, modelo, capacidad):
        super().__init__(id_vehiculo, marca, modelo, capacidad)

class Ruta:
    def __init__(self, id_ruta, origen, destino, duracion):
        self.id_ruta = id_ruta
        self.origen = origen
        self.destino = destino
        self.duracion = duracion
        self.conductor = None
        self.clientes = []

    def asignar_conductor(self, conductor):
        self.conductor = conductor

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def __str__(self):
        return f'Ruta(id={self.id_ruta}, origen={self.origen}, destino={self.destino}, duracion={self.duracion}, conductor={self.conductor.nombre if self.conductor else "N/A"}, clientes={len(self.clientes)})'

class Conductor:
    def __init__(self, id_conductor, nombre, licencia):
        self.id_conductor = id_conductor
        self.nombre = nombre
        self.licencia = licencia

    def __str__(self):
        return f'Conductor(id={self.id_conductor}, nombre={self.nombre}, licencia={self.licencia})'

class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f'Cliente(id={self.id_cliente}, nombre={self.nombre}, email={self.email})'

# Ejemplo de uso:
automovil1 = Automovil(1, 'Toyota', 'Corolla', 5)
camion1 = Camion(2, 'Mercedes', 'Actros', 20)

conductor1 = Conductor(1, 'Carlos', 'L12345')
cliente1 = Cliente(1, 'Facundo', 'facundo@yahoo.com')
cliente2 = Cliente(2, 'María', 'maria@yahoo.com')

ruta1 = Ruta(1, 'Buenos Aires', 'Córdoba', 7)
ruta1.asignar_conductor(conductor1)
ruta1.agregar_cliente(cliente1)
ruta1.agregar_cliente(cliente2)

print(automovil1)
print(camion1)
print(conductor1)
print(cliente1)
print(cliente2)
print(ruta1)


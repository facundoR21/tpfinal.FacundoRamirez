class Ciudadano:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def __str__(self):
        return f'Ciudadano(nombre={self.nombre}, edad={self.edad}, ocupacion={self.ocupacion})'


class Edificio:
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad

    def __str__(self):
        return f'Edificio(nombre={self.nombre}, tipo={self.tipo}, capacidad={self.capacidad})'


class Vehículo:
    def __init__(self, modelo, tipo, capacidad):
        self.modelo = modelo
        self.tipo = tipo
        self.capacidad = capacidad

    def __str__(self):
        return f'Vehículo(modelo={self.modelo}, tipo={self.tipo}, capacidad={self.capacidad})'


class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ciudadanos = []
        self.edificios = []
        self.vehiculos = []
        self.economia = 0
        self.seguridad = 0

    def agregar_ciudadano(self, ciudadano):
        self.ciudadanos.append(ciudadano)

    def agregar_edificio(self, edificio):
        self.edificios.append(edificio)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def actualizar_economia(self, cantidad):
        self.economia += cantidad

    def actualizar_seguridad(self, cantidad):
        self.seguridad += cantidad

    def mostrar_ciudad(self):
        print(f'Ciudad: {self.nombre}')
        print(f'Economía: {self.economia}')
        print(f'Seguridad: {self.seguridad}')
        print('Ciudadanos:')
        for ciudadano in self.ciudadanos:
            print(ciudadano)
        print('Edificios:')
        for edificio in self.edificios:
            print(edificio)
        print('Vehículos:')
        for vehiculo in self.vehiculos:
            print(vehiculo)

# Ejemplo de uso:
ciudad = Ciudad('Ciudad Ejemplo')

ciudadano1 = Ciudadano('Juan', 30, 'Ingeniero')
ciudadano2 = Ciudadano('María', 25, 'Doctora')
ciudad.agregar_ciudadano(ciudadano1)
ciudad.agregar_ciudadano(ciudadano2)

edificio1 = Edificio('Hospital Central', 'Hospital', 500)
edificio2 = Edificio('Escuela Primaria', 'Escuela', 300)
ciudad.agregar_edificio(edificio1)
ciudad.agregar_edificio(edificio2)

vehiculo1 = Vehículo('Toyota Corolla', 'Automóvil', 5)
vehiculo2 = Vehículo('Autobús Escolar', 'Autobús', 50)
ciudad.agregar_vehiculo(vehiculo1)
ciudad.agregar_vehiculo(vehiculo2)

ciudad.actualizar_economia(100000)
ciudad.actualizar_seguridad(80)

ciudad.mostrar_ciudad()

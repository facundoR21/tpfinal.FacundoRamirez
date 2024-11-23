class Vehiculo:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def mostrar_informacion(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Color: {self.color}')

class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, numero_puertas):
        super().__init__(marca, modelo, color)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Número de puertas: {self.numero_puertas}')

    def conducir(self):
        print(f'El coche {self.marca} {self.modelo} está conduciendo.')

class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, tipo):
        super().__init__(marca, modelo, color)
        self.tipo = tipo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Tipo: {self.tipo}')

    def conducir(self):
        print(f'La moto {self.marca} {self.modelo} está conduciendo.')

# Ejemplo de uso
coche1 = Coche('Toyota', 'Corolla', 'Rojo', 4)
moto1 = Moto('Yamaha', 'MT-07', 'Negra', 'Deportiva')

coche1.mostrar_informacion()
coche1.conducir()

moto1.mostrar_informacion()
moto1.conducir()

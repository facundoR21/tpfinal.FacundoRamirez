class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def ladrar(self):
        print(f'{self.nombre} está ladrando.')

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Raza: {self.raza}')

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def maullar(self):
        print(f'{self.nombre} está maullando.')

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Color: {self.color}')

class Pajaro(Animal):
    def __init__(self, nombre, edad, tipo):
        super().__init__(nombre, edad)
        self.tipo = tipo

    def volar(self):
        print(f'{self.nombre} está volando.')

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Tipo: {self.tipo}')

# Ejemplo de uso
perro1 = Perro('Buddy', 4, 'Golden Retriever')
gato1 = Gato('Whiskers', 2, 'Blanco')
pajaro1 = Pajaro('Tweety', 1, 'Canario')

perro1.mostrar_informacion()
perro1.ladrar()

gato1.mostrar_informacion()
gato1.maullar()

pajaro1.mostrar_informacion()
pajaro1.volar()

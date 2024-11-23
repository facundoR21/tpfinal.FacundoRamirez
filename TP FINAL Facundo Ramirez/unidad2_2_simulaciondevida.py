from abc import ABC, abstractmethod

class Ser(ABC):
    def __init__(self, nombre, energia, salud, edad):
        self.nombre = nombre
        self.energia = energia
        self.salud = salud
        self.edad = edad

    @abstractmethod
    def comportamiento(self):
        pass

    def envejecer(self):
        self.edad += 1
        self.energia -= 10
        self.salud -= 5

    def mostrar_estado(self):
        return f"{self.nombre} - Energía: {self.energia}, Salud: {self.salud}, Edad: {self.edad}"

class Planta(Ser):
    def comportamiento(self):
        self.energia += 5
        return f"{self.nombre} está realizando fotosíntesis."

class Animal(Ser):
    def __init__(self, nombre, energia, salud, edad, especie):
        super().__init__(nombre, energia, salud, edad)
        self.especie = especie

    def comportamiento(self):
        self.energia -= 5
        return f"{self.nombre} está buscando comida."

class Persona(Ser):
    def __init__(self, nombre, energia, salud, edad, ocupacion):
        super().__init__(nombre, energia, salud, edad)
        self.ocupacion = ocupacion

    def comportamiento(self):
        self.energia -= 10
        return f"{self.nombre} está trabajando como {self.ocupacion}."

def simular_dia(ser):
    print(ser.mostrar_estado())
    print(ser.comportamiento())
    ser.envejecer()
    print("Después de un día:")
    print(ser.mostrar_estado())
    print()

# Ejemplo de uso
planta = Planta("Rosa", 50, 100, 2)
animal = Animal("León", 80, 90, 5, "Felino")
persona = Persona("Juan", 70, 85, 30, "Ingeniero")

seres = [planta, animal, persona]

for ser in seres:
    simular_dia(ser)

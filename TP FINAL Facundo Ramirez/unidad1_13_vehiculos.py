from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass

    @abstractmethod
    def frenar(self):
        pass

class Coche(Vehiculo):
    def acelerar(self):
        return f"El coche {self.marca} {self.modelo} está acelerando."

    def frenar(self):
        return f"El coche {self.marca} {self.modelo} está frenando."

class Moto(Vehiculo):
    def acelerar(self):
        return f"La moto {self.marca} {self.modelo} está acelerando."

    def frenar(self):
        return f"La moto {self.marca} {self.modelo} está frenando."

class Bicicleta(Vehiculo):
    def acelerar(self):
        return f"La bicicleta {self.marca} {self.modelo} está acelerando."

    def frenar(self):
        return f"La bicicleta {self.marca} {self.modelo} está frenando."

# Ejemplo de uso
coche = Coche("Toyota", "Corolla")
moto = Moto("Yamaha", "MT-07")
bicicleta = Bicicleta("Giant", "Escape 3")

print(coche.acelerar())
print(coche.frenar())
print(moto.acelerar())
print(moto.frenar())
print(bicicleta.acelerar())
print(bicicleta.frenar())


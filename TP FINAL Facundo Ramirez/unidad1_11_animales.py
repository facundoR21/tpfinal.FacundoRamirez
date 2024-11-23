from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

    @abstractmethod
    def moverse(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

    def moverse(self):
        return "El perro corre"

class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"

    def moverse(self):
        return "El gato salta"

class Pajaro(Animal):
    def hacer_sonido(self):
        return "Pío"

    def moverse(self):
        return "El pájaro vuela"

# Ejemplo de uso
perro = Perro()
gato = Gato()
pajaro = Pajaro()

print(f"El perro hace: {perro.hacer_sonido()} y {perro.moverse()}")
print(f"El gato hace: {gato.hacer_sonido()} y {gato.moverse()}")
print(f"El pájaro hace: {pajaro.hacer_sonido()} y {pajaro.moverse()}")

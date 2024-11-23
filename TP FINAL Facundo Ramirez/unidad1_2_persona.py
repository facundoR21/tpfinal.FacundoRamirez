class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def imprimir_datos(self):
        print(f'Nombre: {self.nombre}, Edad: {self.edad}')

# Ejemplo de uso
persona1 = Persona('Facundo', 22)
persona1.imprimir_datos()

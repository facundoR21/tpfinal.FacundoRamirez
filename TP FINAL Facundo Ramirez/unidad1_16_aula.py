class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Estudiante(Persona):
    def __init__(self, nombre, grado):
        super().__init__(nombre)
        self.grado = grado

    def __str__(self):
        return f"{self.nombre}, Grado: {self.grado}"

class Profesor(Persona):
    def __init__(self, nombre, materia):
        super().__init__(nombre)
        self.materia = materia

    def __str__(self):
        return f"Profesor: {self.nombre}, Materia: {self.materia}"

class Aula:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def eliminar_estudiante(self, nombre_estudiante):
        self.estudiantes = [estudiante for estudiante in self.estudiantes if estudiante.nombre != nombre_estudiante]

    def cambiar_profesor(self, nuevo_profesor):
        self.profesor = nuevo_profesor

    def mostrar_aula(self):
        print(f"Aula: {self.nombre}")
        print(self.profesor)
        print("Estudiantes:")
        for estudiante in self.estudiantes:
            print(estudiante)

# Ejemplo de uso
profesor = Profesor("Juan Pérez", "Matemáticas")
aula = Aula("Aula 101", profesor)

estudiante1 = Estudiante("Ana García", 5)
estudiante2 = Estudiante("Luis Martínez", 5)
estudiante3 = Estudiante("María López", 5)

aula.agregar_estudiante(estudiante1)
aula.agregar_estudiante(estudiante2)
aula.agregar_estudiante(estudiante3)

aula.mostrar_aula()

aula.eliminar_estudiante("Luis Martínez")
print("\nDespués de eliminar un estudiante:")
aula.mostrar_aula()

nuevo_profesor = Profesor("Laura Gómez", "Ciencias")
aula.cambiar_profesor(nuevo_profesor)
print("\nDespués de cambiar al profesor:")
aula.mostrar_aula()

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona(nombre={self.nombre}, edad={self.edad})'

class Estudiante(Persona):
    def __init__(self, nombre, edad, id_estudiante):
        super().__init__(nombre, edad)
        self.id_estudiante = id_estudiante
        self.asignaturas = []

    def agregar_asignatura(self, asignatura):
        self.asignaturas.append(asignatura)

    def __str__(self):
        return f'Estudiante(nombre={self.nombre}, edad={self.edad}, id={self.id_estudiante}, asignaturas={len(self.asignaturas)})'

class EstudianteRegular(Estudiante):
    def __init__(self, nombre, edad, id_estudiante):
        super().__init__(nombre, edad, id_estudiante)

class EstudianteAvanzado(Estudiante):
    def __init__(nombre, edad, id_estudiante):
        super().__init__(nombre, edad, id_estudiante)

class Profesor(Persona):
    def __init__(self, nombre, edad, id_profesor):
        super().__init__(nombre, edad)
        self.id_profesor = id_profesor

    def __str__(self):
        return f'Profesor(nombre={self.nombre}, edad={self.edad}, id={self.id_profesor})'

class Asignatura:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        self.calificaciones.append(calificacion)

    def __str__(self):
        return f'Asignatura(nombre={self.nombre}, profesor={self.profesor.nombre})'

class Calificacion:
    def __init__(self, estudiante, asignatura, nota):
        self.estudiante = estudiante
        self.asignatura = asignatura
        self.nota = nota

    def __str__(self):
        return f'Calificacion(estudiante={self.estudiante.nombre}, asignatura={self.asignatura.nombre}, nota={self.nota})'

# Ejemplo de uso:
profesor_bonini = Profesor('Bonini', 34, 'P002')
asignatura1 = Asignatura('Matemáticas', profesor_bonini)

estudiante1 = EstudianteRegular('Facundo', 22, 'E001')
estudiante2 = EstudianteAvanzado('María', 23, 'E002')

estudiante1.agregar_asignatura(asignatura1)
estudiante2.agregar_asignatura(asignatura1)

calificacion1 = Calificacion(estudiante1, asignatura1, 90)
calificacion2 = Calificacion(estudiante2, asignatura1, 95)

asignatura1.agregar_calificacion(calificacion1)
asignatura1.agregar_calificacion(calificacion2)

print(profesor_bonini)
print(asignatura1)
print(estudiante1)
print(estudiante2)
print(calificacion1)
print(calificacion2)

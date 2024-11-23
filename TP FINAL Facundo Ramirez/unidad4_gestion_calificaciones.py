class Profesor:
    def __init__(self, nombre, asignatura):
        self.nombre = nombre
        self.asignatura = asignatura

    def __str__(self):
        return f'Profesor(nombre={self.nombre}, asignatura={self.asignatura})'


class Alumno:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.calificaciones = {}

    def agregar_calificacion(self, asignatura, profesor, calificacion):
        self.calificaciones[asignatura] = {'profesor': profesor, 'calificacion': calificacion}

    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        total = sum(info['calificacion'] for info in self.calificaciones.values())
        return total / len(self.calificaciones)

    def determinar_promocion(self):
        promedio = self.calcular_promedio()
        return promedio >= 6  # Asumiendo que 6 es la nota mínima para promoción

    def __str__(self):
        return f'Alumno(nombre={self.nombre}, curso={self.curso})'


class Asignatura:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return f'Asignatura(nombre={self.nombre})'


# Ejemplo de uso:
profesor1 = Profesor('Bonini', 'Informática')
profesor2 = Profesor('García', 'Matemáticas')

alumno1 = Alumno('Facundo', '4to Año')
alumno2 = Alumno('María', '4to Año')

asignatura1 = Asignatura('Informática')
asignatura2 = Asignatura('Matemáticas')

alumno1.agregar_calificacion(asignatura1.nombre, profesor1.nombre, 8)
alumno1.agregar_calificacion(asignatura2.nombre, profesor2.nombre, 7)
alumno2.agregar_calificacion(asignatura1.nombre, profesor1.nombre, 9)
alumno2.agregar_calificacion(asignatura2.nombre, profesor2.nombre, 6)

print(profesor1)
print(profesor2)
print(alumno1)
print(alumno2)
print(asignatura1)
print(asignatura2)

print(f'Promedio de {alumno1.nombre}: {alumno1.calcular_promedio()}')
print(f'{alumno1.nombre} está promocionado: {alumno1.determinar_promocion()}')

print(f'Promedio de {alumno2.nombre}: {alumno2.calcular_promedio()}')
print(f'{alumno2.nombre} está promocionado: {alumno2.determinar_promocion()}')

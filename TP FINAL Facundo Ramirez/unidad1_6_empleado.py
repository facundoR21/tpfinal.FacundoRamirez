class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Salario: {self.salario}, Departamento: {self.departamento}')

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Equipo: {", ".join(self.equipo)}')

    def gestionar(self):
        print(f'{self.nombre} está gestionando el equipo: {", ".join(self.equipo)}.')

class Analista(Empleado):
    def __init__(self, nombre, salario, departamento, proyectos):
        super().__init__(nombre, salario, departamento)
        self.proyectos = proyectos

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f'Proyectos: {", ".join(self.proyectos)}')

    def analizar(self):
        print(f'{self.nombre} está analizando los proyectos: {", ".join(self.proyectos)}.')

# Ejemplo de uso
gerente1 = Gerente('Laura', 60000, 'Administración', ['Pedro', 'María', 'Luis'])
analista1 = Analista('Jorge', 55000, 'Finanzas', ['Proyecto A', 'Proyecto B'])

gerente1.mostrar_informacion()
gerente1.gestionar()

analista1.mostrar_informacion()
analista1.analizar()

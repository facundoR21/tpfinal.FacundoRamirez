from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, salario_base):
        self.nombre = nombre
        self.salario_base = salario_base

    @abstractmethod
    def calcular_sueldo(self):
        pass

    @abstractmethod
    def generar_reporte(self):
        pass

class Desarrollador(Empleado):
    def __init__(self, nombre, salario_base, horas_extra):
        super().__init__(nombre, salario_base)
        self.horas_extra = horas_extra

    def calcular_sueldo(self):
        return self.salario_base + (self.horas_extra * 20)

    def generar_reporte(self):
        return f"Desarrollador: {self.nombre}, Sueldo: {self.calcular_sueldo()}"

class Gerente(Empleado):
    def __init__(self, nombre, salario_base, bono):
        super().__init__(nombre, salario_base)
        self.bono = bono

    def calcular_sueldo(self):
        return self.salario_base + self.bono

    def generar_reporte(self):
        return f"Gerente: {self.nombre}, Sueldo: {self.calcular_sueldo()}"

class Contador(Empleado):
    def __init__(self, nombre, salario_base, clientes):
        super().__init__(nombre, salario_base)
        self.clientes = clientes

    def calcular_sueldo(self):
        return self.salario_base + (self.clientes * 50)

    def generar_reporte(self):
        return f"Contador: {self.nombre}, Sueldo: {self.calcular_sueldo()}"

# Ejemplo de uso
desarrollador = Desarrollador("Alice", 3000, 10)
gerente = Gerente("Bob", 5000, 1000)
contador = Contador("Charlie", 4000, 5)

print(desarrollador.generar_reporte())
print(gerente.generar_reporte())
print(contador.generar_reporte())

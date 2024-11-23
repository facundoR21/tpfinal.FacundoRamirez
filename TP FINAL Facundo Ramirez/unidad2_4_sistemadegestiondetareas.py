class Tarea:
    def __init__(self, id_tarea, titulo, descripcion, estado='pendiente'):
        self.id_tarea = id_tarea
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def actualizar_tarea(self, titulo=None, descripcion=None, estado=None):
        if titulo:
            self.titulo = titulo
        if descripcion:
            self.descripcion = descripcion
        if estado:
            self.estado = estado

    def __str__(self):
        return f'Tarea(id_tarea={self.id_tarea}, titulo={self.titulo}, descripcion={self.descripcion}, estado={self.estado})'


class ListaTareas:
    def __init__(self):
        self.tareas = {}
        self.proximo_id = 1

    def agregar_tarea(self, titulo, descripcion):
        nueva_tarea = Tarea(self.proximo_id, titulo, descripcion)
        self.tareas[self.proximo_id] = nueva_tarea
        self.proximo_id += 1

    def eliminar_tarea(self, id_tarea):
        if id_tarea in self.tareas:
            del self.tareas[id_tarea]

    def actualizar_tarea(self, id_tarea, titulo=None, descripcion=None, estado=None):
        if id_tarea in self.tareas:
            self.tareas[id_tarea].actualizar_tarea(titulo, descripcion, estado)

    def mostrar_tareas(self):
        for id_tarea, tarea in self.tareas.items():
            print(tarea)

# Ejemplo de uso:
lista_tareas = ListaTareas()
lista_tareas.agregar_tarea('Comprar pan', 'Comprar pan en la panadería')
lista_tareas.agregar_tarea('Leer libro', 'Leer el libro de Python')
lista_tareas.mostrar_tareas()

lista_tareas.actualizar_tarea(1, estado='completada')
lista_tareas.eliminar_tarea(2)
lista_tareas.mostrar_tareas()

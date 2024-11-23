class Usuario:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    def cambiar_contraseña(self, nueva_contraseña):
        self.contraseña = nueva_contraseña
        print("Contraseña cambiada con éxito.")

    def mostrar_informacion(self):
        print(f'Nombre: {self.nombre}, Email: {self.email}')

# Ejemplo de uso
usuario1 = Usuario('Facundo', 'facundo@example.com', 'contraseña123')
usuario1.mostrar_informacion()
usuario1.cambiar_contraseña('nueva_contraseña456')

class Cancion:
    def __init__(self, nombre, artista, duracion):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion

    def reproducir(self):
        print(f'Reproduciendo: {self.nombre} por {self.artista}')

    def mostrar_detalles(self):
        print(f'Nombre: {self.nombre}, Artista: {self.artista}, Duración: {self.duracion} minutos')

# Ejemplo de uso
cancion1 = Cancion('Shape of You', 'Ed Sheeran', 4.24)
cancion1.mostrar_detalles()
cancion1.reproducir()

import pygame
import time

class Entretenimiento:
    def reproducir(self):
        pass

class Cancion(Entretenimiento):
    def __init__(self, archivo):
        self.archivo = archivo

    def reproducir(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.archivo)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)

class Pelicula(Entretenimiento):
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

    def reproducir(self):
        print(f"Reproduciendo la película: {self.titulo}, dirigida por {self.director}")

class Libro(Entretenimiento):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def reproducir(self):
        print(f"Leyendo el libro: {self.titulo}, escrito por {self.autor}")

def reproducir(objeto):
    if isinstance(objeto, Entretenimiento):
        objeto.reproducir()
    else:
        print("El objeto no es un medio de entretenimiento válido.")

# Ejemplo de uso
cancion = Cancion("ruta/a/tu/cancion.mp3")
pelicula = Pelicula("Inception", "Christopher Nolan")
libro = Libro("1984", "George Orwell")

reproducir(cancion)
reproducir(pelicula)
reproducir(libro)

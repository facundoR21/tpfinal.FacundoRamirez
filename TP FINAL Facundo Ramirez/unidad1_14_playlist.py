class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def __str__(self):
        return f"{self.titulo} de {self.artista} ({self.duracion} min)"

class Playlist:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)

    def eliminar_cancion(self, titulo):
        self.canciones = [cancion for cancion in self.canciones if cancion.titulo != titulo]

    def mostrar_playlist(self):
        print(f"Playlist: {self.nombre}")
        for cancion in self.canciones:
            print(cancion)

# Ejemplo de uso
cancion1 = Cancion("Bohemian Rhapsody", "Queen", 5.55)
cancion2 = Cancion("Imagine", "John Lennon", 3.03)
cancion3 = Cancion("Hotel California", "Eagles", 6.30)

playlist = Playlist("Mis Favoritas")
playlist.agregar_cancion(cancion1)
playlist.agregar_cancion(cancion2)
playlist.agregar_cancion(cancion3)

playlist.mostrar_playlist()

playlist.eliminar_cancion("Imagine")
print("\nDespués de eliminar una canción:")
playlist.mostrar_playlist()

import numpy as np
import pandas as pd

class Usuario:
    def __init__(self, id_usuario, nombre):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.calificaciones = {}

    def calificar_pelicula(self, pelicula, calificacion):
        self.calificaciones[pelicula.id_pelicula] = calificacion

    def __str__(self):
        return f'Usuario(id={self.id_usuario}, nombre={self.nombre})'

class Pelicula:
    def __init__(self, id_pelicula, titulo, genero):
        self.id_pelicula = id_pelicula
        self.titulo = titulo
        self.genero = genero

    def __str__(self):
        return f'Pelicula(id={self.id_pelicula}, titulo={self.titulo}, genero={self.genero})'

class SistemaRecomendacion:
    def __init__(self):
        self.usuarios = []
        self.peliculas = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def generar_matriz_calificaciones(self):
        datos = {
            usuario.id_usuario: usuario.calificaciones for usuario in self.usuarios
        }
        matriz_calificaciones = pd.DataFrame(datos).fillna(0)
        return matriz_calificaciones

    def recomendar_peliculas(self, usuario, num_recomendaciones=5):
        matriz_calificaciones = self.generar_matriz_calificaciones().T
        if usuario.id_usuario not in matriz_calificaciones.index:
            return []

        calificaciones_usuario = matriz_calificaciones.loc[usuario.id_usuario]
        calificaciones_similares = matriz_calificaciones.corrwith(calificaciones_usuario)
        recomendaciones = calificaciones_similares.sort_values(ascending=False).index
        peliculas_recomendadas = [
            self.obtener_pelicula_por_id(id_pelicula)
            for id_pelicula in recomendaciones
            if id_pelicula not in usuario.calificaciones
        ]
        return peliculas_recomendadas[:num_recomendaciones]

    def obtener_pelicula_por_id(self, id_pelicula):
        for pelicula in self.peliculas:
            if pelicula.id_pelicula == id_pelicula:
                return pelicula
        return None

    def detectar_tendencias(self):
        matriz_calificaciones = self.generar_matriz_calificaciones()
        calificaciones_promedio = matriz_calificaciones.mean(axis=1)
        tendencias = calificaciones_promedio.sort_values(ascending=False).index
        peliculas_tendencias = [self.obtener_pelicula_por_id(id_pelicula) for id_pelicula in tendencias]
        return peliculas_tendencias

    def recomendar_grupos(self, usuarios):
        peliculas_comunes = set()
        for usuario in usuarios:
            peliculas_comunes = peliculas_comunes.union(usuario.calificaciones.keys())
        peliculas_comunes = list(peliculas_comunes)

        recomendaciones = []
        for pelicula_id in peliculas_comunes:
            peliculas_interes = [usuario.calificaciones.get(pelicula_id, 0) for usuario in usuarios]
            promedio_interes = np.mean(peliculas_interes)
            if promedio_interes > 3:  # Umbral de interés
                recomendaciones.append(self.obtener_pelicula_por_id(pelicula_id))

        return recomendaciones

    def retroalimentacion_usuario(self, usuario, pelicula, calificacion):
        usuario.calificar_pelicula(pelicula, calificacion)

# Ejemplo de uso:
sistema = SistemaRecomendacion()

# Crear usuarios
facundo = Usuario(1, 'Facundo')
maria = Usuario(2, 'María')

# Crear películas
pelicula1 = Pelicula(1, 'Matrix', 'Ciencia ficción')
pelicula2 = Pelicula(2, 'El Padrino', 'Drama')
pelicula3 = Pelicula(3, 'Toy Story', 'Animación')

# Agregar usuarios y películas al sistema
sistema.agregar_usuario(facundo)
sistema.agregar_usuario(maria)
sistema.agregar_pelicula(pelicula1)
sistema.agregar_pelicula(pelicula2)
sistema.agregar_pelicula(pelicula3)

# Calificar películas
facundo.calificar_pelicula(pelicula1, 5)
facundo.calificar_pelicula(pelicula2, 4)
maria.calificar_pelicula(pelicula1, 5)
maria.calificar_pelicula(pelicula3, 4)

# Obtener recomendaciones para Facundo
recomendaciones_facundo = sistema.recomendar_peliculas(facundo)
print('Recomendaciones para Facundo:')
for pelicula in recomendaciones_facundo:
    print(pelicula)

# Detectar tendencias
tendencias = sistema.detectar_tendencias()
print('Películas en tendencia:')
for pelicula in tendencias:
    print(pelicula)

# Obtener recomendaciones para un grupo (Facundo y María)
recomendaciones_grupo = sistema.recomendar_grupos([facundo, maria])
print('Recomendaciones para el grupo (Facundo y María):')
for pelicula in recomendaciones_grupo:
    print(pelicula)

# Retroalimentación del usuario
sistema.retroalimentacion_usuario(facundo, pelicula3, 5)
print('Facundo ha calificado Toy Story con 5 estrellas.')

 

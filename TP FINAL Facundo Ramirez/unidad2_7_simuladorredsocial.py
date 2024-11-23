class Usuario:
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.amigos = []
        self.publicaciones = []

    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

    def publicar(self, contenido):
        publicacion = Publicacion(self, contenido)
        self.publicaciones.append(publicacion)
        return publicacion

    def __str__(self):
        return f'Usuario(nombre={self.nombre}, edad={self.edad}, email={self.email}, amigos={len(self.amigos)}, publicaciones={len(self.publicaciones)})'


class Publicacion:
    def __init__(self, usuario, contenido):
        self.usuario = usuario
        self.contenido = contenido
        self.comentarios = []

    def agregar_comentario(self, usuario, contenido):
        comentario = Comentario(usuario, contenido)
        self.comentarios.append(comentario)

    def __str__(self):
        return f'Publicacion(usuario={self.usuario.nombre}, contenido={self.contenido}, comentarios={len(self.comentarios)})'


class Comentario:
    def __init__(self, usuario, contenido):
        self.usuario = usuario
        self.contenido = contenido

    def __str__(self):
        return f'Comentario(usuario={self.usuario.nombre}, contenido={self.contenido})'


class RedSocial:
    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []

    def registrar_usuario(self, nombre, edad, email):
        usuario = Usuario(nombre, edad, email)
        self.usuarios.append(usuario)
        return usuario

    def mostrar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def mostrar_publicaciones(self):
        for usuario in self.usuarios:
            for publicacion in usuario.publicaciones:
                print(publicacion)
                for comentario in publicacion.comentarios:
                    print(f'  {comentario}')

# Ejemplo de uso con datos de Facundo:
red_social = RedSocial('Red Social Ejemplo')

facundo = red_social.registrar_usuario('Facundo', 22, 'facundo@ejemplo.com')
usuario2 = red_social.registrar_usuario('María', 25, 'maria@ejemplo.com')

facundo.agregar_amigo(usuario2)
usuario2.agregar_amigo(facundo)

publicacion1 = facundo.publicar('¡Hola a todos! Soy Facundo.')
usuario2.publicar('¡Buen día a todos!')

publicacion1.agregar_comentario(usuario2, '¡Hola, Facundo! Bienvenido a la red social.')

red_social.mostrar_usuarios()
red_social.mostrar_publicaciones()

import random

class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.eventos_creados = []
        self.eventos_registrados = []

    def crear_evento(self, evento):
        self.eventos_creados.append(evento)

    def registrar_evento(self, evento):
        self.eventos_registrados.append(evento)

    def __str__(self):
        return f'Usuario(id={self.id_usuario}, nombre={self.nombre}, email={self.email})'


class Evento:
    def __init__(self, id_evento, titulo, descripcion, tipo, fecha, creador):
        self.id_evento = id_evento
        self.titulo = titulo
        self.descripcion = descripcion
        self.tipo = tipo
        self.fecha = fecha
        self.creador = creador
        self.registrados = []
        self.pagos = []

    def registrar_usuario(self, usuario):
        self.registrados.append(usuario)
        usuario.registrar_evento(self)

    def agregar_pago(self, pago):
        self.pagos.append(pago)

    def __str__(self):
        return f'Evento(id={self.id_evento}, titulo={self.titulo}, descripcion={self.descripcion}, tipo={self.tipo}, fecha={self.fecha}, creador={self.creador.nombre}, registrados={len(self.registrados)})'


class Pago:
    def __init__(self, id_pago, usuario, evento, cantidad):
        self.id_pago = id_pago
        self.usuario = usuario
        self.evento = evento
        self.cantidad = cantidad

    def __str__(self):
        return f'Pago(id={self.id_pago}, usuario={self.usuario.nombre}, evento={self.evento.titulo}, cantidad={self.cantidad})'


class Recomendacion:
    def __init__(self, usuario, eventos):
        self.usuario = usuario
        self.eventos = eventos

    def recomendar_eventos(self):
        return random.sample(self.eventos, min(len(self.eventos), 3))

    def __str__(self):
        recomendaciones = ', '.join([evento.titulo for evento in self.recomendar_eventos()])
        return f'Recomendaciones para {self.usuario.nombre}: {recomendaciones}'


class Notificacion:
    def __init__(self, usuario, mensaje):
        self.usuario = usuario
        self.mensaje = mensaje

    def enviar_notificacion(self):
        print(f'Notificación para {self.usuario.nombre}: {self.mensaje}')

    def __str__(self):
        return f'Notificacion(usuario={self.usuario.nombre}, mensaje={self.mensaje})'


# Ejemplo de uso:
usuario1 = Usuario(1, 'Facundo', 'facundo@yahoo.com')
usuario2 = Usuario(2, 'María', 'maria@yahoo.com')

evento1 = Evento(1, 'Conferencia de Tecnología', 'Una conferencia sobre tecnología de punta.', 'Conferencia', '2023-07-01', usuario1)
evento2 = Evento(2, 'Concierto de Rock', 'Un concierto con las mejores bandas de rock.', 'Concierto', '2023-08-15', usuario2)
evento3 = Evento(3, 'Reunión de Negocios', 'Una reunión para discutir nuevas oportunidades de negocio.', 'Reunión', '2023-06-10', usuario1)

usuario1.crear_evento(evento1)
usuario2.crear_evento(evento2)
usuario1.crear_evento(evento3)

evento1.registrar_usuario(usuario2)
evento2.registrar_usuario(usuario1)

pago1 = Pago(1, usuario2, evento1, 50)
pago2 = Pago(2, usuario1, evento2, 100)
evento1.agregar_pago(pago1)
evento2.agregar_pago(pago2)

recomendacion1 = Recomendacion(usuario1, [evento1, evento2, evento3])
print(recomendacion1)

notificacion1 = Notificacion(usuario1, 'Tienes una nueva recomendación de eventos.')
notificacion1.enviar_notificacion()

print(usuario1)
print(usuario2)
print(evento1)
print(evento2)
print(evento3)
print(pago1)
print(pago2)

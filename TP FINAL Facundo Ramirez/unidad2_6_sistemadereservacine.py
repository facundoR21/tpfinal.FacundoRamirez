class Pelicula:
    def __init__(self, titulo, duracion, genero):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero

    def __str__(self):
        return f'Pelicula(titulo={self.titulo}, duracion={self.duracion}, genero={self.genero})'


class SalaCine:
    def __init__(self, numero, asientos):
        self.numero = numero
        self.asientos = asientos

    def __str__(self):
        return f'SalaCine(numero={self.numero}, asientos={self.asientos})'


class Asiento:
    def __init__(self, fila, numero, reservado=False):
        self.fila = fila
        self.numero = numero
        self.reservado = reservado

    def reservar(self):
        self.reservado = True

    def liberar(self):
        self.reservado = False

    def __str__(self):
        return f'Asiento(fila={self.fila}, numero={self.numero}, reservado={self.reservado})'


class Horario:
    def __init__(self, pelicula, sala, hora):
        self.pelicula = pelicula
        self.sala = sala
        self.hora = hora

    def __str__(self):
        return f'Horario(pelicula={self.pelicula.titulo}, sala={self.sala.numero}, hora={self.hora})'


class Reserva:
    def __init__(self, horario, asiento):
        self.horario = horario
        self.asiento = asiento

    def __str__(self):
        return f'Reserva(pelicula={self.horario.pelicula.titulo}, sala={self.horario.sala.numero}, hora={self.horario.hora}, asiento={self.asiento})'


class Cine:
    def __init__(self, nombre):
        self.nombre = nombre
        self.peliculas = []
        self.salas = []
        self.horarios = []
        self.reservas = []

    def agregar_pelicula(self, pelicula):
        self.peliculas.append(pelicula)

    def agregar_sala(self, sala):
        self.salas.append(sala)

    def agregar_horario(self, pelicula_titulo, sala_numero, hora):
        pelicula = next((p for p in self.peliculas if p.titulo == pelicula_titulo), None)
        sala = next((s for s in self.salas if s.numero == sala_numero), None)
        if pelicula and sala:
            horario = Horario(pelicula, sala, hora)
            self.horarios.append(horario)
            print(f'Horario agregado: {horario}')
        else:
            print('Pelicula o sala no encontrada')

    def reservar_asiento(self, pelicula_titulo, sala_numero, hora, fila, numero):
        horario = next((h for h in self.horarios if h.pelicula.titulo == pelicula_titulo and h.sala.numero == sala_numero and h.hora == hora), None)
        if horario:
            asiento = next((a for a in horario.sala.asientos if a.fila == fila and a.numero == numero), None)
            if asiento and not asiento.reservado:
                asiento.reservar()
                reserva = Reserva(horario, asiento)
                self.reservas.append(reserva)
                print(f'Reserva realizada: {reserva}')
            else:
                print('Asiento no disponible')
        else:
            print('Horario no encontrado')

    def mostrar_reservas(self):
        for reserva in self.reservas:
            print(reserva)

# Ejemplo de uso:
cine = Cine('Cine Ejemplo')

pelicula1 = Pelicula('Matrix', 120, 'Ciencia ficción')
pelicula2 = Pelicula('El Padrino', 175, 'Drama')
cine.agregar_pelicula(pelicula1)
cine.agregar_pelicula(pelicula2)

asientos_sala1 = [Asiento(fila, numero) for fila in range(1, 6) for numero in range(1, 11)]
sala1 = SalaCine(1, asientos_sala1)
cine.agregar_sala(sala1)

cine.agregar_horario('Matrix', 1, '18:00')
cine.agregar_horario('El Padrino', 1, '21:00')

cine.reservar_asiento('Matrix', 1, '18:00', 3, 5)
cine.mostrar_reservas()

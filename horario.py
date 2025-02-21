class Horario:
    total_horarios = 0  # Contador de instancias

    def __init__(self, curso, dia, hora_inicio, hora_fin):
        self.curso = curso
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        Horario.total_horarios += 1  # Aumenta el contador cada vez que se crea un horario
    def mostrar_horario(self):
        pass
    def modificar_horario(self):
        pass
    def __str__(self):
        pass
    def __repr__(self):
        pass
    @classmethod
    def desde_tupla(cls, tupla):
        pass
    @staticmethod
    def es_horario_valido(self):
        pass
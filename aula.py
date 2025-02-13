class Aula:
    total_aulas = 0  # Contador de instancias

    def __init__(self, numero, capacidad, recursos):
        self.numero = numero
        self.capacidad = capacidad
        self.recursos = recursos
        Aula.total_aulas += 1  # Aumenta el contador cada vez que se crea un aula
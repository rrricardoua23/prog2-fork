class Aula:
    total_aulas = 0  # Contador de instancias

    def __init__(self, numero, capacidad, recursos):
        self.numero = numero
        self.capacidad = capacidad
        self.recursos = recursos
        Aula.total_aulas += 1  # Aumenta el contador cada vez que se crea un aula

    def mostrar_detalles(self):
        pass
    def reservar_aula(self):
        pass
    def __repr__(self):
        pass
    def __str__(self):
        pass
    def desde_tupla(cls,tupla):
        pass
    @classmethod
    def es_adecuada_para_claase(self):
        pass
    @staticmethod
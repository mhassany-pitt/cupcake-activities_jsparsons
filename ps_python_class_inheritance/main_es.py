class Estudiante():
    def __init__(self, nombre):
        self.nombre=nombre
    def obtenerNombre(self):
        return self.nombre
class Puntaje(Estudiante):
    def __init__(self, nombre, puntaje):
        self.puntaje=puntaje
        Estudiante.__init__(self,nombre)
    def obtenerPuntaje(self):
        return self.puntaje

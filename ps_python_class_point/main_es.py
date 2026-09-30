from math import sqrt
class Punto:
    def __init__(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y
    def distancia_desde(self, otro_punto):
        dist_x = self.x - otro_punto.x
        dist_y = self.y - otro_punto.y
        return sqrt(dist_x * dist_x + dist_y * dist_y)

from math import sqrt
class Point:
    def __init__(self, loc_x, loc_y):
        self.x = loc_x
        self.y = loc_y
    def distance_from(self, another_point):
        x_dist = self.x - another_point.x
        y_dist = self.y - another_point.y
        return sqrt(x_dist * x_dist + y_dist * y_dist)

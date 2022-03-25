from math import sqrt

class Vector:
    def __init__(self, x: float|int, y: float|int):
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)
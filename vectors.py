from math import sqrt

class Vector:
    """
    Obejct representing mathematical vector.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        """
        Return magnitude of the vector.
        """
        return sqrt(self.x**2 + self.y**2)
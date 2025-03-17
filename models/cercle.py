import math

from models.forme import Forme

class Cercle(Forme):
    def __init__(self, couleur="rouge", rempli=False, rayon=1.0):
        super().__init__(couleur, rempli)
        self.rayon = rayon


    def aire(self):
        return math.pi * self.rayon**2

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def __add__(self, autre):
        if isinstance(autre, Cercle):
            return self.aire() + autre.aire()
        else:
            raise TypeError("L'opération n'est possible entre deux cercles")


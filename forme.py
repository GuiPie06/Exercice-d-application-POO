from abc import ABC

class Forme(ABC):
    def __init__(self, couleur, rempli):
        self.couleur = couleur
        self.rempli = rempli


from models.forme import Forme


class Rectangle(Forme):

    def __init__(self, longueur, largeur):
        super().__init__(couleur, rempli)
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

    def perimetre(self):
        return (self.longueur + self.largeur) * 2

    def __add__(self, autre):
        if isinstance(autre, Rectangle): #is instance check si autre(rectangle) et Rectangle sont bien des rectangles
            return self.aire() + autre.aire()

        else:
            raise TypeError("L'opération n'est possible que entre 2 rectangles")

    def __mul__(self, nb):
        if isinstance(nb, (int, float)):
            return Rectangle(
                self.couleur,
                self.rempli,
                self.largeur*nb,
                self.longeur*nb)
        else:
            raise TypeError("L'opération n'est possible qu'avec un nombre")


    def afficher_aire(self):
        return f"L'aire de ce rectangle est de" + str(self.aire())
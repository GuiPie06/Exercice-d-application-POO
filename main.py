import math
class GroupeFormes:
    def __init__(self, *formes):
        self.formes = []


    def ajouter_formes(self, formes):
        self.formes.append(formes)

    def aire_totale(self, formes):
        pass

    def __iter__(self):
        return iter(self.formes)



class forme:
    def __init__(self, couleur, rempli):
        self.couleur = couleur
        self.rempli = bool

    def aire(self):
        pass

    def perimetre(self):
        pass


class Cercle(forme):
    def __init__(self, couleur, rempli, rayon):
        super().__init__(couleur, rempli)
        self.rayon = rayon

    def aire(self):
        aire = math.pi * self.rayon**2
        return aire


from models.forme import Forme
class GroupeForme:
    def __init__(self, malisteformes=None):
        if malisteformes is None:
            for forme in malisteformes:
                self.ajouter(forme)
        self.formes = []
    def ajouter(self,forme):
        if not isinstance(forme,Forme):
            raise TypeError("L'objet doit être une instance de la forme")
        self.formes.append(forme)

    def aire_totale(self):
        return sum(formes.aire() for formes in self.formes)

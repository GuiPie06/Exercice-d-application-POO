def creer_rectangle():


    while True:
        try:
            largeur = float(input("Entrez la largeur SVP : "))
            if largeur < 0:
                print("La largeur doit être positive")
                continue
            break

        except ValueError:
            print("Veuillez entrer un nombre valide")



    while True:
        try:
            longueur = float(input("Entrez la longueur SVP : "))
            if longueur < 0:
                print("La longueur doit être positive")
                continue
            break

        except ValueError:
            print("Veuillez entrer un nombre valide")


    return Rectangle(largeur, longueur)

def afficher_aire_forme(forme):
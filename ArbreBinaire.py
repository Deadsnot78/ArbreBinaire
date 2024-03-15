# Définition de la classe ArbreBinaire
class ArbreBinaire:
    # Constructeur de la classe avec la clef et les sous-arbres gauche et droite
    def __init__(self, clef=None, gauche=None, droite=None):
        self.clef = clef  # Valeur du noeud
        self.gauche = gauche  # Sous-arbre gauche
        self.droite = droite  # Sous-arbre droit

    # Méthode pour vérifier si l'arbre est vide (pas de clef, pas de sous-arbres)
    def estVide(self):
        return self.clef is None and self.gauche is None and self.droite is None

    # Méthode pour insérer une nouvelle clef dans l'arbre
    def inserer(self, clef):
        if self.estVide():  # Si l'arbre est vide, on initialise la racine
            self.clef = clef
            self.gauche = ArbreBinaire()  # Création d'un sous-arbre gauche vide
            self.droite = ArbreBinaire()  # Création d'un sous-arbre droit vide
        else:  # Sinon, on insère la clef dans le sous-arbre approprié
            if clef < self.clef:
                self.gauche.inserer(clef)
            elif clef > self.clef:
                self.droite.inserer(clef)

    # Méthode pour calculer la taille de l'arbre (nombre total de noeuds)
    def taille(self):
        if self.estVide():
            return 0  # Un arbre vide a une taille de 0
        else:
            return 1 + self.gauche.taille() + self.droite.taille()  # Taille = 1 (noeud actuel) + taille des sous-arbres

    # Méthode pour rechercher une clef dans l'arbre
    def rechercher(self, clef):
        if self.estVide():
            return False  # Si l'arbre est vide, la clef n'est pas trouvée
        if self.clef == clef:
            return True  # Si la clef du noeud actuel est celle recherchée, on retourne vrai
        elif clef < self.clef:
            return self.gauche.rechercher(clef)  # Recherche dans le sous-arbre gauche
        else:
            return self.droite.rechercher(clef)  # Recherche dans le sous-arbre droit

# Classe principale pour tester les fonctionnalités de l'ArbreBinaire
class Main:
    def __init__(self):
        self.arbre = ArbreBinaire()  # Création d'un arbre binaire vide

    # Méthode pour construire l'arbre en insérant des valeurs
    def construire_arbre(self, valeurs):
        for valeur in valeurs:
            self.arbre.inserer(valeur)

    # Méthode pour afficher la taille de l'arbre
    def afficher_taille(self):
        print(f"Taille de l'arbre: {self.arbre.taille()}")

    # Méthode pour rechercher une valeur dans l'arbre et afficher le résultat
    def rechercher_valeur(self, valeur):
        result = self.arbre.rechercher(valeur)
        if result:
            print(f"La valeur {valeur} a été trouvée dans l'arbre.")
        else:
            print(f"La valeur {valeur} n'a pas été trouvée dans l'arbre.")

# Code principal pour créer une instance de Main, construire l'arbre, et tester les fonctionnalités
if __name__ == "__main__":
    valeurs = [7, 3, 9, 2, 5, 8, 10]  # Liste de valeurs à insérer dans l'arbre
    main = Main()
    main.construire_arbre(valeurs)
    main.afficher_taille()
    main.rechercher_valeur(5)
    main.rechercher_valeur(4)

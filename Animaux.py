class Animal:
    def __init__(self, nom, habitat):
        self.nom = nom
        self.habitat = habitat

    def se_deplacer(self):
        pass

    def manger(self):
        pass


class Herbivore(Animal):
    def manger(self):
        print(f"{self.nom} mange de l'herbe.")


class Carnivore(Animal):
    def manger(self):
        print(f"{self.nom} mange de la viande.")


# Création des instances
lapin = Herbivore(nom="Lapin Blanc", habitat="Prairie")
mouton = Herbivore(nom="Mouton Noir", habitat="Ferme")
lion = Carnivore(nom="Lion Majestueux", habitat="Savane")

# Utilisation des instances
lapin.manger()  # Lapin Blanc mange de l'herbe.
mouton.manger()  # Mouton Noir mange de l'herbe.
lion.manger()    # Lion Majestueux mange de la viande.

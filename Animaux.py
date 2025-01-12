class Animal:
    def __init__(self, tete, corps, membres, habitat=None):

        # Composition
        if not isinstance(tete, Tete):
            raise ValueError("tete doit être une instance de la classe Tete")
        self.tete = tete

        # Composition
        if not isinstance(corps, Corps):
            raise ValueError("corps doit être une instance de la classe Corps")
        self.corps = corps

        # Composition
        if not isinstance(membres, list) or not all(isinstance(membre, Membres) for membre in membres):
            raise ValueError("membres doit être une liste d'instances de la classe Membres")
        self.membres = membres

        # Association
        if habitat is not None and not isinstance(habitat, Habitat):
            raise ValueError("habitat doit être une instance de la classe Habitat ou None")
        self.habitat = habitat

    def __str__(self):
        membres_str = ", ".join(str(membre) for membre in self.membres)
        return (f"{self.__class__.__name__} (Habitat: {self.habitat}, "
                f"Tête: {self.tete}, Corps: {self.corps}, Membres: [{membres_str}])")


class Herbivore(Animal):
    def __init__(self, tete, corps, membres, habitat=None, alimentation="herbivore"):
        super().__init__(tete, corps, membres, habitat)
        self.alimentation = alimentation

    def __str__(self):
        return f"{super().__str__()} - Alimentation: {self.alimentation}"


class Carnivore(Animal):
    def __init__(self, tete, corps, membres, habitat=None, alimentation="carnivore"):
        super().__init__(tete, corps, membres, habitat)
        self.alimentation = alimentation

    def __str__(self):
        return f"{super().__str__()} - Alimentation: {self.alimentation}"

class Tete:
    def __init__(self, forme, taille):
        self.forme = forme
        self.taille = taille

    def __str__(self):
        return f"Tête (Forme: {self.forme}, Taille: {self.taille})"


class Corps:
    def __init__(self, type, couleur):
        self.type = type
        self.couleur = couleur

    def __str__(self):
        return f"Corps (Type: {self.type}, Couleur: {self.couleur})"


class Membres:
    def __init__(self, nombre, fonction):
        self.nombre = nombre
        self.fonction = fonction

    def __str__(self):
        return f"Membres (Nombre: {self.nombre}, Fonction: {self.fonction})"


class Habitat:
    def __init__(self, type, localisation):
        self.type = type
        self.localisation = localisation

    def __str__(self):
        return f"Habitat (Type: {self.type}, Localisation: {self.localisation})"

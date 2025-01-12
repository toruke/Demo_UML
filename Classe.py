from typing import List

class Personne:
    """
    Représente une personne générique avec des informations personnelles.
    """
    def __init__(self, nom: str, prenom: str, adresse: str, telephone: str):
        """
        Initialise une personne avec ses informations personnelles.
        :param nom: Nom de la personne.
        :param prenom: Prénom de la personne.
        :param adresse: Adresse de la personne.
        :param telephone: Numéro de téléphone de la personne.
        """
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse
        self.telephone = telephone

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.telephone})"


class Professeur(Personne):
    """
    Représente un professeur, qui hérite de la classe Personne.
    """
    def __init__(self, nom: str, prenom: str, adresse: str, telephone: str, specialite: str):
        """
        Initialise un professeur avec ses informations et sa spécialité.
        :param specialite: Spécialité enseignée par le professeur.
        """
        super().__init__(nom, prenom, adresse, telephone)
        self.specialite = specialite

    def __str__(self):
        return f"Professeur {super().__str__()}, spécialité: {self.specialite}"


class Eleve(Personne):
    """
    Représente un élève, qui hérite de la classe Personne.
    """
    def __init__(self, nom: str, prenom: str, adresse: str, telephone: str, numero_matricule: int):
        """
        Initialise un élève avec ses informations et son numéro matricule.
        :param numero_matricule: Numéro d'inscription de l'élève.
        """
        super().__init__(nom, prenom, adresse, telephone)
        self.numero_matricule = numero_matricule

    def __str__(self):
        return f"Élève {super().__str__()}, matricule: {self.numero_matricule}"


class Classe:
    """
    Représente une classe scolaire avec un professeur et des élèves.
    """
    def __init__(self, nom: str, professeur: Professeur):
        """
        Initialise une classe scolaire.
        :param nom: Nom ou niveau de la classe (ex. "5ème A").
        :param professeur: Professeur responsable de la classe.
        """
        self.nom = nom
        self.professeur = professeur
        self.eleves: List[Eleve] = []

    def ajouter_eleve(self, eleve: Eleve):
        """
        Ajoute un élève à la classe, s'il y a moins de 30 élèves.
        :param eleve: L'élève à ajouter.
        """
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
        else:
            raise ValueError("Impossible d'ajouter un élève, la classe est pleine (30 max).")

    def __str__(self):
        eleves_str = "\n".join([str(eleve) for eleve in self.eleves]) if self.eleves else "Aucun élève"
        return (f"Classe: {self.nom}\n"
                f"Professeur: {self.professeur}\n"
                f"Élèves:\n{eleves_str}")

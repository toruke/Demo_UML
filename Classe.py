from typing import List

class Dossier:
    def __init__(self, nom: str, prenom: str, date_naissance: str, adresse: str, telephone: str, email: str):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return (f"{self.prenom} {self.nom}, Né(e) le {self.date_naissance}\n"
                f"Adresse: {self.adresse}, Téléphone: {self.telephone}, Email: {self.email}")


class Personne:
    def __init__(self, dossier: Dossier):
        self.dossier = dossier  # Association : la Personne a un Dossier, mais n'en est pas responsable.

    def __str__(self):
        return str(self.dossier)


class Professeur(Personne):
    def __init__(self, dossier: Dossier, matiere: str):
        super().__init__(dossier)  # Héritage de Personne
        self.matiere = matiere

    def __str__(self):
        return f"Professeur de {self.matiere} : {super().__str__()}"


class Eleve(Personne):
    def __init__(self, dossier: Dossier, niveau: str):
        super().__init__(dossier)  # Héritage de Personne
        self.niveau = niveau

    def __str__(self):
        return f"Élève (Niveau: {self.niveau}) : {super().__str__()}"


class Classe:
    def __init__(self, professeur: Professeur, nom_classe: str):
        self.professeur = professeur  # Agrégation
        self.nom_classe = nom_classe
        self.eleves: List[Eleve] = []  # Agrégation

    def ajouter_eleve(self, eleve: Eleve):
        """Ajoute un élève à la classe si elle n'est pas pleine."""
        if len(self.eleves) < 30:
            self.eleves.append(eleve)
        else:
            print("La classe est déjà pleine, impossible d'ajouter cet élève.")

    def afficher_classe(self):
        """Affiche les informations de la classe, du professeur, et des élèves."""
        print(f"Classe : {self.nom_classe}")
        print(f"Professeur : {self.professeur}")
        print("Élèves :")
        for eleve in self.eleves:
            print(eleve)
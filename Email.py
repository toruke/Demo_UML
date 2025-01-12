from typing import List


class AdresseEmail:
    def __init__(self, adresse: str):
        self.adresse = adresse
        if not self.est_valide():
            raise ValueError(f"Adresse email invalide : {adresse}")

    def est_valide(self) -> bool:
        # Validation simple du format de l'adresse email
        return re.match(r"[^@]+@[^@]+\.[^@]+", self.adresse) is not None


class TexteEmail:
    def __init__(self, titre: str, corps: str):
        # Maintenant, titre et corps sont obligatoires
        self.titre = titre
        self.corps = corps


class FichierJoint:
    def __init__(self, nom: str, contenu: bytes):
        self.nom = nom
        self.contenu = contenu

    def __str__(self):
        return f"Fichier Joint: {self.nom}"


class Email:
    def __init__(
            self,
            expediteur: str,
            destinataire: str,
            titre: str,
            corps: str,
            fichiers: List[FichierJoint] = None  # Fichiers joints sont optionnels
    ):
        # Composition
        self.expediteur = AdresseEmail(expediteur)
        self.destinataire = AdresseEmail(destinataire)

        # Composition
        self.texte = TexteEmail(titre, corps)

        # Composition (Les fichiers sont optionnels)
        self.fichiers = fichiers if fichiers is not None else []

    def envoyer(self):
        print(f"Envoi de l'email de {self.expediteur.adresse} à {self.destinataire.adresse}")
        print(f"Titre: {self.texte.titre}")
        print(f"Corps: {self.texte.corps}")
        if self.fichiers:
            print(f"Fichiers joints: {[f.nom for f in self.fichiers]}")
from typing import List, Optional

class FichierJoint:
    """
    Représente un fichier joint à un email.
    """
    def __init__(self, nom: str, type: str, taille: int):
        """
        Initialise un fichier joint avec un nom, un type et une taille.
        :param nom: Nom du fichier (ex. "document.pdf").
        :param type: Type MIME du fichier (ex. "application/pdf").
        :param taille: Taille du fichier en Ko.
        """
        self.nom = nom
        self.type = type
        self.taille = taille

    def __str__(self):
        return f"FichierJoint(nom={self.nom}, type={self.type}, taille={self.taille} Ko)"


class Email:
    """
    Représente un email avec un titre, un texte, un expéditeur, un destinataire,
    et éventuellement des fichiers joints.
    """
    def __init__(self, expediteur: str, destinataire: str,
                 titre: Optional[str] = None, texte: Optional[str] = None,
                 fichiers_joints: Optional[List[FichierJoint]] = None):
        """
        Initialise un email.
        :param expediteur: Adresse email de l'expéditeur.
        :param destinataire: Adresse email du destinataire.
        :param titre: Titre de l'email (facultatif).
        :param texte: Texte de l'email (facultatif).
        :param fichiers_joints: Liste des fichiers joints (facultatif).
        """
        self.titre = titre
        self.texte = texte
        self.expediteur = expediteur
        self.destinataire = destinataire
        self.fichiers_joints = fichiers_joints if fichiers_joints else []

    def ajouter_fichier_joint(self, fichier: FichierJoint):
        """
        Ajoute un fichier joint à l'email.
        :param fichier: Un objet de type FichierJoint.
        """
        self.fichiers_joints.append(fichier)

    def __str__(self):
        fichiers = "\n".join([str(f) for f in self.fichiers_joints]) if self.fichiers_joints else "Aucun fichier joint"
        return (f"Email(titre={self.titre}, texte={self.texte}, "
                f"expediteur={self.expediteur}, destinataire={self.destinataire}, "
                f"fichiers_joints=\n{fichiers})")

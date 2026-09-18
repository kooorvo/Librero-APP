import json

class Livre():
    def __init__(self, titre, auteur, categorie, isbn, disponible=True, nb_emprunts=0, note=None):
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.disponible = disponible
        self.isbn = isbn
        self.nb_emprunts = nb_emprunts
        self.note = note if note is not None else []
    
    def emprunter(self):
        if self.disponible==False:
            return (f"Le livre {self.titre} est déjà emprunté.")
        else : 
            self.disponible=False
            self.nb_emprunts+=1
            return (f"Vous avez emprunté le livre {self.titre}.")
            
    def rendre(self):
        if self.disponible==True:
            return (f"Le livre {self.titre} a déjà été rendu.")
        else : 
            self.disponible=True
            return (f"Vous avez rendu le livre {self.titre}.")
    
    def afficher_stats(self):
        return (f"Le livre {self.titre} à été emprunté {self.nb_emprunts} de fois")

    def ajouter_note(self, eval):
        self.note.append(eval)

    def calculer_moyenne(self):
        if not self.note:
            return None
        return sum(self.note) / len(self.note)

    def afficher_infos(self):
            disponible = "Oui" if self.disponible else "Non"
            moyenne = self.calculer_moyenne()
            if moyenne is None:
                txt_note = "Aucune évaluation"
            else:
                txt_note = f"{moyenne:.1f}/5"
            return (f"Titre : {self.titre}\n"
                    f"Auteur : {self.auteur}\n"
                    f"Catégorie : {self.categorie}\n"
                    f"Disponible : {disponible}\n"
                    f"ISBN : {self.isbn}\n"
                    f"Note : {txt_note}")




    # prép pour l'export json
    def to_dic(self):
        return{
            "titre":self.titre,
            "auteur": self.auteur,
            "categorie" : self.categorie,
            "disponible" : self.disponible,
            "isbn" : self.isbn,
            "emprunts" : self.nb_emprunts,
            "notes" : self.note
        }

    @classmethod #s'applique à la classe
    # inverse de to_dic
    # on utilise @classmethod pour reconstruire le livre plus facilement
    def from_dic(cls, data):
        return cls(
            titre=data["titre"],
            auteur=data["auteur"],
            categorie=data["categorie"],
            disponible=data["disponible"],
            isbn=data["isbn"],
            nb_emprunts=data["emprunts"],
            note=data["notes"]
        )
import json

class Users():
    def __init__(self, nom, prenom, id, dernierEmprunt):
        self.nom = nom 
        self.prenom = prenom
        self.id = int(id)
        self.dernierEmprunt = dernierEmprunt if len(dernierEmprunt)>0 else "Aucun"

    def to_dic(self):
        return{
            "nom":self.nom,
            "prenom": self.prenom,
            "id": self.id,
            "dernier emprunt" : self.dernierEmprunt
        }

    @classmethod #s'applique à la classe
    # inverse de to_dic
    # on utilise @classmethod pour reconstruire le livre plus facilement
    def from_dic(cls, users):
        return cls(
            nom=users["nom"],
            prenom=users["prenom"],
            id=users["id"],
            dernierEmprunt=users["dernier emprunt"]
        )
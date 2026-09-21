import json

class Users():
    def __init__(self, nom, prenom, emprunts=None):
        self.nom = nom 
        self.prenom = prenom
        self.emprunts = emprunts if emprunts is not None else []

    def to_dic(self):
        return{
            "nom":self.nom,
            "prenom": self.prenom,
            "emprunts" : self.emprunts
        }

    @classmethod #s'applique à la classe
    # inverse de to_dic
    # on utilise @classmethod pour reconstruire le livre plus facilement
    def from_dic(cls, users):
        return cls(
            nom=users["nom"],
            prenom=users["prenom"],
            emprunts=users["emprunts"]
        )
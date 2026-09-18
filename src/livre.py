class Livre():
    def __init__(self, titre, auteur, categorie, isbn, disponible=True, nb_emprunts=0):
        self.titre = titre
        self.auteur = auteur
        self.categorie = categorie
        self.disponible = disponible
        self.isbn = isbn
        self.nb_emprunts = nb_emprunts
        
    def afficher_infos(self):
        disponible = "Oui" if self.disponible else "Non"
        return (f"Titre : {self.titre}\nAuteur : {self.auteur}\nCatégorie : {self.categorie}\nDisponible : {disponible}\nISBN : {self.isbn}")
    
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
    
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "conte", "9783140464079")
livre2 = Livre("1984", "George Orwell", "fiction", "978-2070368228")

print(livre1.emprunter())
print(livre1.afficher_stats())
print(livre1.rendre())
print(livre1.afficher_stats())
print(livre1.emprunter())
print(livre1.afficher_stats())



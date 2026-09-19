import json
import customtkinter as ctk
from livre import Livre

#livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "conte", "9783140464079")
#livre2 = Livre("1984", "George Orwell", "fiction", "978-2070368228")
#
## on met les livres dans une liste pour les exporter
#livres = [livre1, livre2]
#
#donnees = []
#for livre in livres:
#    # on transforme le livre en dico avec la fct to_dic
#    dic_livre = livre.to_dic()
#    # on l'ajoute au dico
#    donnees.append(dic_livre)
#
## on ouvre le json, with sert à fermer automatiquement le fichier
#with open("src/data.json", "w", encoding="utf-8") as fichier:
#    # prend une variable et l'écris dans un fichier (ici fichier) json
#    json.dump(donnees, fichier, indent=4) # indent=4 pour les retours à la ligne et les indentations
#
# opé inverse
with open("src/data.json", "r", encoding="utf-8") as fichier:
    # on met les données chargées depuis le json dans une nvlle variable
    donnees_chargees = json.load(fichier)

livres_charges = []
for dic in donnees_chargees:
    # on reconstruit le livre
    un_livre=Livre.from_dic(dic)
    # on l'add à la liste
    livres_charges.append(un_livre)

def sauvegarder():
  donnees_maj = []
  for un_livre in livres_charges:
    nvdic = un_livre.to_dic()
    donnees_maj.append(nvdic)
  with open("src/data.json", "w", encoding="utf-8") as fichier:
    json.dump(donnees_maj, fichier, indent=4) 

# ---GUI---

# génée=ré par ia(gemini)

# Configuration du thème
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Configuration de la fenêtre ---
        self.title("Librero")
        self.geometry("900x600")

        # Disposition en grille : colonne 0 (sidebar) fixe, colonne 1 (main) extensible
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar (Panneau latéral) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        # Titre dans la sidebar
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Librero", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Boutons du menu
        self.btn_chercher = ctk.CTkButton(self.sidebar_frame, text="Rechercher", command=self.afficher_recherche)
        self.btn_chercher.grid(row=1, column=0, padx=20, pady=10)

        self.btn_ajouter = ctk.CTkButton(self.sidebar_frame, text="Ajouter un livre", command=self.afficher_ajout)
        self.btn_ajouter.grid(row=2, column=0, padx=20, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.sidebar_frame, text="Supprimer", command=self.afficher_suppression)
        self.btn_supprimer.grid(row=3, column=0, padx=20, pady=10)

        # --- Zone Principale (Main View) ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Affichage par défaut au lancement
        self.afficher_recherche()

    # --- Fonctions pour vider la zone principale ---
    def nettoyer_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # --- Vues / Écrans d'action ---
    def afficher_recherche(self):
        self.nettoyer_main_frame()

        titre = ctk.CTkLabel(self.main_frame, text="Rechercher un livre", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)

        self.entry_recherche = ctk.CTkEntry(self.main_frame, placeholder_text="Titre ou ISBN...", width=300)
        self.entry_recherche.pack(pady=10)

        btn_valider = ctk.CTkButton(self.main_frame, text="Valider", command=self.search_button)
        btn_valider.pack(pady=10)

        self.label_resultat = ctk.CTkLabel(self.main_frame, text="")
        self.label_resultat.pack(pady=20)

    def afficher_ajout(self):
        self.nettoyer_main_frame()
        titre = ctk.CTkLabel(self.main_frame, text="Ajouter un nouveau livre", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)
        # Tu placeras tes CTkEntry pour Titre, Auteur, ISBN ici

    def afficher_suppression(self):
        self.nettoyer_main_frame()
        titre = ctk.CTkLabel(self.main_frame, text="Supprimer un livre", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)

    # --- Logique métier (actions) ---
    def search_button(self):
        recherche = self.entry_recherche.get()
        print(f"Recherche lancée pour : {recherche}")
        # Ici tu feras ta boucle sur livres_charges pour afficher le résultat dans self.label_resultat

if __name__ == "__main__":
    app = App()
    app.mainloop()
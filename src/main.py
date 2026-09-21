import json
import customtkinter as ctk
import pyperclip as pc

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
with open("src/BDD/data.json", "r", encoding="utf-8") as fichier:
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

# généré par ia(gemini)

# Configuration du thème
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# Fenêtre secondaires

class ToplevelWindowEmprunt(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("450x300")

        titre = ctk.CTkLabel(self, text="Emprunter un livre", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)

        self.titreISBN = ctk.CTkEntry(self, placeholder_text="Titre ou ISBN :", width=300, height=50)
        self.titreISBN.pack(pady=10)

        confirmBtn = ctk.CTkButton(self, text="Confirmer", width=300, height=50, command=self.emprunterLivre)
        confirmBtn.pack(pady=10)

        self.resultatText = ctk.CTkLabel(self, text="")
        self.resultatText.pack(pady=10)

    def emprunterLivre(self):
        existe = False
        titreISBNinput = self.titreISBN.get().strip()

        for un_livre in livres_charges:
            if un_livre.isbn == titreISBNinput or un_livre.titre.lower() == titreISBNinput.lower():
                existe = True
                if un_livre.disponible:
                    un_livre.disponible = False
                    sauvegarder()
                    self.resultatText.configure(text=f"Le livre '{un_livre.titre}' a été emprunté.")
                else:
                    self.resultatText.configure(text=f"Le livre '{un_livre.titre}' est indisponible.")
                break

        if not existe:
            self.resultatText.configure(text=f"Le livre '{titreISBNinput}' n'existe pas.")


class ToplevelWindowRendu(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("450x300")

        titre = ctk.CTkLabel(self, text="Rendre un livre", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)

        self.titreISBN = ctk.CTkEntry(self, placeholder_text="Titre ou ISBN :", width=300, height=50)
        self.titreISBN.pack(pady=10)

        confirmBtn = ctk.CTkButton(self, text="Confirmer", width=300, height=50, command=self.rendreLivre)
        confirmBtn.pack(pady=10)

        self.resultatText = ctk.CTkLabel(self, text="")
        self.resultatText.pack(pady=10)

    def rendreLivre(self):
        existe = False
        titreISBNinput = self.titreISBN.get().strip()

        for un_livre in livres_charges:
            if un_livre.isbn == titreISBNinput or un_livre.titre.lower() == titreISBNinput.lower():
                existe = True
                if not un_livre.disponible:
                    un_livre.disponible = True
                    sauvegarder()
                    self.resultatText.configure(text=f"Le livre '{un_livre.titre}' a été rendu.")
                else:
                    self.resultatText.configure(text=f"Le livre '{un_livre.titre}' est déjà disponible.")
                break

        if not existe:
            self.resultatText.configure(text=f"Le livre '{titreISBNinput}' n'existe pas.")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.toplevel_window = None

        self.title("Librero")
        self.geometry("900x600")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar ---
        self.sidebar_frame = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Librero", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_chercher = ctk.CTkButton(self.sidebar_frame, text="Rechercher", command=self.afficher_recherche)
        self.btn_chercher.grid(row=1, column=0, padx=20, pady=10)

        self.btn_emprunts = ctk.CTkButton(self.sidebar_frame, text="Emprunts", command=self.afficher_emprunts)
        self.btn_emprunts.grid(row=2, column=0, padx=20, pady=10)

        self.btn_ajouter = ctk.CTkButton(self.sidebar_frame, text="Ajouter un livre", command=self.afficher_ajout)
        self.btn_ajouter.grid(row=3, column=0, padx=20, pady=10)        

        self.btn_supprimer = ctk.CTkButton(self.sidebar_frame, text="Supprimer", command=self.afficher_suppression)
        self.btn_supprimer.grid(row=4, column=0, padx=20, pady=10)

        self.switchTheme = ctk.CTkSwitch(self.sidebar_frame, text="Mode clair", command=self.switchTheme, onvalue=1, offvalue=0)
        self.switchTheme.grid(row=6, column=0, padx=20, pady=10)

        # --- Zone Principale ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        self.afficher_recherche()

    def nettoyer_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def afficher_recherche(self):
        self.nettoyer_main_frame()

        titre = ctk.CTkLabel(self.main_frame, text="Rechercher un livre", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)

        self.entry_recherche = ctk.CTkEntry(self.main_frame, placeholder_text="Titre ou ISBN :", width=300, height=50)
        self.entry_recherche.pack(pady=10)

        btn_valider = ctk.CTkButton(self.main_frame, text="Valider", command=self.search_button, width=300, height=50)
        btn_valider.pack(pady=10)

        self.label_resultat = ctk.CTkLabel(self.main_frame, text="")
        self.label_resultat.pack(pady=20)

        # Bouton créé avec texte, prêt à être affiché par search_button()
        self.btn_note = ctk.CTkButton(self.main_frame, text="Ajouter une note", command=self.ajouter_note_btn, width=300, height=50, fg_color="purple", hover_color="#910A64")
        self.btn_copier_isbn = ctk.CTkButton(self.main_frame, text="copier l'ISBN", command=self.copier_isbn, width=300, height=50, fg_color="grey", hover_color="#999499")

    def afficher_emprunts(self):
        self.nettoyer_main_frame()

        titre = ctk.CTkLabel(self.main_frame, text="Gestion des emprunts", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)

        btn_ajouterEmprunt = ctk.CTkButton(self.main_frame, text="Emprunter un livre", command=self.ajouter_emprunt, width=300, height=50)
        btn_ajouterEmprunt.pack(pady=10)

        btn_ajouterRendu = ctk.CTkButton(self.main_frame, text="Rendre un livre", command=self.ajouter_rendu, width=300, height=50)
        btn_ajouterRendu.pack(pady=10)

    def ajouter_emprunt(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowEmprunt(self)
        else:
            self.toplevel_window.focus()

    def ajouter_rendu(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindowRendu(self)
        else:
            self.toplevel_window.focus()

    def afficher_ajout(self):
        self.nettoyer_main_frame()
        titre = ctk.CTkLabel(self.main_frame, text="Ajouter un nouveau livre", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)
        
        self.titre_input = ctk.CTkEntry(self.main_frame, placeholder_text="Titre du livre :", width=300, height=50)
        self.titre_input.pack(pady=10)
        self.auteur_input = ctk.CTkEntry(self.main_frame, placeholder_text="Nom de l'auteur :", width=300, height=50)
        self.auteur_input.pack(pady=10)
        self.cate_input = ctk.CTkEntry(self.main_frame, placeholder_text="Genre du livre :", width=300, height=50)
        self.cate_input.pack(pady=10)
        self.isbn_input = ctk.CTkEntry(self.main_frame, placeholder_text="ISBN du livre :", width=300, height=50)
        self.isbn_input.pack(pady=10)

        btn_valider = ctk.CTkButton(self.main_frame, text="Ajouter", command=self.ajouter_btn, width=300, height=50)
        btn_valider.pack(pady=10)

        self.ajout_resultat = ctk.CTkLabel(self.main_frame, text="")
        self.ajout_resultat.pack(pady=20)

    def afficher_suppression(self):
        self.nettoyer_main_frame()
        titre = ctk.CTkLabel(self.main_frame, text="Supprimer un livre", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)

        self.isbnTitre_input = ctk.CTkEntry(self.main_frame, placeholder_text="Titre ou ISBN :", width=300, height=50)
        self.isbnTitre_input.pack(pady=10)

        btn_valider = ctk.CTkButton(self.main_frame, text="Supprimer", command=self.supprimer_btn, width=300, height=50)
        btn_valider.pack(pady=10)

        self.supp_resultat = ctk.CTkLabel(self.main_frame, text="")
        self.supp_resultat.pack(pady=20)

    # --- Logique ---
    def search_button(self):
        recherche = self.entry_recherche.get().strip()
        trouve = False

        for un_livre in livres_charges:
            if un_livre.titre.lower() == recherche.lower() or un_livre.isbn == recherche:
                trouve = True
                self.label_resultat.configure(text=un_livre.afficher_infos())
                self.btn_note.pack(pady=10)
                self.btn_copier_isbn.pack(pady=10)
                break

        if not trouve:
            self.btn_note.pack_forget()
            self.btn_copier_isbn.pack_forget()
            if len(recherche) > 0:
                self.label_resultat.configure(text=f"Le livre '{recherche}' n'existe pas.")
            else:
                self.label_resultat.configure(text="")

    def ajouter_note_btn(self):
        recherche = self.entry_recherche.get().strip()
        confirm = ctk.CTkInputDialog(text=f"Note pour '{recherche}' (entre 0 et 5) :", title="Attribuer une note")
        saisie = confirm.get_input()

        if not saisie:
            return

        try:
            valeur_note = float(saisie.replace(",", "."))
        except ValueError:
            self.label_resultat.configure(text="Saisie invalide, veuillez entrer un nombre.")
            return

        if not (0 <= valeur_note <= 5):
            self.label_resultat.configure(text="La note doit être comprise entre 0 et 5.")
            return

        for un_livre in livres_charges:
            if un_livre.titre.lower() == recherche.lower() or un_livre.isbn == recherche:
                if not hasattr(un_livre, "note") or not isinstance(un_livre.note, list):
                    un_livre.note = []
                
                un_livre.note.append(valeur_note)
                sauvegarder()
                self.label_resultat.configure(text=f"Note de {valeur_note}/5 ajoutée à '{un_livre.titre}' !")
                break

    def copier_isbn(self):
      recherche = self.entry_recherche.get()
      for un_livre in livres_charges:
        if un_livre.titre.lower() == recherche.lower() or un_livre.isbn == recherche:
          pc.copy(un_livre.isbn)
          self.btn_copier_isbn.configure(text="ISBN copié !")

    def ajouter_emprunt(self):
      # On appelle la petite fenêtre créée avant la class App
      if self.toplevel_window is None or not self.toplevel_window.winfo_exists(): #si la fenêtre existe pas ou qu'elle es fermée on l'ouvre
        self.toplevel_window = ToplevelWindowEmprunt()
      else:
        self.toplevel_window.focus() #sinon on focus dessus

    def ajouter_rendu(self):
      if self.toplevel_window is None or not self.toplevel_window.winfo_exists(): #si la fenêtre existe pas ou qu'elle es fermée on l'ouvre
        self.toplevel_window = ToplevelWindowRendu()
      else:
        self.toplevel_window.focus()

    def ajouter_btn(self):
      infoTitre = self.titre_input.get()
      infoAuteur = self.auteur_input.get()
      infoCate = self.cate_input.get()
      infoIsbn = self.isbn_input.get()
      print(f"Ajout du livre {infoTitre}, de {infoAuteur}, {infoCate}, {infoIsbn}")
      existe = False

      # on vérifie que l'isbn n'est pas déjà dans data.json
      for un_livre in livres_charges:
        if un_livre.isbn == infoIsbn:
          existe = True
          self.ajout_resultat.configure(text=f"Un livre dont l'ISBN est {infoIsbn} existe déjà.")
          break

      #Sinon on le supprime (bien mettre hors de la boucle for)
      if not existe :
        existe = False
        livreAjoute = Livre(infoTitre, infoAuteur, infoCate, infoIsbn)
        livres_charges.append(livreAjoute)
        sauvegarder()
        self.ajout_resultat.configure(text=f"Ce livre à bien été ajouté\n({infoTitre} de {infoAuteur} (Genre : {infoCate}, ISBN : {infoIsbn}))")

    def supprimer_btn(self):
      isbnTitre = self.isbnTitre_input.get()
      print(f"Suppression du livre {isbnTitre}")
      existe = False

      for un_livre in livres_charges:
        if un_livre.isbn == isbnTitre or un_livre.titre == isbnTitre:
          existe = True
          confirm = ctk.CTkInputDialog(text=f"Confirmer la suppression (Oui/Non)")
          confirm_input = confirm.get_input().lower()
          if confirm_input == "oui":
            livres_charges.remove(un_livre)
            sauvegarder()

      if not existe:
        self.ajout_resultat.configure(text=f"Le livre {isbnTitre} n'existe pas.")

    def switchTheme(self):
      val = self.switchTheme.get()
      if val:
        ctk.set_appearance_mode("light")
      else : 
        ctk.set_appearance_mode("dark")

if __name__ == "__main__":
    app = App()
    app.mainloop()
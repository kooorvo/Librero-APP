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

app = ctk.CTk()
app.geometry("400x150")

app.mainloop()
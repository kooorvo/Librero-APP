import json
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


# ---UI---
#for i in livres_charges:
#    # on appelle afficher_infos pour le livre i
#    print(i.afficher_infos())
#    # on crée un séparateur
#    print("-"*20)

print(f"1. Afficher les informations d'un livre\n"
      f"2. Emprunter un livre\n"
      f"3. Rendre un livre\n"
      f"4. Noter un livre")

rep = input("Que souhaitez-vous faire ? (mettre le numéro de l'option) ")

match rep:
    case "1":
        livre = input("Quel livre cherchez-vous ? ")
        livre = livre.lower()
        trouve = False
        
        for un_livre in livres_charges:
            if un_livre.titre.lower() == livre:
                print(un_livre.afficher_infos())
                trouve = True
                break
        # si on ne trouve pas le livre
        if not trouve:
          print(f"Le livre {livre} n'existe pas.")

    case "2" :
        livre = input("Quel livre cherchez-vous ? ")
        livre = livre.lower()
        trouve = False
        
        for un_livre in livres_charges:
          if un_livre.titre.lower() == livre:
              print(un_livre.emprunter())
              trouve = True
              break
        if not trouve:
            print(f"Le livre {livre} n'existe pas.")

    case "3" :
            livre = input("Quel livre cherchez-vous ? ")
            livre = livre.lower()
            trouve = False
            
            for un_livre in livres_charges:
              if un_livre.titre.lower() == livre:
                  print(un_livre.rendre())
                  trouve = True
                  break
            if not trouve:
                print(f"Le livre {livre} n'existe pas.")

    case "4" :
            livre = input("Quel livre cherchez-vous ? ")
            livre = livre.lower()
            trouve = False
            
            for un_livre in livres_charges:
              if un_livre.titre.lower() == livre:
                  note = input(f"Quelle note souhaitez-vous attribuer au livre {livre} ? (/5) ")
                  note = float(note)
                  assert note<=5 and note>=0, "La note doit être comprise entre 0 et 5"
                  print(un_livre.ajouter_note(note))
                  trouve = True
                  break
            if not trouve:
                print(f"Le livre {livre} n'existe pas.")

# on met à jour le fichier JSON
donnees_maj = []
for un_livre in livres_charges:
  nvdic = un_livre.to_dic()
  donnees_maj.append(nvdic)
with open("src/data.json", "w", encoding="utf-8") as fichier:
  json.dump(donnees_maj, fichier, indent=4) 
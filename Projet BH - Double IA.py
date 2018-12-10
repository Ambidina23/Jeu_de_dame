from tkinter import *
import random

# Définition des gestionnaires d'événements :

def new_game():
    delete_pions()
    pions()


def damier():       # Création du damier
    a=50
    b=0
    c=1
    for i in range(1,51):
        can1.create_rectangle(a, b, a+50, b+50, width=2, fill='#8B4513') # Marron foncé
        a=a+100
        if a==550:
            a=0
            b=b+50
            c=c+1
        if a==500:
            a=50
            b=b+50
            c=c+1

    a=0
    b=0
    for i in range(51,101):
        can1.create_rectangle(a, b, a+50, b+50, width=2, fill='#DEB887') # Marron clair
        a=a+100
        if a==550:
            a=0
            b=b+50
            c=c+1
        if a==500:
            a=50
            b=b+50
            c=c+1


def pions():        # Création des pions
    a=60
    b=10
    for i in range(0,40):
        if i in range (0,20):
            can1.create_oval(a, b, a+30, b+30, width=2, fill='black', tags = "computer")
        else:
            can1.create_oval(a, b, a+30, b+30, width=2, fill='white', tags = "player")
        a=a+100
        if a==560:
            a=10
            b=b+50
        if a==510:
            a=60
            b=b+50
        if b==210:
            a=60
            b=b+100


def delete_pions(): # Suppression des pions
    pions = can1.find_all()
    for i in pions:
        if i>100:
            can1.delete(i)


def tour_joueur(e):
    global flag,choix_prise, compteur
    if flag ==0:
        compteur=compteur+1
        #print("C'est le tour des blancs !")
        prise_obligatoire_joueur()             # Effectuer une prise obligatoire
        if choix_prise == 0:            # Si une prise n'a pas été faite...
            deplacement_joueur()        # Flag à 0 pour permettre le déplacement
        #print("Fin du tour des blancs. !")
        flag =1
    else:
        #print("Ca n'est pas le tour des blancs")
        "blabla"


def tour_ordinateur(e):
    global flag, choix_prise, check, compteur
    check=0
    if flag==1:
        compteur=compteur+1
        #print("C'est le tour des noirs !")
        prise_obligatoire_ordinateur()             # Effectuer une prise obligatoire
        if choix_prise == 0:            # Si une prise n'a pas été faite...
            deplacement_ordinateur()    # ... déplacer un pion
        #print("Fin du tour des noirs.")
        flag=0
    else:
        #print("Ca n'est pas le tour des noirs")
        "blabla"


def deplacement_ordinateur():
    # Récupération des identifiants de chaque pion de l'ordinateur
    pions_ordinateur = can1.find_withtag("computer")
    # Choix d'un nombre aléatoire
    a = random.randint(0,len(pions_ordinateur)-1)
    # Choix d'un pion de l'ordinateur au hasard à l'aide du nombre aléatoire
    a = pions_ordinateur[a]

    # Récupération des coordonnées de ce pion
    coords_pionc = can1.coords(a)
    x0c = coords_pionc[0]
    y0c = coords_pionc[1]
    x1c = coords_pionc[2]
    y1c = coords_pionc[3]

    # Récupération de l'identifiant de la case sur laquelle se trouve le pion
    case_dupion = can1.find_enclosed(x0c-15,y0c-15,x1c+15,y1c+15)
    case_dupion = case_dupion[0]

    case_possible_ordi = []

    # Voir si on est au bout du damier
    if case_dupion+5 > 50:
        #print("On ne pourra pas avancer")
        "blabla"
    else:
    
        # Voir si on peut aller à gauche
        if case_dupion%10==6:
            #print("On ne pourra pas aller à gauche")
            "blabla"
        else:
            gauche = can1.find_enclosed(x0c-55,y0c+5,x1c-35,y1c+55)
            if len(gauche)==0:
                case_possible_ordi.append(1)
        
        # Voir si on peut aller à droite
        if case_dupion%10==5:
            #print("On ne pourra pas aller à droite")
            "blabla"
        else:
            droite = can1.find_enclosed(x0c+35,y0c+5,x1c+55,y1c+55)
            if len(droite)==0:
                case_possible_ordi.append(2)

    # Déplacement sur une des cases libres, si elle existe
    if not case_possible_ordi:
        #print("Les deux cases sont prises, nouvelle tentative")
        deplacement_ordinateur()
    else:    
        d = random.randint(0,len(case_possible_ordi)-1)
        if case_possible_ordi[d]==1:
            case_arrivee=can1.find_enclosed(x0c-70,y0c+35,x1c-5,y1c+70)
            #case_arrivee=case_arrivee[0]
            #print("Déplacement 1")
            can1.coords(a,x0c-50,y0c+50,x1c-50,y1c+50)
            print(compteur,":",case_dupion,"-",case_arrivee)
        elif case_possible_ordi[d]==2:
            case_arrivee=can1.find_enclosed(x0c+30,y0c+30,x1c+70,y1c+70)
            #case_arrivee=case_arrivee[0]
            #print("Déplacement 2")
            can1.coords(a,x0c+50,y0c+50,x1c+50,y1c+50)
            print(compteur,":",case_dupion,"-",case_arrivee)
        else:
            print("Impossible...")


def deplacement_joueur():
    # Récupération des identifiants de chaque pion de l'ordinateur
    pions_ordinateur = can1.find_withtag("player")
    # Choix d'un nombre aléatoire
    a = random.randint(0,len(pions_ordinateur)-1)
    # Choix d'un pion de l'ordinateur au hasard à l'aide du nombre aléatoire
    a = pions_ordinateur[a]

    # Récupération des coordonnées de ce pion
    coords_pionc = can1.coords(a)
    x0c = coords_pionc[0]
    y0c = coords_pionc[1]
    x1c = coords_pionc[2]
    y1c = coords_pionc[3]

    # Récupération de l'identifiant de la case sur laquelle se trouve le pion
    case_dupion = can1.find_enclosed(x0c-15,y0c-15,x1c+15,y1c+15)
    case_dupion = case_dupion[0]

    case_possible_ordi = []

    # Voir si on est au bout du damier
    if case_dupion-5 < 1:
        #print("On ne pourra pas avancer")
        "blabla"
    else:
    
        # Voir si on peut aller à gauche
        if case_dupion%10==6:
            #print("On ne pourra pas aller à gauche")
            "blabla"
        else:
            gauche = can1.find_enclosed(x0c-55,y0c-55,x1c-35,y1c-5)
            if len(gauche)==0:
                case_possible_ordi.append(1)
        
        # Voir si on peut aller à droite
        if case_dupion%10==5:
            #print("On ne pourra pas aller à droite")
            "blabla"
        else:
            droite = can1.find_enclosed(x0c+35,y0c-55,x1c+55,y1c-5)
            if len(droite)==0:
                case_possible_ordi.append(2)
    #print("case_possible_ordi",case_possible_ordi)
    # Déplacement sur une des cases libres, si elle existe
    if not case_possible_ordi:
        #print("Les deux cases sont prises, nouvelle tentative")
        deplacement_joueur()
    else:    
        d = random.randint(0,len(case_possible_ordi)-1)
        if case_possible_ordi[d]==1:
            case_arrivee=can1.find_enclosed(x0c-70,y0c-70,x1c-5,y1c-5)
            #case_arrivee=case_arrivee[0]
            can1.coords(a,x0c-50,y0c-50,x1c-50,y1c-50)
            print(compteur,":",case_dupion,"-",case_arrivee)
            #tour_ordinateur()
        elif case_possible_ordi[d]==2:
            case_arrivee=can1.find_enclosed(x0c+30,y0c-70,x1c+5,y1c-35)
            #case_arrivee=case_arrivee[0]
            can1.coords(a,x0c+50,y0c-50,x1c+50,y1c-50)
            print(compteur,":",case_dupion,"-",case_arrivee)
            #tour_ordinateur()
        else:
            print("Impossible...")


def prise_obligatoire_ordinateur(): # A améliorer
        global choix_prise, prise_faite, compteur
        pions_possibles = []
        pions_ordinateur_restant = can1.find_withtag("computer") # On récupère les pions restants de l'ordinateur
        for i in pions_ordinateur_restant: # On boucle sur chacun de ces pions
            choix_possible = []
            
            coords_item = can1.coords(i) # On récupère les coordonnées du pion
            #print("Coordonnées du point étudié : ",coords_item)
            
            item_found = can1.find_enclosed(coords_item[0]-55,coords_item[1]-55,coords_item[2]+55,coords_item[3]+55) # On cherche des voisins
            #print("Numéro de l'item s'il existe : ",item_found)
            
            for j in range(0,len(item_found)): # On boucle sur chaque voisin
                if item_found[j] > 120: # Si le voisin est un adversaire
                    #print("Le pion",item_found[j],"est à portée du pion",i,"!")
                    # Voir s'il peut être pris.
                    coords_item2 = can1.coords(item_found[j])
                    diff_coords = []
                    diff_coords.append(coords_item[0]-(coords_item[0]-coords_item2[0])*2-5)
                    diff_coords.append(coords_item[1]-(coords_item[1]-coords_item2[1])*2-5)
                    diff_coords.append(coords_item[2]-(coords_item[2]-coords_item2[2])*2+5)
                    diff_coords.append(coords_item[3]-(coords_item[3]-coords_item2[3])*2+5)
                    
                    item_behind =  can1.find_enclosed(diff_coords[0],diff_coords[1],diff_coords[2],diff_coords[3])

                    if len(can1.find_enclosed(diff_coords[0]-15,diff_coords[1]-15,diff_coords[2]+15,diff_coords[3]+15))==0:
                        print("problème pièce sur le côté")
                    
                    elif len(item_behind) == 0:
                        #print("La pièce peut être prise")
                        choix_possible.append(item_found[j])
                        
                    else:
                        "blabla"
                        #print("La pièce ne peut pas être prise")

                    # Examiner combien de pieces sont prenables pour chaque possibilité
                    # Choisir la meilleure, sinon au hasard

            if len(choix_possible) ==1:
                #print("Choix possibles de",i,":",choix_possible)
                pions_possibles.append(choix_possible[0])
            elif len(choix_possible) > 1:
                e = random.randint(0,len(choix_possible)-1)
                # Choix d'un pion de l'ordinateur au hasard à l'aide du nombre aléatoire
                pions_possibles.append(choix_possible[e])
            else:
                pions_possibles.append(0)

        #print("Choix : ",pions_possibles)
      
        x = 0

        for num in pions_possibles:
            x = x + num
        choix_prise=0
        if x !=0:
            while choix_prise==0:
                f = random.randint(0,len(pions_possibles)-1)
                if pions_possibles[f]!=0:
                    choix_prise=1
                    g=pions_ordinateur_restant[f]
                    
                else:
                    #print("Prise sélectionné non valable")
                    "blabla"
            #print("Le choix de prise sera le pion",pions_possibles[f],"par le pion", g)
            coords_pionap = can1.coords(pions_possibles[f])
            x0ap = coords_pionap[0]
            y0ap = coords_pionap[1]
            x1ap = coords_pionap[2]
            y1ap = coords_pionap[3]

            coords_pionqp = can1.coords(g)
            x0qp = coords_pionqp[0]
            y0qp = coords_pionqp[1]
            x1qp = coords_pionqp[2]
            y1qp = coords_pionqp[3]

            x0d = coords_pionap[0] + (coords_pionap[0] - coords_pionqp[0])
            y0d = coords_pionap[1] + (coords_pionap[1] - coords_pionqp[1])
            x1d = coords_pionap[2] + (coords_pionap[2] - coords_pionqp[2])
            y1d = coords_pionap[3] + (coords_pionap[3] - coords_pionqp[3])
            #print("x0d,y0d,x1d,y1d =",x0d,y0d,x1d,y1d)
            case_arrivee = can1.find_enclosed(x0d-15,y0d-15,x1d+15,y1d+15)
            can1.coords(g,x0d,y0d,x1d,y1d)
            case_dupion = can1.find_enclosed(x0qp-15,y0qp-15,x1qp+15,y1qp+15)
            can1.delete(pions_possibles[f])

            
            print(compteur,".",case_dupion,"x",case_arrivee)
            
        else:
            "blabla"
            #print("Pas de prise possible")
        
            
def prise_obligatoire_joueur():
    global choix_prise, prise_faite, compteur
    pions_possibles = []
    pions_joueur_restant = can1.find_withtag("player")
    for i in pions_joueur_restant:
        choix_possible = []
        coords_item = can1.coords(i)
        #print("Coordonnées du point étudié : ")
        #print(coords_item)
        #print("Numéro de l'item s'il existe : ")
        item_found = can1.find_enclosed(coords_item[0]-55,coords_item[1]-55,coords_item[2]+55,coords_item[3]+55)
        #print (item_found)
        for j in range(0,len(item_found)):
            if item_found[j] > 100 and item_found[j] < 121:
                #print("Le pion",item_found[j],"est à portée du pion",i,"!")
                # Voir s'il peut être pris.
                coords_item2 = can1.coords(item_found[j])
                diff_coords = []
                diff_coords.append(coords_item[0]-(coords_item[0]-coords_item2[0])*2-5)
                diff_coords.append(coords_item[1]-(coords_item[1]-coords_item2[1])*2-5)
                diff_coords.append(coords_item[2]-(coords_item[2]-coords_item2[2])*2+5)
                diff_coords.append(coords_item[3]-(coords_item[3]-coords_item2[3])*2+5)
                    
                item_behind =  can1.find_enclosed(diff_coords[0],diff_coords[1],diff_coords[2],diff_coords[3])

                if len(item_behind) == 0:
                    #print("La pièce peut être prise")
                    choix_possible.append(item_found[j])
                        
                else:
                    "blabla"
                    #print("La pièce ne peut pas être prise")


        if len(choix_possible) ==1:
            #print("Choix possibles de",i,":",choix_possible)
            pions_possibles.append(choix_possible[0])
        elif len(choix_possible) > 1:
            e = random.randint(0,len(choix_possible)-1)
            # Choix d'un pion de l'ordinateur au hasard à l'aide du nombre aléatoire
            pions_possibles.append(choix_possible[e])
        else:
            pions_possibles.append(0)

    #print("Choix : ",pions_possibles)
    #print("Liste pions restants =",pions_joueur_restant)
    x = 0
    for num in pions_possibles:                             # Additionne les valeurs du tableau
        x = x + num                                         # pour éviter de faire une boucle infinie

    choix_prise=0
    if x !=0:
        while choix_prise==0:
            f = random.randint(0,len(pions_possibles)-1)
            if pions_possibles[f]!=0:
                choix_prise=1
                g=pions_joueur_restant[f]
                    
            else:
                #print("Prise sélectionné non valable")
                "blabla"
        #print("Le choix de prise sera le pion",pions_possibles[f],"par le pion", g)
            
        coords_pionap = can1.coords(pions_possibles[f])
        x0ap = coords_pionap[0]
        y0ap = coords_pionap[1]
        x1ap = coords_pionap[2]
        y1ap = coords_pionap[3]

        coords_pionqp = can1.coords(g) ### problème avec le +121.... car des pions ont été supprimés...
        x0qp = coords_pionqp[0]
        y0qp = coords_pionqp[1]
        x1qp = coords_pionqp[2]
        y1qp = coords_pionqp[3]

        x0d = coords_pionap[0] + (coords_pionap[0] - coords_pionqp[0])
        y0d = coords_pionap[1] + (coords_pionap[1] - coords_pionqp[1])
        x1d = coords_pionap[2] + (coords_pionap[2] - coords_pionqp[2])
        y1d = coords_pionap[3] + (coords_pionap[3] - coords_pionqp[3])
        #print("x0d,y0d,x1d,y1d =",x0d,y0d,x1d,y1d)
        #print("Le pion",g,"va prendre le pion",pions_possibles[f])
        case_arrivee = can1.find_enclosed(x0d-15,y0d-15,x1d+15,y1d+15)
        can1.coords(g,x0d,y0d,x1d,y1d)
        case_dupion = can1.find_enclosed(x0qp-15,y0qp-15,x1qp+15,y1qp+15)
        can1.delete(pions_possibles[f])
        print(compteur,".",case_dupion,"x",case_arrivee)
        ### Problème : prend aussi les pions sur le bord du damier, à régler.
                    
    else:
        #print("Pas de prise possible")
        "blabla"


#============= Programme principal =============

# Les variables suivantes seront utilisées de manière globale :
choix_prise = 0         # Commutateurs
flag = 0
compteur = 0

# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Jeu de dames avec deux IA jouant au hasard et prise obligatoire simple")
# Création des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=500, width=500)
can1.pack(side=LEFT, padx =5, pady =5)

damier()
pions()

# Mouseclick event
can1.bind("<Button 1>",tour_joueur)
can1.bind("<Button 3>",tour_ordinateur)

bou1 = Button(fen1, text='Nouvelle partie', width =12, command=new_game)
bou1.pack()

# Démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()

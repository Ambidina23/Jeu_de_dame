from tkinter import *
import random

# Définition des gestionnaires d'événements :

def new_game():
    delete_pions()
    pions()         ### Problème : Les pions qui sont créés à nouveau ont un identifiant plus élevé. ###


def damier():       # Création du damier
    a=50
    b=0
    c=1
    for i in range(1,51):
        can1.create_rectangle(a, b, a+50, b+50, width=2, fill='#8B4513', tags="use") # Marron foncé
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
    

def tour_ordinateur():
    print("C'est le tour de l'ordinateur !")
    # Prise obligatoire ?
        # Voir chaque pion de son équipe
        # Voir si un pion adverse est autour
            # S'il y en a un, voir derriere
    global flag
    prise_obligatoire()
    deplacement_ordinateur()
    # Si oui, voir toutes les prises possibles et en réaliser une
    # Si non, choisir un pion et le déplacer

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
    # Voir si on peut aller à gauche
    if case_dupion%10==6:
        print("On ne pourra pas aller à gauche")
    else:
        gauche = can1.find_enclosed(x0c-55,y0c+5,x1c-35,y1c+55)
        if len(gauche)==0:
            case_possible_ordi.append(1)
    
    # Voir si on peut aller à droite
    if case_dupion%10==5:
        print("On ne pourra pas aller à droite")
    else:
        droite = can1.find_enclosed(x0c+35,y0c+5,x1c+55,y1c+55)
        if len(droite)==0:
            case_possible_ordi.append(2)

    # Déplacement sur une des cases libres, si elle existe
    if not case_possible_ordi:
        print("Les deux cases sont prises, nouvelle tentative")
        deplacement_ordinateur()
    else:    
        d = random.randint(0,len(case_possible_ordi)-1)
        if case_possible_ordi[d]==1:
            can1.coords(a,x0c-50,y0c+50,x1c-50,y1c+50)
        elif case_possible_ordi[d]==2:
            can1.coords(a,x0c+50,y0c+50,x1c+50,y1c+50)
        else:
            print("Impossible...")

def tour_joueur():
    print("C'est le tour du joueur !")

def prise_obligatoire(): # A améliorer
    if flag==0:
        for i in range(101,121):
            choix_possible = []
            coords_item = can1.coords(i)
            #print("Coordonnées du point étudié : ")
            #print(coords_item)
            #print("Numéro de l'item s'il existe : ")
            item_found = can1.find_enclosed(coords_item[0]-55,coords_item[1]-55,coords_item[2]+55,coords_item[3]+55)
            #print (item_found)
            for j in range(0,len(item_found)):
                if item_found[j] > 120:
                    print("Le pion",item_found[j],"est à portée du pion",i,"!")
                    # Voir s'il peut être pris.
                    coords_item2 = can1.coords(item_found[j])
                    diff_coords = []
                    diff_coords.append(coords_item[0]-(coords_item[0]-coords_item2[0])*2-5)
                    diff_coords.append(coords_item[1]-(coords_item[1]-coords_item2[1])*2-5)
                    diff_coords.append(coords_item[2]-(coords_item[2]-coords_item2[2])*2+5)
                    diff_coords.append(coords_item[3]-(coords_item[3]-coords_item2[3])*2+5)
                    ###print ("diff_coords =",diff_coords)
                    print("Coords de la pièce qui pourrait prendre :",coords_item[0],coords_item[1],coords_item[2],coords_item[3])
                    print("Coords de la pièce qui pourrait être prise:",coords_item2[0],coords_item2[1],coords_item2[2],coords_item2[3])
                    ###print("Coords examinées :",coords_item[0]-(coords_item[0]-coords_item2[0])*2-5,coords_item[1]-(coords_item[1]-coords_item2[1])*
                                                      #2-5,coords_item[2]-(coords_item[2]-coords_item2[2])*2+5,coords_item[3]-(coords_item[3]-coords_item2[3])*2+5)
                    item_behind =  can1.find_enclosed(diff_coords[0],diff_coords[1],diff_coords[2],diff_coords[3])
                    print ("item_behind =",item_behind)
                    ###print ("Coords de l'item 141",can1.coords(141))

                    if len(item_behind) == 0:
                        print("La pièce peut être prise")
                        choix_possible.append(item_found[j])
                        
                    else:
                        print("La pièce ne peut pas être prise")

                    # Examiner combien de pieces sont prenables pour chaque possibilité
                    # Choisir la meilleure, sinon au hasard

            #### Voir liste
            print("Choix possibles :",choix_possible)
            ### Analyse des choix ?
            for k in range (0, len(choix_possible)):
                print("...")
                    
                    
                    
            
    else:
        for i in range(121,141):
            coords_item = can1.coords(i)
            #print("Coordonnées du point étudié : ")
            #print(coords_item)
            #print("Numéro de l'item s'il existe : ")
            item_found = can1.find_enclosed(coords_item[0]-55,coords_item[1]-55,coords_item[2]+55,coords_item[3]+55)
            #print (item_found)
            for j in range(0,len(item_found)):
                if item_found[j] > 100 and item_found[j] <121:
                    print("Le pion",item_found[j],"est à portée du pion",i,"!")
                    # Voir s'il peut être pris.
                    coords_item2 = can1.coords(item_found[j])
                    diff_coords = []
                    diff_coords.append(coords_item[0]-(coords_item[0]-coords_item2[0])*2-5)
                    diff_coords.append(coords_item[1]-(coords_item[1]-coords_item2[1])*2-5)
                    diff_coords.append(coords_item[2]-(coords_item[2]-coords_item2[2])*2+5)
                    diff_coords.append(coords_item[3]-(coords_item[3]-coords_item2[3])*2+5)
                    ###print ("diff_coords =",diff_coords)
                    print("Coords de la pièce qui pourrait prendre :",coords_item[0],coords_item[1],coords_item[2],coords_item[3])
                    print("Coords de la pièce qui pourrait être prise:",coords_item2[0],coords_item2[1],coords_item2[2],coords_item2[3])
                    ###print("Coords examinées :",coords_item[0]-(coords_item[0]-coords_item2[0])*2-5,coords_item[1]-(coords_item[1]-coords_item2[1])*
                                                      #2-5,coords_item[2]-(coords_item[2]-coords_item2[2])*2+5,coords_item[3]-(coords_item[3]-coords_item2[3])*2+5)
                    item_behind =  can1.find_enclosed(diff_coords[0],diff_coords[1],diff_coords[2],diff_coords[3])
                    print ("item_behind =",item_behind)
                    ###print ("Coords de l'item 141",can1.coords(141))

                    # Examiner combien de pieces sont prenables pour chaque possibilité
                    # Choisir la meilleure, sinon au hasard

# Determine the origin by clicking
def getorigin(eventorigin):
    global x0,y0, deplacementencours, jeton, case_depart
    if deplacementencours == 0: # Au premier clic, on récupère les coordonnées de la souris et l'identifiant du pion sélectionné s'il y en a un
        x0 = eventorigin.x
        y0 = eventorigin.y
             
        x0 = int(x0/50)*50
        y0 = int(y0/50)*50

        jeton = can1.find_enclosed(x0-5,y0-5,x0+55,y0+55)
        case_depart = jeton[0]
        if len(jeton)==2:
            jeton = jeton[1]
        else:
            jeton = jeton[0]
            
        if jeton > 120: ### Possible solution : On pourrait comparer à la liste de pions correspondant au bon tag. ###
            deplacementencours=1
            
    elif deplacementencours == 1: # Au second clic, on récupère les coordonnées de la souris et la destination
        x0 = eventorigin.x
        y0 = eventorigin.y
             
        x0 = int(x0/50)*50
        y0 = int(y0/50)*50

        case_destination = can1.find_enclosed(x0-5,y0-5,x0+55,y0+55)

        if len(case_destination)==2:
            print("Il y a déjà un pion sur cette case")
        else:
            case_destination = case_destination[0]
            if case_destination > 50:
                print("Vous ne pouvez pas déplacer votre pion sur cette case")
            else: # Si la case destination est une case utilisable (1 à 50)
                 # On pourrait grouper les deux premiers cas...
                print("Vérification si case faisable")
                print("Case départ :",case_depart,"et case destination =",case_destination)
                if case_depart%10==6 and case_depart-case_destination==5: # Cas tout à gauche
                    print("Cas ou on est en case 6 16 26 36 46 (tout à gauche)")
                    can1.coords(jeton,x0+10,y0+10,x0+40,y0+40)
                    deplacementencours = 0
                    tour_ordinateur()
                    
                elif case_depart%10==5 and case_depart-case_destination==5: # cas tout à droite
                    print("Cas ou on est en case 5 15 25 35 45 (tout à droite)")
                    can1.coords(jeton,x0+10,y0+10,x0+40,y0+40)
                    deplacementencours = 0
                    tour_ordinateur()

                elif int(case_depart/5)%2==0 and (case_depart-case_destination==5 or case_depart-case_destination==4) and case_depart%10!=0: # cas ligne pair
                    print("Cas classique 1")
                    can1.coords(jeton,x0+10,y0+10,x0+40,y0+40)
                    deplacementencours = 0
                    tour_ordinateur()

                elif int(case_depart/5)%2==0 and (case_depart-case_destination==6 or case_depart-case_destination==5) and case_depart%10==0: # cas ligne pair
                    print("Cas classique 2")
                    can1.coords(jeton,x0+10,y0+10,x0+40,y0+40)
                    deplacementencours = 0
                    tour_ordinateur()

                elif int(case_depart/5)%2==1 and (case_depart-case_destination==6 or case_depart-case_destination==5) and case_depart%10!=0 and case_depart%5!=0: # cas ligne impair
                    print("Cas classique 3")
                    can1.coords(jeton,x0+10,y0+10,x0+40,y0+40)
                    deplacementencours = 0
                    tour_ordinateur()

                else:
                    print("On ne se déplace qu'en diagonale et d'une case")

    else:
        print("Pas votre tour")
    
 
#========== Programme principal =============
 
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10         # coordonnées initiales
dx, dy = 15, 0          # 'pas' du déplacement
flag =0                 # commutateur

deplacementencours = 0
 
# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Jeu de dames avec IA jouant au hasard")
# création des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=500, width=500)
can1.pack(side=LEFT, padx =5, pady =5)

damier()
pions()

#mouseclick event
can1.bind("<Button 1>",getorigin)

bou1 = Button(fen1,text='Quitter', width =8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Nouvelle partie', width =12, command=new_game)
bou2.pack()
bou3 = Button(fen1, text='Arrêter', width =8)
bou3.pack()
# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()

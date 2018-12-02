#                      #
# Code assez brouillon #
#                      #

from tkinter import *
 
# définition des gestionnaires
# d'événements :
 
def stop_it():
    "arret de l'animation"
    global flag
    flag =0
    tour_ordinateur()
 
def start_it():
    "démarrage de l'animation"
    global flag
    if flag ==0:         # pour ne lancer qu'une seule boucle # plus trop le cas si on utilise le flag pour le tour
        flag =1
        tour_joueur()

def tour_ordinateur():
    print("C'est le tour de l'ordinateur !")
    # Prise obligatoire ?
        # Voir chaque pion de son équipe
        # Voir si un pion adverse est autour
            # S'il y en a un, voir derriere
    global flag
    prise_obligatoire()
    # Si oui, voir toutes les prises possibles et en réaliser une
    # Si non, choisir un pion et le déplacer
    fen1.after(500,tour_joueur()) 

def tour_joueur():
    print("C'est le tour du joueur !")

def prise_obligatoire():
    if flag==0:
        for i in range(101,121):
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

                    # Examiner combien de pieces sont prenables pour chaque possibilité
                    # Choisir la meilleure, sinon au hasard
            
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
    global x0,y0, flag, deplacementencours, jeton
    if flag == 1 and deplacementencours == 0:
        x0 = eventorigin.x
        y0 = eventorigin.y
        print(x0,y0)
    
        jeton = can1.find_closest(x0,y0,halo=20) # à améliorer , start='140' ?
        jeton = jeton[0]
        print (jeton)
        if jeton > 120:
            print("Avant la fonction coords")
            deplacementencours=1
            

            #fen1.after(500,tour_ordinateur())
            
    elif flag == 1 and deplacementencours == 1: # Case impossible selectionnable...
        flag = 0
        x0 = eventorigin.x
        y0 = eventorigin.y
        print("Avant",x0,y0)
             
        x0 = int(x0/50)*50
        y0 = int(y0/50)*50
        print("Après",x0,y0)

        case_destination = can1.find_enclosed(x0-5,y0-5,x0+55,y0+55)
        #case_destination = can1.find_enclosed(x0-5,y0-5,x0+55,y0+5)
        print("case destination :",case_destination)
        if len(case_destination)==2:
            print("Il y a déjà un pion sur cette case")
        elif len(case_destination)==1:
            print ("can1.gettags(case_destination[0] :",can1.gettags(case_destination[0]))
            if (can1.gettags(case_destination[0]) == "donotuse"):
                print("Vous ne pouvez pas déplacer votre pion sur cette case")
            else:
                can1.coords(jeton,x0+10,y0+10,x0+40,y0+40)  
        
        
        

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
fen1.title("Exercice d'animation avec Tkinter")
# création des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=500, width=500)
can1.pack(side=LEFT, padx =5, pady =5)


a=0
b=0
c=0
for i in range(0,100):
    if (i%2==0 and c%2==0) or (i%2!=0 and c%2!=0):
        can1.create_rectangle(a, b, a+50, b+50, width=2, fill='#DEB887', tags = "donotuse")
    else:
        can1.create_rectangle(a, b, a+50, b+50, width=2, fill='#8B4513') 
    a=a+50
    if a==500:
        a=0
        b=b+50
        c=c+1
        

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

### can1.create_oval(10, 260, 10+30, 260+30, width=2, fill='white') ### Pour tester

#mouseclick event
can1.bind("<Button 1>",getorigin)

### Inutile mais à garder pour l'instant

#lines = []
#for x in range(10):
#    item = can1.create_line(150,452,203,437)
#    lines.append(item)
#print (lines)
   
###

bou1 = Button(fen1,text='Quitter', width =8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Démarrer', width =8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text='Arrêter', width =8, command=stop_it)
bou3.pack()
# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()

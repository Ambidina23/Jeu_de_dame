#                      #
# Code assez brouillon #
#                      #

from tkinter import *
 
# définition des gestionnaires
# d'événements :
 
def stop_it():
    "arret de l'animation"
    global flag
    flag = 1
    tour_ordinateur()
 
def start_it():
    "démarrage de l'animation"
    global flag
    if flag == 0:         # pour ne lancer qu'une seule boucle # plus trop le cas si on utilise le flag pour le tour
        flag = 1
        tour_ordinateur()

def tour_ordinateur():
    print("C'est le tour de l'ordinateur !")
    global flag
    prise_obligatoire()
    fen1.after(500,tour_joueur()) 

def tour_joueur():
    print("C'est le tour du joueur !")

def prise_obligatoire():
    if flag==1:
        for i in range(108,111): ### On examine les possibilités de prise de chaque pion de l'ordinateur ###
            print("On examine les possibilités de prise du pion",i)
            choix_possible = []
            coords_item = can1.coords(i)
            item_found = can1.find_enclosed(coords_item[0]-55,coords_item[1]-55,coords_item[2]+55,coords_item[3]+55)
            for j in range(0,len(item_found)): ### Pour chaque voisin du pion de l'ordinateur...
                
                if item_found[j] > 100 and item_found[j] < 108: ### ... on regarde si c'est un pion de l'humain
                    print("Le pion",item_found[j],"est à portée du pion",i,"!")
                    # Voir s'il peut être pris.
                    coords_item2 = can1.coords(item_found[j])
                    diff_coords = []
                    diff_coords.append(coords_item[0]-(coords_item[0]-coords_item2[0])*2-5)
                    diff_coords.append(coords_item[1]-(coords_item[1]-coords_item2[1])*2-5)
                    diff_coords.append(coords_item[2]-(coords_item[2]-coords_item2[2])*2+5)
                    diff_coords.append(coords_item[3]-(coords_item[3]-coords_item2[3])*2+5)
                    item_behind =  can1.find_enclosed(diff_coords[0],diff_coords[1],diff_coords[2],diff_coords[3])
                    print ("item_behind =",item_behind)
                    
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
        print("Pas censé être là") 
 
#========== Programme principal =============
 
# les variables suivantes seront utilisées de manière globale :
x1, y1 = 10, 10         # coordonnées initiales
dx, dy = 15, 0          # 'pas' du déplacement
flag =0                 # commutateur
 
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
        can1.create_rectangle(a, b, a+50, b+50, width=2, fill='#DEB887')
    else:
        can1.create_rectangle(a, b, a+50, b+50, width=2, fill='#8B4513')  
    a=a+50
    if a==500:
        a=0
        b=b+50
        c=c+1
    #print(i,can1.coords(i)) #Pourquoi la case 100 est créée mais pas son print ?
        

can1.create_oval(110, 60, 140, 90, width=2, fill='white')   #101
can1.create_oval(110, 160, 140, 190, width=2, fill='white') #102
can1.create_oval(60, 310, 90, 340, width=2, fill='white')   #103
can1.create_oval(160, 310, 190, 340, width=2, fill='white') #104
can1.create_oval(260, 310, 290, 340, width=2, fill='white') #105
can1.create_oval(360, 310, 390, 340, width=2, fill='white') #106
can1.create_oval(260, 210, 290, 240, width=2, fill='white') #107

can1.create_oval(160, 210, 190, 240, width=2, fill='black') #108
can1.create_oval(210, 260, 240, 290, width=2, fill='black') #109
can1.create_oval(110, 360, 140, 390, width=2, fill='black') #110

for i in range(101,111):
    print(i,can1.coords(i))

bou1 = Button(fen1,text='Quitter', width =8, command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1, text='Démarrer', width =8, command=start_it)
bou2.pack()
bou3 = Button(fen1, text='Arrêter', width =8, command=stop_it)
bou3.pack()
# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()

from tkinter import *
import random

# définition des gestionnaires
# d'événements :
 
def restart():
    print("TODO")

def tour_ordinateur():
    global tour, entier
    if tour%2==0:
        print("Tour",tour,"C'est le tour de l'ordinateur !")
        
        joue = list(can1.find_withtag("full")) # Liste toutes les cases ayant déjà été choisi
        entier = list(set(entier)-set(joue))   # Liste les cases libres
        a = random.randint(0,len(entier)-1)    
        a = entier[a]

        if (a<2):
            can1.create_oval(10,10,40,40, fill='black')
        elif (a<3):
            can1.create_oval(60,10,90,40, fill='black')
        elif (a<4):
            can1.create_oval(110,10,140,40, fill='black')
        elif (a<5):
            can1.create_oval(10,60,40,90, fill='black')
        elif (a<6):
            can1.create_oval(60,60,90,90, fill='black')
        elif (a<7):
            can1.create_oval(110,60,140,90, fill='black')
        elif (a<8):
            can1.create_oval(10,110,40,140, fill='black')
        elif (a<9):
            can1.create_oval(60,110,90,140, fill='black')
        elif (a<10):
            can1.create_oval(110,110,140,140, fill='black')

        can1.addtag_withtag("black",a)
        can1.addtag_withtag("full",a)
        print("L'ordinateur place un pion noir en ",a)    
        if tour > 4:
            check_winner()
        tour=tour+1
    
    else:
        print("Pas le tour de l'ordinateur")
        

def piece(eventorigin):
    global tour
    if tour%2==1:
        print("Tour",tour,"C'est le tour du joueur !")
        color = 'blue'
        x=int(eventorigin.char)
        if (x > 0 and x< 10):
            if (len(can1.gettags(x))!=0):
                print("Case non sélectionnable")
            else: # On pourrait utiliser un switch case
                if (x<2):
                    can1.create_oval(10,10,40,40, fill='red')  
                elif (x<3):
                        can1.create_oval(60,10,90,40, fill='red')
                elif (x<4):
                        can1.create_oval(110,10,140,40, fill='red')
                elif (x<5):
                        can1.create_oval(10,60,40,90, fill='red')
                elif (x<6):
                        can1.create_oval(60,60,90,90, fill='red')
                elif (x<7):
                        can1.create_oval(110,60,140,90, fill='red')
                elif (x<8):
                        can1.create_oval(10,110,40,140, fill='red')
                elif (x<9):
                        can1.create_oval(60,110,90,140, fill='red')
                elif (x<10):
                        can1.create_oval(110,110,140,140, fill='red')

                if tour%2==1:
                    can1.addtag_withtag("red",x)
                
                else:
                    can1.addtag_withtag("black",x)
                can1.addtag_withtag("full",x)
                print("Le joueur place un pion rouge en ",x)
                
                if tour > 4:
                    check_winner()
                
                if gagnant==0:
                    tour=tour+1
                    tour_ordinateur()
    
    else:
        print("Pas votre tour de jouer")

def check_winner():
    for i in range (1,3):
        if i==1:
            items = can1.find_withtag("black")
            if (set([1,2,3]).issubset(items)) or (set([4,5,6]).issubset(items)) or (set([7,8,9]).issubset(items)) or (set([1,4,7]).issubset(items)) or (set([2,5,8]).issubset(items)) or (set([3,6,9]).issubset(items)) or (set([1,5,9]).issubset(items)) or (set([3,5,7]).issubset(items)):
                print("Les noirs gagnent.")
                print("Appuyez sur une touche pour recommencer")
                gagnant=1
                restart()
        
        elif i==2:
            items = can1.find_withtag("red")
            if (set([1,2,3]).issubset(items)) or (set([4,5,6]).issubset(items)) or (set([7,8,9]).issubset(items)) or (set([1,4,7]).issubset(items)) or (set([2,5,8]).issubset(items)) or (set([3,6,9]).issubset(items)) or (set([1,5,9]).issubset(items)) or (set([3,5,7]).issubset(items)):
                print("Les rouges gagnent.")
                print("Appuyez sur une touche pour recommencer")
                gagnant=1
                restart()
        
        elif tour==10:
            print("Match nul")
        
        else:
            print("La partie continue")
            
 
#========== Programme principal =============
 
# les variables suivantes seront utilisées de manière globale :
tour=1              # Compteur de tour
gagnant=0           # Gagnant ou pas (Utiliser un booléen ?) 0 : Non / 1 : Oui
            
# Création du widget principal ("parent") :
fen1 = Tk()
fen1.title("Morpion avec IA jouant au hasard")
# création des widgets "enfants" :
can1 = Canvas(fen1,bg='dark grey',height=150, width=150)
can1.pack(side=LEFT, padx =5, pady =5)

# Création de la grille
a=0
b=0
for i in range(0,9):
    can1.create_rectangle(a, b, a+50, b+50, width=2, fill='#FFFFFF')
    a=a+50
    if a%3 == 0:
        a=0
        b=b+50

# Liste les cases de la grille
entier = list(can1.find_all())

# Attente du relachement d'une touche du clavier (Actuellement, appuyer sur autre chose que le pavé numérique provoque une erreur)
fen1.bind('<KeyRelease>', piece)

# démarrage du réceptionnaire d'évènements (boucle principale) :
fen1.mainloop()

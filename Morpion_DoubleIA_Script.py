from tkinter import *
import random
import time

# Définition des gestionnaires d'événements :

def grille():   # Création de la grille
    a = 100
    b = 100
    for i in range(0,9):
        can1.create_rectangle(a, b, a+50, b+50, width=2, fill='#FFFFFF')        # Création des cases
        a = a-50
        if a == -50:
            a = 100
            b = b-50


def simulation():   # 
    global tour, gagnant
    fen1.update()
    time.sleep(1)
    while not gagnant:
        if tour%2==1:
            piece()
            fen1.update()
            time.sleep(0.5)
        else:
            tour_ordinateur()
            fen1.update()
            time.sleep(0.5)

def recuperation(n, r):
    global tour
    tour = 1
    for noir in n:
        if (noir<2):
            can1.create_oval(10,110,40,140, fill='black')
        elif (noir<3):
            can1.create_oval(60,110,90,140, fill='black')
        elif (noir<4):
            can1.create_oval(110,110,140,140, fill='black')
        elif (noir<5):
            can1.create_oval(10,60,40,90, fill='black')
        elif (noir<6):
            can1.create_oval(60,60,90,90, fill='black')
        elif (noir<7):
            can1.create_oval(110,60,140,90, fill='black')
        elif (noir<8):
            can1.create_oval(10,10,40,40, fill='black')
        elif (noir<9):
            can1.create_oval(60,10,90,40, fill='black')
        elif (noir<10):
            can1.create_oval(110,10,140,40, fill='black')
        can1.addtag_withtag("black",noir)
        can1.addtag_withtag("full",noir)
        tour = tour +1

    for rouge in r:
        if (rouge<2):
            can1.create_oval(10,110,40,140, fill='red')
        elif (rouge<3):
            can1.create_oval(60,110,90,140, fill='red')
        elif (rouge<4):
            can1.create_oval(110,110,140,140, fill='red')
        elif (rouge<5):
            can1.create_oval(10,60,40,90, fill='red')
        elif (rouge<6):
            can1.create_oval(60,60,90,90, fill='red')
        elif (rouge<7):
            can1.create_oval(110,60,140,90, fill='red')
        elif (rouge<8):
            can1.create_oval(10,10,40,40, fill='red')
        elif (rouge<9):
            can1.create_oval(60,10,90,40, fill='red')
        elif (rouge<10):
            can1.create_oval(110,10,140,40, fill='red')
        can1.addtag_withtag("red",rouge)
        can1.addtag_withtag("full",rouge)
        tour = tour +1
    print("Fin de la récupération")
    

def restart():  # Remise à zéro
    global tour, gagnant, entier
    pions = can1.find_all()     # Récupération des identifiants
    for i in pions:
        if i < 10:
            can1.dtag(i, "full")        # Suppression des tags
            can1.dtag(i, "red")         # Suppression des tags
            can1.dtag(i, "black")       # Suppression des tags
        if i > 9:
            can1.delete(i)      # Suppression des pions
    tour = 1
    gagnant = 0
    entier = list(can1.find_all())
    

def tour_ordinateur():
    global tour, entier, gagnant
    if tour%2 == 0 and gagnant == 0:      
        joue = list(can1.find_withtag("full")) # Liste toutes les cases ayant déjà été choisi
        entier = list(set(entier)-set(joue))   # Liste les cases libres
        a = random.randint(0,len(entier)-1)    
        a = entier[a]

        if (a<2):
            can1.create_oval(10,110,40,140, fill='black')
        elif (a<3):
            can1.create_oval(60,110,90,140, fill='black')
        elif (a<4):
            can1.create_oval(110,110,140,140, fill='black')
        elif (a<5):
            can1.create_oval(10,60,40,90, fill='black')
        elif (a<6):
            can1.create_oval(60,60,90,90, fill='black')
        elif (a<7):
            can1.create_oval(110,60,140,90, fill='black')
        elif (a<8):
            can1.create_oval(10,10,40,40, fill='black')
        elif (a<9):
            can1.create_oval(60,10,90,40, fill='black')
        elif (a<10):
            can1.create_oval(110,10,140,40, fill='black')

        can1.addtag_withtag("black",a)
        can1.addtag_withtag("full",a)
        print(tour,": L'ordinateur place un pion noir en",a)    
        if tour > 4:
            check_winner()
        tour=tour+1
    
    else:
        "Pas le tour de l'ordinateur"
        

def piece():
    global tour, gagnant, entier
    if tour%2 == 1 and gagnant == 0:
        joue = list(can1.find_withtag("full")) # Liste toutes les cases ayant déjà été choisi
        entier = list(set(entier)-set(joue))   # Liste les cases libres
        a = random.randint(0,len(entier)-1)    
        a = entier[a]

        if (a<2):
            can1.create_oval(10,110,40,140, fill='red')
        elif (a<3):
            can1.create_oval(60,110,90,140, fill='red')
        elif (a<4):
            can1.create_oval(110,110,140,140, fill='red')
        elif (a<5):
            can1.create_oval(10,60,40,90, fill='red')
        elif (a<6):
            can1.create_oval(60,60,90,90, fill='red')
        elif (a<7):
            can1.create_oval(110,60,140,90, fill='red')
        elif (a<8):
            can1.create_oval(10,10,40,40, fill='red')
        elif (a<9):
            can1.create_oval(60,10,90,40, fill='red')
        elif (a<10):
            can1.create_oval(110,10,140,40, fill='red')

        can1.addtag_withtag("red",a)
        can1.addtag_withtag("full",a)
        print(tour,": Le joueur place un pion rouge en",a)    
        if tour > 4:
            check_winner()
        tour=tour+1
    
    else:
        "Pas votre tour de jouer"

def check_winner():
    global gagnant, tour
    for i in range (1,3):
        if i == 1:
            items = can1.find_withtag("black")
            if (set([1,2,3]).issubset(items)) or (set([4,5,6]).issubset(items)) or (set([7,8,9]).issubset(items)) or (set([1,4,7]).issubset(items)) or (set([2,5,8]).issubset(items)) or (set([3,6,9]).issubset(items)) or (set([1,5,9]).issubset(items)) or (set([3,5,7]).issubset(items)):
                print("Les noirs gagnent.")
                gagnant = 1
        
        elif i == 2:
            items = can1.find_withtag("red")
            if (set([1,2,3]).issubset(items)) or (set([4,5,6]).issubset(items)) or (set([7,8,9]).issubset(items)) or (set([1,4,7]).issubset(items)) or (set([2,5,8]).issubset(items)) or (set([3,6,9]).issubset(items)) or (set([1,5,9]).issubset(items)) or (set([3,5,7]).issubset(items)):
                print("Les rouges gagnent.")
                gagnant = 2

    if gagnant == 0:
        if tour == 9:
            print("Match nul")
            gagnant = 3
            
        else:
            "La partie continue"


def getValue():
    global gagnant
    return gagnant
    fen1.destroy()



#========== Programme principal =============
def appel(n, r):
    global can1, entier, tour, gagnant, fen1, gagnant
    # Les variables suivantes seront utilisées de manière globale :
    tour = 1              # Compteur de tour
    gagnant = 0           # Gagnant ou pas (Utiliser un booléen ?) 0 : Non / 1 : Oui
    # Création du widget principal ("parent") :
    fen1 = Tk()
    fen1.title("Morpion")

    # Création des widgets "enfants" :
    can1 = Canvas(fen1, bg='dark grey', height=150, width=150)
    can1.pack(side=LEFT, padx=5, pady=5)

    bou1 = Button(fen1, text='Simulation', width=8, command=simulation)
    bou1.pack()

    grille()
    # Liste les cases de la grille
    entier = list(can1.find_all())
    recuperation(n, r)
    simulation()
    return gagnant
    # Démarrage du réceptionnaire d'évènements (boucle principale) :
    fen1.mainloop()



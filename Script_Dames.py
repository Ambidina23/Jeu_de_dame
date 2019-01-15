import Dames

total = 0

for i in range (1, 11):
    gagnant = Dames.UCTPlayGame(True)
    print("Le gagnant de la partie",i,"est",gagnant,"\n")
    total += gagnant

print("Résultat final =",total/i)
print("L'ordinateur a gagné",(total/i)*100,"% des",i,"parties.")

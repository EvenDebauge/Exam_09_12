from colorama import init
init()
from colorama import Fore,Back,Style
import random

def bibliotheque_mot (liste):
    bibliotheque_mot=[wapiti,webcam,totoro,atouts,manger,orange,castor,bureau,phyton,chaton]
    choix_mot= random.randint(0.9)
    mot_choisis=bibliotheque_mot[choix_mot]
    tour=1
    

def mot_joueur (mot_aleatoire):
    print(STYLE.RESET_ALL)
    mot_joueur= input("Entrez un mot de six lettres:")
    if mot_choisis[i] == mot_joueur[i]:
        print(Back.RED +mot_joueur[i], end="")
    else:
        print(Back.BLUE + mot_joueur[i], end="")
    for i in range(0,7):
        return mot_joueur







    
def rules (regles):
    print("Le jeu choisira un mot aléatoire parmis une liste de 10 mots")
    print("Si une lettre est bien placée par rapport au mot à trouver, elle sera rouge.")
    print("Si une lettre est mal placée par rapport au mot à trouver, elle sera jaune.")
    print("Si une lettre ne se trouve pas dans le mot à trouver, elle sera bleue.")
    print("Le mot à trouver est un mot de six lettres")
    print("_ _ _ _ _ _")

def test_victoire (test):
    if mot_choisis == mot_joueur :
        victoire =True
        print("Vous avez trouvés!")
    else: 
        victoire= False
        print("Il vous reste",tentatives,".")
        tentatives=tentatives-1
    return victoire

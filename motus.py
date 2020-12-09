from colorama import init
init()
from colorama import Fore,Back,Style
import random


def rules():
    print("Le jeu choisira un mot aléatoire parmis une liste de 10 mots")
    print("Si une lettre est bien placée par rapport au mot à trouver, elle sera rouge.")
    print("Si une lettre est mal placée par rapport au mot à trouver, elle sera jaune.")
    print("Si une lettre ne se trouve pas dans le mot à trouver, elle sera bleue.")
    print("Le mot à trouver est un mot de six lettres")
    print("_ _ _ _ _ _")
    
    
def tourJoueur (motAleatoire):
    print(Style.RESET_ALL)
    motJoueur= input("Entrez un mot de six lettres: ")
    for i in range (0,6):
        if motChoisis[i] == motJoueur[i]:
            print(Back.RED +motJoueur[i], end="")
        else:
            print(Back.BLUE + motJoueur[i], end="")
            print(Style.RESET_ALL)
    return motJoueur

def test_victoire (test):
    if motChoisis == motJoueur :
        victoire =True
        print("   Vous avez trouvés!")
    else: 
        victoire= False
        print("  Il vous reste",tentatives_restantes,".")
    return victoire
    
def test_defaite (test):
    if tentatives == 9:
        defaite=True
        print("Vous n'avez plus de tentatives, vous avez échoués.")
    else:
        defaite=False
        
bibliotheque_mot=["wapiti","webcam","totoro","atouts","manger","orange","castor","bureau","phyton","chaton"]
choix_mot= random.randint(0,9)
motChoisis=bibliotheque_mot[choix_mot]
tentatives=1
tentatives_restantes=7
victoire=False
defaite=False
rules()
while tentatives<9 and victoire != True:
    print(Style.RESET_ALL)
    print("tentative n°",tentatives,".")
    motJoueur=tourJoueur(motChoisis)
    victoire=test_victoire(motJoueur)
    defaite=test_defaite(motJoueur)
    tentatives=tentatives+1
    tentatives_restantes=tentatives_restantes-1


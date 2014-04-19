from modele import *
from vue import *

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v = Vue(self)
        
        #POUR TEST SEULEMENT (ATTENTION CODE LAID :D !)
        self.j = Jeu(self.m)
        i = 1
        for etoile in self.j.listeEtoiles:
            print(i, " ", etoile.posX, " ", etoile.posY, " ", etoile.typeEtoile)
            i+=1
        etoileProche = self.j.gubru.calculerEtoilePlusProche(self.j.gubru.etoileMere)
        print("Etoile proche ",etoileProche.posX, " ", etoileProche.posY, " ", etoileProche.typeEtoile)
        
#----Main----

if __name__ == '__main__':
    c = Controleur()
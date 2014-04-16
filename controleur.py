from modele import *
from vue import *

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v = Vue(self)
        self.j = Jeu(self.m)#POUR TEST SEULEMENT
        print(self.j.listeEtoiles[0].posX)
#----Main----

if __name__ == '__main__':
    c = Controleur()
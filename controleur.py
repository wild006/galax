#Francois Genest
#Julien Metivier
#Mathias Perreault-Guimond

from modele import *
from vue import *
import math

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v = Vue(self)
        self.v.root.mainloop()
    
    def commencerPartie(self):
        self.m.commencerJeu()
        
    def getListeEtoile(self):
        return self.m.j.listeEtoiles
    
    def getFlottesHumaines(self):
        return self.m.j.humain.flottes
    
    def getFlottesGubru(self):
        return self.m.j.gubru.flottes
    
    def getFlottesCzin(self):
        return self.m.j.czin.flottes
    
    def deplacementHumain(self,etoileDepart,etoileChoisi,nombreVaisseau):#Pour le deplacement des flottes dans la vue
        return self.m.j.humain.deplacementFlotte(etoileDepart, etoileChoisi, nombreVaisseau)
    
    def getGrandeurJeuX(self):
        return self.m.grandeurJeuX
    
    def getGrandeurJeuY(self):
        return self.m.grandeurJeuY
    
    def getDistance(self, etoileDepart, etoileArrivee):
       flotteTemp = Flotte(etoileDepart, etoileArrivee, 0)
       return math.ceil(flotteTemp.nbAnnee)
    
    def getInfoEtoile(self,x,y):
        etoileRechercher = None
        for etoile in self.m.j.listeEtoiles:
            if x == etoile.posX and y == etoile.posY:
                etoileRechercher = etoile
                break
        if etoileRechercher == None:
            return None   
        return self.m.j.infoEtoile(etoileRechercher)
    
    def getEtoile(self,x,y):
        etoileRechercher = None
        for etoile in self.m.j.listeEtoiles:
            if x == etoile.posX and y == etoile.posY:
                etoileRechercher = etoile
                break
        if etoileRechercher == None:
            return None   
        return etoileRechercher
    
    def changementTour(self):
        self.m.j.changementDeTour()
    
    def changerDifficulteFacile(self):
        self.m.difficulte = 1
    
    def changerDifficulteInter(self):
        self.m.difficulte = 2
    
    def changerDifficulteDifficile(self):
        self.m.difficulte = 3
    
    def getDifficulte(self):
        return self.m.difficulte
        
    def finPartie(self, humainGagnant):
        self.v.finPartie(humainGagnant)
    
    def getTemps(self):
        return int(self.m.j.tempsCourant)
            
#----Main----

if __name__ == '__main__':
    c = Controleur()
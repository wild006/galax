#Francois Genest
#Julien Metivier
#Mathias Perreault-Guimond

from modele import *
from vue import *

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v = Vue(self)
        self.v.root.mainloop()
    
    def commencerPartie(self):
        self.m.commencerJeu()
        
    def getListeEtoile(self):
        return self.m.j.listeEtoiles
    
    def deplacementHumain(self,etoileDepart,etoileChoisi,nombreVaisseau):#Pour le deplacement des flottes dans la vue
        return self.m.j.humain.deplacementFlotte(etoileDepart, etoileChoisi, nombreVaisseau)
    
    def getGrandeurJeuX(self):
        return self.m.grandeurJeuX
    
    def getGrandeurJeuY(self):
        return self.m.grandeurJeuY
    
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
        print("Temps", self.m.j.tempsCourant)
        i = 1
        for etoile in self.m.j.listeEtoiles:
            if etoile.typeEtoile == 1:
                print("Humain  ", "nbVaisseaux:", etoile.nombreVaisseau)
            elif etoile.typeEtoile == 2:
                print("Gubru  " ,"Position: ", "[", etoile.posX, ",", etoile.posY, "]","nbVaisseaux:", etoile.nombreVaisseau)
            elif etoile.typeEtoile == 3:
                print("Czin  " ,"Position: ", "[", etoile.posX, ",", etoile.posY, "]","nbVaisseaux:", etoile.nombreVaisseau)
            elif etoile.typeEtoile == 4:
                print("ind", etoile.nombreVaisseau)
        for flotte in self.m.j.czin.flottes:
            print("Czin ", flotte.positionInitialeX, " ",flotte.positionInitialeY, " ",flotte.etoileArrivee.posX, " ", flotte.etoileArrivee.posY, " annee", flotte.nbAnnee, "nbVaisseaux:", flotte.nombreVaisseau)
            print("Czin ", " annee", flotte.nbAnnee, "nbVaisseaux:", flotte.nombreVaisseau)
        for flotte in self.m.j.gubru.flottes:
            print("Gubru ", " annee:", flotte.nbAnnee, "Position: ", "[", flotte.etoileArrivee.posX, ",", flotte.etoileArrivee.posY, "]","nbVaisseaux:", flotte.nombreVaisseau)
    
    def finPartie(self, humainGagnant):
        self.v.finPartie(humainGagnant)
    
    def getTemps(self):
        return int(self.m.j.tempsCourant)
            
#----Main----

if __name__ == '__main__':
    c = Controleur()
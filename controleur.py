from modele import *
from vue import *

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v = Vue(self)
        self.v.root.mainloop()
    
    def commencerPartie(self):
        #POUR TEST SEULEMENT (ATTENTION CODE LAID :D !)
        self.j = Jeu(self.m)
        
        #for etoile in self.j.listeEtoiles:
         #   if etoile.typeEtoile == TypeEtoile.mereCzin:
          #      etoile.typeEtoile = TypeEtoile.gubru
        
        self.j.czin.calculerGrappes()
        i = 1
        for etoile in self.j.listeEtoiles:
            print(i, " ", etoile.posX, " ", etoile.posY, " ", etoile.typeEtoile, " ", etoile.valeurGrappe, " ", etoile.nombreVaisseau)
            i+=1
        etoileProche = self.j.gubru.calculerEtoilePlusProche(self.j.gubru.etoileMere)
        print("Etoile proche ",etoileProche.posX, " ", etoileProche.posY, " ", etoileProche.typeEtoile)
        print(self.j.gubru.calculerForceAttaque())
        #self.j.gubru.creationFlottes()
        #for flotte in self.j.gubru.flottes:
        #    print(flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau)
        #Mettre une etoile a Gubru pour test
        print(len(self.j.gubru.flottes))
        for i in range(10):
          #  self.j.gubru.choixDeplacementFlottes()
            for flotte in self.j.gubru.flottes:
                print("temps ", self.j.tempsCourant, " " , flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau, flotte.nbAnnee)
            self.j.changementDeTour()
        
        print(len(self.j.gubru.flottes))
        print("FIN")
        for flotte in self.j.gubru.flottes:
            print("FIN !!! temps ", self.j.tempsCourant, " " , flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau, flotte.nbAnnee)

    def getListeEtoile(self):
        return self.j.listeEtoiles
            
#----Main----

if __name__ == '__main__':
    c = Controleur()
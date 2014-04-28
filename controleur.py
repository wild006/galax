from modele import *
from vue import *

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v = Vue(self)
        self.v.root.mainloop()
    
    def commencerPartie(self):
        #POUR TEST SEULEMENT (ATTENTION CODE LAID :D !)
        self.m.commencerJeu()
        
        #for etoile in self.j.listeEtoiles:
         #   if etoile.typeEtoile == TypeEtoile.mereCzin:
          #      etoile.typeEtoile = TypeEtoile.gubru
        
       # self.j.czin.calculerGrappes()
      #  self.j.czin.essaimerGrappes()
       # i = 1
      #  for etoile in self.j.listeEtoiles:
       #     print(i, " ", etoile.posX, " ", etoile.posY, " ", etoile.typeEtoile, " ", etoile.valeurGrappe, " ", etoile.nombreVaisseau)
       #     i+=1
       # etoileProche = self.j.gubru.calculerEtoilePlusProche(self.j.gubru.etoileMere)
        #print("Etoile proche ",etoileProche.posX, " ", etoileProche.posY, " ", etoileProche.typeEtoile)
       # print(self.j.gubru.calculerForceAttaque())
        #self.j.gubru.creationFlottes()
        #for flotte in self.j.gubru.flottes:
        #    print(flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau)
        #Mettre une etoile a Gubru pour test
       # print(len(self.j.gubru.flottes))
        #for i in range(1):
         #   self.j.gubru.choixDeplacementFlottes()
         #   self.j.changementDeTour()
         #   for flotte in self.j.gubru.flottes:
          #      print("temps ", self.j.tempsCourant, " " , flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau, flotte.nbAnnee)
        
        #print(len(self.j.gubru.flottes))
        #print("FIN")
        #for flotte in self.j.gubru.flottes:
         #   print("FIN !!! temps ", self.j.tempsCourant, " " , flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau, flotte.nbAnnee)

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
            #print("etoileVAL ", etoile.posX, " ", etoile.posY, " ", etoile.valeurGrappe)
            if etoile.typeEtoile == 1:
                print("Humain  ", "nbVaisseaux:", etoile.nombreVaisseau)
            elif etoile.typeEtoile == 2:
                print("Gubru  " ,"Position: ", "[", etoile.posX, ",", etoile.posY, "]","nbVaisseaux:", etoile.nombreVaisseau)
            elif etoile.typeEtoile == 3:
                print("Czin  " ,"Position: ", "[", etoile.posX, ",", etoile.posY, "]","nbVaisseaux:", etoile.nombreVaisseau)
            elif etoile.typeEtoile == 4:
                print("ind", etoile.nombreVaisseau)
          #  print(i, " ", etoile.posX, " ", etoile.posY, " ", etoile.typeEtoile, " ", etoile.valeurGrappe, " ", etoile.nombreVaisseau)
           # i+=1
        for flotte in self.m.j.czin.flottes:
             print("Czin ", flotte.positionInitialeX, " ",flotte.positionInitialeY, " ",flotte.etoileArrivee.posX, " ", flotte.etoileArrivee.posY, " annee", flotte.nbAnnee, "nbVaisseaux:", flotte.nombreVaisseau)
             print("Czin ", " annee", flotte.nbAnnee, "nbVaisseaux:", flotte.nombreVaisseau)
        for flotte in self.m.j.gubru.flottes:
            #print("Gubru ", flotte.positionInitialeX, " ",flotte.positionInitialeY, " ",flotte.etoileArrivee.posX, " ", flotte.etoileArrivee.posY, " annee:", flotte.nbAnnee, "nbVaisseaux:", flotte.nombreVaisseau)
             print("Gubru ", " annee:", flotte.nbAnnee, "Position: ", "[", flotte.etoileArrivee.posX, ",", flotte.etoileArrivee.posY, "]","nbVaisseaux:", flotte.nombreVaisseau)
 
    def getTemps(self):
        return int(self.m.j.tempsCourant)
            
#----Main----

if __name__ == '__main__':
    c = Controleur()
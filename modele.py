import random
from enum import Enum

class TypeEtoile(Enum):
   	mereHumain = 1
    mereGubru = 2
    mereCzin = 3
    indep = 4
    humain = 5
    gubru = 6
    czin = 7

class NiveauIntelligence(Enum):
    aucun = 1
    premier = 2
    deuxieme = 3
    troisieme = 4

class Race(Enum):
	humain = 1
	gubru = 2
	czin = 3

class Modele():
    def __init__(self, parent):
        self.parent = parent



    def infoEtoile(self, Etoile, Race):
    	if Race == Race.humain:
    		if Etoile.IntelligenceHumain == NiveauIntelligence.aucun :
    			return None
    		elif Etoile.IntelligenceHumain == NiveauIntelligence.premier :
    			return Etoile.nombreVaisseau
    		elif Etoile.IntelligenceHumain == NiveauIntelligence.deuxieme :
    			return (Etoile.nombreVaisseau, Etoile.nombreUsine)
    		elif Etoile.IntelligenceHumain == NiveauIntelligence.troisieme :
    			return Etoile
 
class Jeu():
    def __init__(self):
        pass

class Humain():
    pass

class Czin():
    def __init__(self):
        pass
    
    def calculerGrappes(self):
        pass

class Gubru():
    pass

class Etoile():
    def __init__(self, typeEtoileAttribue):
    	self.IntelligenceHumain = NiveauIntelligence.aucun
    	self.IntelligenceGubru = NiveauIntelligence.aucun
    	self.IntelligenceCzin = NiveauIntelligence.aucun
    	self.posX = None
    	self.posY = None
    	self.nombreUsine = None
    	self.nombreVaisseau = None
    	self.typeEtoile = typeEtoileAttribue
    	initialiserEtoile()

    def initialiserEtoile(self):
    	if self.typeEtoile == TypeEtoile.mereHumain or self.typeEtoile == TypeEtoile.mereCzin or self.typeEtoile == TypeEtoile.mereGubru :
    		self.nombreUsine = 10
    		self.quantiteVaisseau = 100
    		if self.typeEtoile == TypeEtoile.mereHumain:
    			self.IntelligenceHumain = NiveauIntelligence.troisieme
    		elif self.typeEtoile == TypeEtoile.mereCzin:
    			self.IntelligenceCzin = NiveauIntelligence.troisieme
    		elif self.typeEtoile == TypeEtoile.mereGubru:
    			self.IntelligenceGubru = NiveauIntelligence.troisieme
    	elif self.typeEtoile == TypeEtoile.gubru or self.typeEtoile == TypeEtoile.humain or self.typeEtoile == TypeEtoile.czin or self.typeEtoile == TypeEtoile.indep :
    		self.nombreUsine = random.randrange(6)

    def creerVaisseau(self):
    	for x in range(0,self.nombreUsine):
    		self.quantiteVaisseau += random.randrange(6)

    

class Flotte():
    pass

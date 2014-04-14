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

class Modele():
    def __init__(self, parent):
        self.parent = parent
 
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
    def __init__(self, typeEtoile):
    	self.niveauIntelligence = 0
    	self.nombreUsine = None
    	self.quantiteVaisseau = None
    	self.typeEtoile = typeEtoile
    	initialiserEtoile()

    def initialiserEtoile(self):
    	if self.typeEtoile == TypeEtoile.mereHumain or self.typeEtoile == TypeEtoile.mereCzin or self.typeEtoile == TypeEtoile.mereGubru :
    		self.nombreUsine = 10
    		self.quantiteVaisseau = 100
    		self.niveauIntelligence = NiveauIntelligence.troisieme
    	elif self.typeEtoile == TypeEtoile.gubru or self.typeEtoile == TypeEtoile.humain or self.typeEtoile == TypeEtoile.czin or self.typeEtoile == TypeEtoile.indep :
    		self.nombreUsine = random.randrange(6)

    def creerVaisseau(self):
    	for x in range(0,self.nombreUsine):
    		self.quantiteVaisseau += random.randrange(6)

    

class Flotte():
    pass

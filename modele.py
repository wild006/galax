import random

class TypeEtoile():
	mereHumain = 1
	mereGubru = 2
	mereCzin = 3
	indep = 4
	humain = 5
	gubru = 6
	czin = 7

class NiveauIntelligence():
	aucun = 1
	premier = 2
	deuxieme = 3
	troisieme = 4

class Race():
	humain = 1
	gubru = 2
	czin = 3
    
class ModeCzin():
    rassemblementForces = 1
    etablirBase = 2
    conquerirGrappe = 3

class Modele():
	def __init__(self, parent):
		self.parent = parent
		self.nbEtoiles = 40
 
class Jeu():
	def __init__(self, parent):
		self.czin = Czin(self)
		self.gubru = Gubru(self)
		self.parent = parent
		self.listeEtoiles = [] #Liste de toutes les etoiles du jeu

	def initialiserToutesEtoiles(self, Modele):
		pass
	
	def infoEtoile(self, etoileChoisi):    # MODIFIER PAR JULIEN POUR CREER UNE ETOILE AVEC LES INFORMATIONS NECESSAIRES
		if etoileChoisi.IntelligenceHumain == NiveauIntelligence.aucun :
			return Etoile(TypeEtoile.indep)
		elif etoileChoisi.IntelligenceHumain == NiveauIntelligence.premier :
			nouvelleEtoile = Etoile(etoileChoisi.typeEtoile)
			nouvelleEtoile.nombreVaisseau = etoileChoisi.nombreVaisseau
			return nouvelleEtoile
		elif etoileChoisi.IntelligenceHumain == NiveauIntelligence.deuxieme :
			nouvelleEtoile = Etoile(etoileChoisi.typeEtoile)
			nouvelleEtoile.nombreVaisseau = etoileChoisi.nombreVaisseau
			nouvelleEtoile.nombreUsine = etoileChoisi.nombreUsine
			return nouvelleEtoile
		elif etoileChoisi.IntelligenceHumain == NiveauIntelligence.troisieme :
			return etoileChoisi

#Besoin dune variable pour le temps qui sincremente
class Humain():
	def __init__(self,parent):
		self.estHumain#besoin de verification pour determiner si humain ou non
		self.enVoyage#selon le choix du joueur a verifier
		
	def deplacementFlotte(self):
		for x in self.parent.listeEtoiles:
			if Etoile.IntelligenceHumain==NiveauIntelligence.troisieme:
				if self.estHumain:
					Flotte.calculerTempsVoyage(self)
					Flotte.vaisseauDefenseur=Flotte.vaisseauDefenseur-self.enVoyage
					
		
	def choixDeplacementFlotte(self):
		pass

class Czin():
    def __init__(self, parent, etoileMere):
        self.parent = parent #De type Jeu
        self.listeFlottes = [] #Toutes les flottes des Czin
        self.base = etoileMere
        #self.etoileMere = etoileMere
        self.distanceGrappe = 4
        self.nbVaisseauxParAttaque = 4
        self.forceAttaqueBasique = 20
        self.distanceRassemblement = 6 #en annees
        self.mode = ModeCzin.rassemblementForces #Mode de depart
        
    def calculerGrappes(self):
        for etoile1 in self.parent.listeEtoiles:
            for etoile2 in self.parent.listeEtoiles:
                distance = ((etoile1.posX - etoile2.posX)**2 + (etoile1.posY - etoile2.posY)**2)**0.5
                if distance <= self.distanceGrappe:
                    s = self.distanceGrappe - distance +1
                    etoile1.valeurGrappe *= s
    
    def calculerForceAttaque(self):
        return self.parent.tempsCourant * 
    def calculerMode(self):
        #rassemblementForces
        #if self.mode = ModeCzin.rassemblementForces and 
   
class Gubru():
	def __init__(self, parent, etoileMere):
		self.parent = parent #De type Jeu
		self.forceAttaqueBasique = 10
		self.nbVaisseauxParAttaque = 5

class Etoile():
	def __init__(self, typeEtoileAttribue):
		self.IntelligenceHumain = NiveauIntelligence.aucun
		self.posX = None
		self.posY = None
		self.valeurGrappe = 0 #Pour la strategie des Czin
		self.nombreUsine = None
		self.nombreVaisseau = None
		self.typeEtoile = typeEtoileAttribue

	def initialiserEtoile(self):
		if self.typeEtoile == TypeEtoile.mereHumain or self.typeEtoile == TypeEtoile.mereCzin or self.typeEtoile == TypeEtoile.mereGubru :
			self.nombreUsine = 10
			self.quantiteVaisseau = 100
			if self.typeEtoile == TypeEtoile.mereHumain:
				self.IntelligenceHumain = NiveauIntelligence.troisieme
		elif self.typeEtoile == TypeEtoile.gubru or self.typeEtoile == TypeEtoile.humain or self.typeEtoile == TypeEtoile.czin or self.typeEtoile == TypeEtoile.indep :
			self.nombreUsine = random.randrange(6)

	def initialiserPosition(self):
		self.posX = random.randrange(40) #le 40 est une fausse donner, doit etre changer
		self.posY = random.randrange(40) #meme chose ici

	def creerVaisseau(self):
		for x in range(0,self.nombreUsine):
			self.quantiteVaisseau += random.randrange(6)

	

class Flotte():
	def __init__(self,etoilePartante,etoileArrive,nombreVaisseau): #Verifier les valeurs de x et y
		self.positionInitialeX=etoilePartante.posX
		self.positionInitialeY=etoilePartante.posY
		self.positionFinalX=etoileArrive.posX
		self.positionFinalY=etoileArrive.posY
		self.distanceX=0
		self.distanceY=0
		self.nbAnnee=0
		self.nombreVaisseauDansFlotte=nombreVaisseau
		#self.flotteVaisseau=flotteVaisseau(self,x,y)?
		#self.vaisseauDefenseur=Etoile.nombreVaisseau
		self.vaisseauAttaquant=None
		self.probabiliteEliminer=None
		self.force=self.vaisseauDefenseur/self.vaisseauAttaquant


	def calculerTempsVoyage(self):
		self.distanceX=self.positionInitialeX-self.positionFinalX
		self.distanceY=self.positionInitialeY-self.positionFinalY

		if self.distanceX <=2 and self.distanceY <=2:
			self.nbAnnee = (self.distanceX / 2)+(self.distanceY / 2)
		else:
			self.nbAnnee = 1 + (((self.distanceX - 2) / 3) + ((self.distanceY - 2) / 3))


	def attaquer(self, etoile):
		if self.flotteVaisseau==(self.positionFinalX and self.positionFinalY):
			if etoile.nombreVaisseau>=1:
				if self.vaisseauAttaquant < self.vaisseauDefenseur:
					if self.force<5:
						self.probabiliteEliminer=self.force/10
					else:
						if self.force<20:
							self.probabiliteEliminer=(3*self.force+35)/100
						else:
							self.probabiliteEliminer=0.95
					while self.vaisseauAttaquant !=0 or self.vaisseauDefenseur !=0:
						for x in range(etoile.nombreVaisseau):
							self.probabiliteEliminer=random.randrange(10)
							if self.probabiliteEliminer>=7:
								self.vaisseauAttaquant-=1
						for y in range(self.vaisseauAttaquant):
							self.probabiliteEliminer=random.randrange(10)
							if self.probabiliteEliminer>=1:#Chiffre a verifier
								self.vaisseauDefenseur-=1
				



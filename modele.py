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
		self.grandeurJeuX = 20
		self.grandeurJeuY = 20
 
class Jeu():
	def __init__(self, parent):
		self.parent = parent
		self.tempsCourant = 0 #Temps qui va s'incrementer en cours de partie
		self.listeEtoiles = [] #Liste de toutes les etoiles du jeu
		self.initialiserToutesEtoiles(self.parent)
		#Pour TEST SEULEMENT
		self.czin = Czin(self,Etoile(TypeEtoile.mereCzin,self))
		self.gubru = Gubru(self,Etoile(TypeEtoile.mereGubru,self))

	def initialiserToutesEtoiles(self, Modele):
		#Creer les objets Czin et Gubru
		
		#Initialise les etoiles-meres de chaque race
		self.listeEtoiles.append(Etoile(TypeEtoile.mereHumain,self))
		self.listeEtoiles.append(Etoile(TypeEtoile.mereGubru,self))
		self.listeEtoiles.append(Etoile(TypeEtoile.mereCzin,self))
		while len(self.listeEtoiles) < self.parent.nbEtoiles:
			self.listeEtoiles.append(Etoile(TypeEtoile.indep,self))
	
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
	
	@staticmethod
	def calculerDistance(self, point1X, point1Y, point2X, point2Y):
		return ((point1X - point2X)**2 + (point1Y - point2Y)**2)**0.5

#Besoin dune variable pour le temps qui sincremente
class Humain():
	def __init__(self,parent):
		self.parent = parent
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
        self.flottes = [] #Toutes les flottes des Czin
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
                distance = Jeu.calculerDistance(self, etoile1.posX, etoile1.posY, etoile2.posX, etoile1.posY)
                if distance <= self.distanceGrappe:
                    s = self.distanceGrappe - distance +1
                    etoile1.valeurGrappe *= s
    
    def calculerBase(self):
    	for etoile in self.parent.listeEtoiles:
    		if etoile.valeurGrappe == 0:
    			etoile.valeurBase = 0
    		else:
    			distanceBase = Jeu.calculerDistance(self, self.base.posX, self.base.posY, etoile.posX, etoile.posY)
    			etoile.valeurBase = etoile.valeurGrappe-3*distanceBase
       	#A FAIRE: Update la base
       	
    def calculerForceAttaque(self):
        return self.parent.tempsCourant * self.nbVaisseauxParAttaque * self.forceAttaqueBasique
       
    def calculerMode(self):
        #rassemblementForces
        if self.mode == ModeCzin.rassemblementForces and self.base.nbVaisseaux >= (self.calculerForceAttaque*3):
        	self.mode = ModeCzin.etablirBase
        elif self.mode == ModeCzin.etablirBase: #A FAIRE: changer la condition selon deplacement
        	pass
        elif self.mode == ModeCzin.conquerirGrappe and len(self.flottes) == 0:
        	self.mode = ModeCzin.rassemblementForces
        #A FAIRE: les 2 autres modes

class Gubru():
	def __init__(self, parent, etoileMere):
		self.parent = parent #De type Jeu
		self.forceAttaqueBasique = 10
		self.nbVaisseauxParAttaque = 5
		self.etoileMere = etoileMere
		self.flottes = [] #Toutes les flottes des Czin
		
	def calculerForceAttaque(self):
		forceAttaque = parent.tempsCourant*self.nbVaisseauxParAttaque+self.forceAttaqueBasique
		if forceAttaque < self.forceAttaqueBasique*2:
			forceAttaque = self.forceAttaqueBasique*2
		return forceAttaque
	
	def calculerEtoilePlusProche(self, etoileDepart): #Retourne l'etoile la plus proche qui n'est pas au Gubru
		distanceMin = 0
		etoilePlusProche = etoileDepart
		for etoileArrivee in self.parent.listeEtoiles:
			if etoileArrivee.typeEtoile != TypeEtoile.gubru or etoileArrivee.typeEtoile != TypeEtoile.mereGubru:
				distance = Jeu.calculerDistance(self, etoileDepart.posX, etoileDepart.posY, etoileArrivee.posX, etoileArrivee.posY)
				if distanceMin > distance:
					distanceMin = distance
					etoilePlusProche = etoileArrivee
		return etoilePlusProche
	
	def creationFlottes(self): #Pour l'etoileMere
		while self.etoileMere.nombreVaisseau > self.calculerForceAttaque() + self.forceAttaqueBasique:
			self.flottes.append(etoileMere.creationFlotte(self.calculerEtoilePlusProche(self.etoileMere),self.calculerForceAttaque))

class Etoile():#Modifier par Julien
	def __init__(self, typeEtoileAttribue,parent):
		self.jeu = parent
		self.IntelligenceHumain = NiveauIntelligence.aucun
		self.posX = None
		self.posY = None
		self.valeurGrappe = 0 #Pour la strategie des Czin
		self.valeurBase = 0 #Pour la strategie des Czin
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
		xx = random.randrange(20)
		yy = random.randrange(20)
		tempPosEtoile = [[xx, yy]]
		while len(self.jeu.listeEtoiles) < self.jeu.parent.nbEtoiles:
			x = random.randrange(20)
			y = random.randrange(20)
			if [x,y] not in tempPosEtoile:
				if self.jeu.listeEtoiles:
					for etoile in self.jeu.listeEtoiles:
						if x != etoile.posX and y != etoile.posY:
							self.posX = x
							self.posY = y
							break
				else:
					self.posX = x
					self.posY = y

	def creerVaisseau(self):
		for x in range(0,self.nombreUsine):
			self.quantiteVaisseau += random.randrange(6)
	
	def creationFlotte(self, etoileArrivee, nbVaisseaux):
		pass #A FAIRE: retourne une flotte et enleve le nbvaisseaux a l'etoile
	
	

class Flotte():
	def __init__(self,etoileDepart,etoileArrivee,nombreVaisseau): 
		self.positionInitialeX=etoileDepart.posX
		self.positionInitialeY=etoileDepart.posY
		self.positionFinalX=etoileArrivee.posX
		self.positionFinalY=etoileArrivee.posY
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
		#A FAIRE : Calculer selon calculerDistance dans Jeu !
		
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
				



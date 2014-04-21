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
		self.espacementEtoileMereX = 5
		self.espacementEtoileMereY = 5
 
class Jeu():
	def __init__(self, parent):
		self.parent = parent
		self.tempsCourant = 0 #Temps qui va s'incrementer en cours de partie
		self.listeEtoiles = [] #Liste de toutes les etoiles du jeu
		self.initialiserToutesEtoiles(self.parent)

	def initialiserToutesEtoiles(self, Modele):
		#Initialise les etoiles-meres de chaque race et cree les objets Czin et Gubru
		self.listeEtoiles.append(Etoile(TypeEtoile.mereHumain,self))
		self.humain = Humain(self)
		#Gubru
		etoileMereGubru = Etoile(TypeEtoile.mereGubru,self)
		self.listeEtoiles.append(etoileMereGubru)
		self.gubru = Gubru(self,etoileMereGubru)
		#Czin
		etoileMereCzin = Etoile(TypeEtoile.mereCzin,self)
		self.listeEtoiles.append(etoileMereCzin)
		self.czin = Czin(self,etoileMereCzin)
		
		while len(self.listeEtoiles) < self.parent.nbEtoiles:
			self.listeEtoiles.append(Etoile(TypeEtoile.indep,self))
	
	def infoEtoile(self, etoileChoisi):    
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

	def changementDeTour(self):
		self.gubru.choixDeplacementFlottes()
		#self.czin.calculerMode()
		#self.czin.calculerBase()
		#self.czin.calculerGrappes()
		
		
		for x in range(10):
			self.tempsCourant += 0.1
			flotteASupp = []
			for flotte in self.humain.flottes:
				flotte.nbAnnee -= 0.1
				if flotte.nbAnnee <= 0:
					if flotte.etoileArrivee.nombreVaisseau>=1: #Combat
						if self.attaqueEnCours(flotte) != flotte:
							flotte.etoileArrivee.typeEtoile = TypeEtoile.humain
							flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
					else:
						flotte.etoileArrivee.typeEtoile = TypeEtoile.humain
						flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
						
					flotteASupp.append(flotte)
			self.supprimerFlottes(flotteASupp, self.humain.flottes)
			
			flotteASupp =[]
			for flotte in self.gubru.flottes:
				flotte.nbAnnee -= 0.1
				if flotte.nbAnnee <= 0:
					if flotte.etoileArrivee.nombreVaisseau>=1: #Combat
						if self.attaqueEnCours(flotte) != flotte:
							flotte.etoileArrivee.typeEtoile = TypeEtoile.gubru
							flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
					else:
						flotte.etoileArrivee.typeEtoile = TypeEtoile.gubru
						flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
			
					flotteASupp.append(flotte)
			self.supprimerFlottes(flotteASupp, self.gubru.flottes)
			
			flotteASupp =[]	
			for flotte in self.czin.flottes:
				flotte.nbAnnee -= 0.1
				if flotte.nbAnnee <= 0:
					if flotte.etoileArrivee.nombreVaisseau>=1: #Combat
						if self.attaqueEnCours(flotte) == flotte:
							self.czin.flottes.remove(flotte)
						else:
							flotte.etoileArrivee.typeEtoile = TypeEtoile.czin
							flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
					else:
						flotte.etoileArrivee.typeEtoile = TypeEtoile.czin
						flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
							
					flotteASupp.append(flotte)
			self.supprimerFlottes(flotteASupp, self.czin.flottes)
		print("fin changement tour")

	def attaqueEnCours(self, flotteAttaquante):
		flotteDefense = Flotte(flotteAttaquante.etoileArrivee,flotteAttaquante.etoileArrivee, flotteAttaquante.etoileArrivee.nombreVaisseau) #Flotte temporaire pour combat
		
		while flotteAttaquante.nombreVaisseau !=0 or flotteDefense.nombreVaisseau !=0:
			if flotteAttaquante.nombreVaisseau > flotteDefense.nombreVaisseau: #Attaque surprise
				r = flotteDefense.nombreVaisseau/flotteAttaquante.nombreVaisseau
				if r< 0.5:
					PremierprobabiliteEliminer = force/10
				elif r< 0.20:
					probabiliteAttaquePremier = (3* force+35)/100
				else:
					probabiliteAttaquePremier= 0.95
					
				prob = random.randrange(10)
				if probabiliteAttaquePremier*10 <= probabiliteAttaquePremier:
					flotteAttaquante.attaquer(flotteDefense,True)
					flotteDefense.attaquer(flotteAttaquante,False)
				else:
					flotteDefense.attaquer(flotteAttaquante,False)
					flotteAttaquante.attaquer(flotteDefense,True)
		
		#Retourne le perdant
		if flotteAttaquante.nombreVaisseau == 0:
			return flotteAttaquante
		else:
			return flotteDefense
		
	def supprimerFlottes(self, listeFlottesASupp, listeFlottes ):
		for flotte in listeFlottesASupp:
			print("REMOVE DEBUT" , flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau, flotte.nbAnnee)
			listeFlottes.remove(flotte)
			print("REMOVE FIN " , flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau, flotte.nbAnnee)
			
	@staticmethod
	def calculerDistance(point1X, point1Y, point2X, point2Y):
		return ((point1X - point2X)**2 + (point1Y - point2Y)**2)**0.5

#Besoin dune variable pour le temps qui sincremente
class Humain():
	def __init__(self,parent):
		self.parent = parent
		self.flottes = []
		
		#A FAIRE DANS LA VUE ???
		#self.estHumain#besoin de verification pour determiner si humain ou non
		#self.enVoyage#selon le choix du joueur a verifier
		
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
                distance = Jeu.calculerDistance(etoile1.posX, etoile1.posY, etoile2.posX, etoile1.posY)
                if distance <= self.distanceGrappe:
                	s = self.distanceGrappe - distance +1
                	etoile1.valeurGrappe += s*s
    
    def calculerBase(self):
    	for etoile in self.parent.listeEtoiles:
    		if etoile.valeurGrappe == 0:
    			etoile.valeurBase = 0
    		else:
    			distanceBase = Jeu.calculerDistance(self.base.posX, self.base.posY, etoile.posX, etoile.posY)
    			etoile.valeurBase = etoile.valeurGrappe-3*distanceBase
       	#A FAIRE: Update la base
       	
    def calculerForceAttaque(self):
        return self.parent.tempsCourant * self.nbVaisseauxParAttaque * self.forceAttaqueBasique
       
    def calculerMode(self):
        #rassemblementForces
        if self.mode == ModeCzin.rassemblementForces and self.base.nombreVaisseau >= (self.calculerForceAttaque()*3):
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
		self.flottes = [] #Toutes les flottes des Gubru
		
	def choixDeplacementFlottes(self):
		self.creationFlottesEtoileMere()
		for etoile in self.parent.listeEtoiles:
			if etoile.typeEtoile == TypeEtoile.gubru:
				print("nombre vaisseau" , etoile.nombreVaisseau)
				if etoile.nombreVaisseau > 25:
					self.flottes.append(etoile.creationFlotte(self.etoileMere, etoile.nombreVaisseau - 15))
	
	def calculerForceAttaque(self):
		forceAttaque = self.parent.tempsCourant*self.nbVaisseauxParAttaque+self.forceAttaqueBasique
		if forceAttaque < self.forceAttaqueBasique*2:
			forceAttaque = self.forceAttaqueBasique*2
		return forceAttaque
	
	def calculerEtoilePlusProche(self, etoileDepart): #Retourne l'etoile la plus proche qui n'est pas au Gubru
		distanceMin = Jeu.calculerDistance(0,0,self.parent.parent.grandeurJeuX+1, self.parent.parent.grandeurJeuY+1)
		etoilePlusProche = etoileDepart
		for etoileArrivee in self.parent.listeEtoiles:
			if etoileArrivee.typeEtoile != TypeEtoile.gubru and etoileArrivee.typeEtoile != TypeEtoile.mereGubru:
				distance = Jeu.calculerDistance(etoileDepart.posX, etoileDepart.posY, etoileArrivee.posX, etoileArrivee.posY)
				if distanceMin > distance:
					distanceMin = distance
					etoilePlusProche = etoileArrivee
		return etoilePlusProche
	
	def creationFlottesEtoileMere(self): #Pour l'etoile Mere/ Utiliser dans la fonction de deplacement des flottes
		while self.etoileMere.nombreVaisseau > self.calculerForceAttaque() + self.forceAttaqueBasique:
			self.flottes.append(self.etoileMere.creationFlotte(self.calculerEtoilePlusProche(self.etoileMere),self.calculerForceAttaque()))

class Etoile():
	def __init__(self, typeEtoileAttribue,parent):
		self.jeu = parent
		self.IntelligenceHumain = NiveauIntelligence.aucun
		self.posX = None
		self.posY = None
		self.valeurGrappe = 0 #Pour la strategie des Czin
		self.valeurBase = 0 #Pour la strategie des Czin
		self.nombreUsine = None
		self.nombreVaisseau = 0
		self.typeEtoile = typeEtoileAttribue
		self.initialiserEtoile()
		self.initialiserPosition()

	def initialiserEtoile(self):
		if self.typeEtoile == TypeEtoile.mereHumain or self.typeEtoile == TypeEtoile.mereCzin or self.typeEtoile == TypeEtoile.mereGubru :
			self.nombreUsine = 10
			self.nombreVaisseau = 100
			if self.typeEtoile == TypeEtoile.mereHumain:
				self.IntelligenceHumain = NiveauIntelligence.troisieme
		elif self.typeEtoile == TypeEtoile.gubru or self.typeEtoile == TypeEtoile.humain or self.typeEtoile == TypeEtoile.czin or self.typeEtoile == TypeEtoile.indep :
			self.nombreUsine = random.randrange(6)

	def initialiserPosition(self):#A FAIRE: Peut-etre ajouter que les etoiles meres sont loin l'une de l'autre
		valide = False
		while not valide:
			self.posX = random.randrange(self.jeu.parent.grandeurJeuX)
			self.posY = random.randrange(self.jeu.parent.grandeurJeuY)
			if self.jeu.listeEtoiles:
				for etoile in self.jeu.listeEtoiles:
					if etoile.typeEtoile == TypeEtoile.mereHumain or etoile.typeEtoile == TypeEtoile.mereCzin or etoile.typeEtoile == TypeEtoile.mereGubru :
						if self.typeEtoile == TypeEtoile.mereHumain or self.typeEtoile == TypeEtoile.mereCzin or self.typeEtoile == TypeEtoile.mereGubru :
							if abs(etoile.posX - self.posX) <= self.jeu.parent.espacementEtoileMereX:  
								if abs(etoile.posY - self.posY) <= self.jeu.parent.espacementEtoileMereY:
									valide = False
									break
					if self.posX == etoile.posX and self.posY == etoile.posY:
						valide = False
						break
					else:
						valide = True
			else:
				valide = True #S'il y a aucune etoile dans la liste

	def creerVaisseau(self):
		for x in range(0,self.nombreUsine):
			self.quantiteVaisseau += random.randrange(6)
	
	def creationFlotte(self, etoileArrivee, nbVaisseau):
		self.nombreVaisseau -= nbVaisseau
		return Flotte(self, etoileArrivee, nbVaisseau)
		#A FAIRE: Voir si il y a assez de vaisseaux sur l'etoile... (controle)
	

class Flotte():
	def __init__(self,etoileDepart,etoileArrivee,nombreVaisseau): 
		self.positionInitialeX=etoileDepart.posX
		self.positionInitialeY=etoileDepart.posY
		self.positionFinalX=etoileArrivee.posX
		self.positionFinalY=etoileArrivee.posY
		self.etoileArrivee=etoileArrivee
		self.raceOrigine=etoileDepart.typeEtoile
		self.distanceX=0
		self.distanceY=0
		self.nbAnnee=0
		self.nombreVaisseau=nombreVaisseau
		#self.nombreVaisseauDefenseur=None
		self.calculerTempsVoyage()
		#self.force=self.nombreVaisseauDefenseur/self.nombreVaisseau
		#self.flotteVaisseau=flotteVaisseau(self,x,y)?

	def calculerTempsVoyage(self):
		distance = Jeu.calculerDistance(self.positionInitialeX, self.positionInitialeY, self.positionFinalX, self.positionFinalY)
		if distance <= 2:
			self.nbAnnee = distance/2
		else:
			self.nbAnnee = 1 + ((distance-2)/3)
		
	def attaquer(self, flotteEnnemi, attaquant):
		if attaquant == True: # attaquant
			prob = 0.3 #Chiffre a verifier
		else:
			prob = 0.7
			for vaisseau in range(self.nombreVaisseau):
				probabiliteEliminer =random.randrange(10)
				if probabiliteEliminer >= prob:
					flotteEnnemi.nombreVaisseau -=1		



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
		etoileMereHumain = Etoile(TypeEtoile.mereHumain,self)
		self.listeEtoiles.append(etoileMereHumain)
		self.humain = Humain(etoileMereHumain, self)
		#Czin
		etoileMereCzin = Etoile(TypeEtoile.mereCzin,self)
		self.listeEtoiles.append(etoileMereCzin)
		self.czin = Czin(self,etoileMereCzin)
		#Gubru
		etoileMereGubru = Etoile(TypeEtoile.mereGubru,self)
		self.listeEtoiles.append(etoileMereGubru)
		self.gubru = Gubru(self,etoileMereGubru)
		
		while len(self.listeEtoiles) < self.parent.nbEtoiles:
			self.listeEtoiles.append(Etoile(TypeEtoile.indep,self))
	
	def infoEtoile(self, etoileChoisi):	
		if etoileChoisi.IntelligenceHumain == NiveauIntelligence.aucun :
			return Etoile(TypeEtoile.indep, self)
		elif etoileChoisi.IntelligenceHumain == NiveauIntelligence.premier :
			nouvelleEtoile = Etoile(etoileChoisi.typeEtoile, self)
			nouvelleEtoile.nombreVaisseau = etoileChoisi.nombreVaisseau
			return nouvelleEtoile
		elif etoileChoisi.IntelligenceHumain == NiveauIntelligence.deuxieme :
			nouvelleEtoile = Etoile(etoileChoisi.typeEtoile, self)
			nouvelleEtoile.nombreVaisseau = etoileChoisi.nombreVaisseau
			nouvelleEtoile.nombreUsine = etoileChoisi.nombreUsine
			return nouvelleEtoile
		elif etoileChoisi.IntelligenceHumain == NiveauIntelligence.troisieme :
			return etoileChoisi

	def changementDeTour(self):
		print("gubru")
		self.gubru.choixDeplacementFlottes()
		print("Czin")
		self.czin.choixDeplacementFlottes()
		#self.czin.calculerMode()
		#self.czin.calculerBase()
		#self.czin.calculerGrappes()
		
		
		for x in range(10):
			#self.tempsCourant += 0.1
			flotteASupp = []
            #humain
			for flotte in self.humain.flottes:
				flotte.nbAnnee -= 0.1
				if flotte.nbAnnee <= 0:
					if flotte.etoileArrivee.nombreVaisseau>=1 and (flotte.etoileArrivee.typeEtoile != TypeEtoile.humain and flotte.etoileArrivee.typeEtoile != TypeEtoile.mereHumain): #Combat
						if self.attaqueEnCours(flotte) != flotte:
							if flotte.etoileArrivee.typeEtoile != TypeEtoile.mereHumain:
								flotte.etoileArrivee.typeEtoile = TypeEtoile.humain
							flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
					else:
						if flotte.etoileArrivee.typeEtoile != TypeEtoile.mereHumain:
							flotte.etoileArrivee.typeEtoile = TypeEtoile.humain
						flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
						
					flotteASupp.append(flotte)
			self.supprimerFlottes(flotteASupp, self.humain.flottes)
			
			#gubru
			flotteASupp =[]
			for flotte in self.gubru.flottes:
				flotte.nbAnnee -= 0.1
				if flotte.nbAnnee <= 0:
					if flotte.etoileArrivee.nombreVaisseau>=1 and (flotte.etoileArrivee.typeEtoile != TypeEtoile.gubru and flotte.etoileArrivee.typeEtoile != TypeEtoile.mereGubru): #Combat
						if self.attaqueEnCours(flotte) != flotte:
							if flotte.etoileArrivee.typeEtoile != TypeEtoile.mereGubru:
								flotte.etoileArrivee.typeEtoile = TypeEtoile.gubru
							flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
					else:
						if flotte.etoileArrivee.typeEtoile != TypeEtoile.mereGubru:
							flotte.etoileArrivee.typeEtoile = TypeEtoile.gubru
						flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
			
					flotteASupp.append(flotte)
			self.supprimerFlottes(flotteASupp, self.gubru.flottes)
			
			#czin
			flotteASupp =[]	
			for flotte in self.czin.flottes:
				flotte.nbAnnee -= 0.1
				if flotte.nbAnnee <= 0:
					print("Type etoile czin : ", flotte.etoileArrivee.typeEtoile)
					if flotte.etoileArrivee.nombreVaisseau>=1 and(flotte.etoileArrivee.typeEtoile != TypeEtoile.czin and flotte.etoileArrivee.typeEtoile != TypeEtoile.mereCzin): #Combat
						flottePerdante = self.attaqueEnCours(flotte)
						if flottePerdante == flotte:
							self.czin.flottes.remove(flotte)
						else:
							if flotte.etoileArrivee.typeEtoile != TypeEtoile.mereCzin:
								flotte.etoileArrivee.typeEtoile = TypeEtoile.czin
							flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
					else:
						if flotte.etoileArrivee.typeEtoile != TypeEtoile.mereCzin:
							flotte.etoileArrivee.typeEtoile = TypeEtoile.czin
						flotte.etoileArrivee.nombreVaisseau += flotte.nombreVaisseau
						print("AJOUTE ", flotte.nombreVaisseau , " a ", flotte.etoileArrivee.nombreVaisseau)
							
					flotteASupp.append(flotte)
			self.supprimerFlottes(flotteASupp, self.czin.flottes)
		print("fin changement tour")
		self.tempsCourant +=1
		#Savoir si c'est la fin de la partie
		self.mortHumaine = True
		for etoile in self.listeEtoiles:
			if etoile.typeEtoile == TypeEtoile.mereHumain or etoile.typeEtoile == TypeEtoile.humain:
				self.mortHumaine = False
				break
		for flotte in self.humain.flottes:
			if flotte.raceOrigine == Race.humain:
				self.mortHumaine = False
				break
		if self.mortHumaine == True:
			print("FIN DE LA PARTIE")
			#Partie terminer
		#manufactures
		for etoile in self.listeEtoiles:
			etoile.creerVaisseau()

	def attaqueEnCours(self, flotteAttaquante):
		flotteDefense = Flotte(flotteAttaquante.etoileArrivee,flotteAttaquante.etoileArrivee, flotteAttaquante.etoileArrivee.nombreVaisseau) #Flotte temporaire pour combat
		print("attaquant", flotteAttaquante.nombreVaisseau, "defense", flotteDefense.nombreVaisseau)
		while  flotteAttaquante.nombreVaisseau > 0 and flotteDefense.nombreVaisseau > 0:
			print("attaquant", flotteAttaquante.nombreVaisseau, "defense", flotteDefense.nombreVaisseau)
			if flotteAttaquante.nombreVaisseau > flotteDefense.nombreVaisseau: #Attaque surprise
				r = flotteDefense.nombreVaisseau/flotteAttaquante.nombreVaisseau
				if r< 0.5:
					probabiliteAttaquePremier = r/10
				elif r< 0.20:
					probabiliteAttaquePremier = (3* r+35)/100
				else:
					probabiliteAttaquePremier= 0.95
					
				prob = random.randrange(10)
				#print("prob de : ",prob)
				if probabiliteAttaquePremier*10 <= probabiliteAttaquePremier:
					flotteAttaquante.attaquer(flotteDefense,True)
					flotteDefense.attaquer(flotteAttaquante,False)
					#if flotteDefense.nombreVaisseau > 0:
						#flotteDefense.attaquer(flotteAttaquante,False)
				else:
					flotteDefense.attaquer(flotteAttaquante,False)
					flotteAttaquante.attaquer(flotteDefense,True)
					#if flotteAttaquante.nombreVaisseau > 0:
						#flotteAttaquante.attaquer(flotteDefense,True)
			else:
				flotteDefense.attaquer(flotteAttaquante,False)
				flotteAttaquante.attaquer(flotteDefense,True)
				#if flotteAttaquante.nombreVaisseau > 0:
				#	flotteAttaquante.attaquer(flotteDefense,True)
		
		#Retourne le perdant
		if flotteAttaquante.nombreVaisseau <= 0:
			return flotteAttaquante
		else:
			return flotteDefense
		
	def supprimerFlottes(self, listeFlottesASupp, listeFlottes ):
		for flotte in listeFlottesASupp:
			print("REMOVE DEBUT" , flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau, flotte.nbAnnee)
			try:
				listeFlottes.remove(flotte)
			except:
				print("Flotte deja supp...") #FLOTTE DEJA SUPPRIMER !
			print("REMOVE FIN " , flotte.positionInitialeX, " ", flotte.positionInitialeY, " Arrivee ", flotte.positionFinalX, " ", flotte.positionFinalY, " avec ", flotte.nombreVaisseau, flotte.nbAnnee)
			
	@staticmethod
	def calculerDistance(point1X, point1Y, point2X, point2Y):
		return ((point1X - point2X)**2 + (point1Y - point2Y)**2)**0.5

#Besoin dune variable pour le temps qui sincremente
class Humain():
	def __init__(self, etoileMere, parent):
		self.parent = parent
		self.etoileMere = etoileMere
		self.flottes = []
		
		#A FAIRE DANS LA VUE ???
		#self.estHumain#besoin de verification pour determiner si humain ou non
		#self.enVoyage#selon le choix du joueur a verifier
		
	def deplacementFlotte(self, etoileDepart, etoileChoisi, nombreVaisseau):
		self.flottes.append(Flotte(etoileDepart,etoileChoisi,nombreVaisseau))


class Czin():
	def __init__(self, parent, etoileMere):
		self.parent = parent #De type Jeu
		self.flottes = [] #Toutes les flottes des Czin
		self.base = etoileMere
		self.nouvelleBase = None
		self.etoileMere = etoileMere
		self.distanceGrappe = 4
		self.nbVaisseauxParAttaque = 4
		self.forceAttaqueBasique = 20
		self.distanceRassemblement = 6 #en annees
		self.nbVaisseauxLaisser = 3
		self.mode = ModeCzin.rassemblementForces #Mode de depart
		
	def choixDeplacementFlottes(self):
		if self.base.typeEtoile != TypeEtoile.czin:
			self.base = self.etoileMere
			self.mode = ModeCzin.rassemblementForces
		if self.etoileMere.typeEtoile != TypeEtoile.mereCzin:
			self.base.typeEtoile = TypeEtoile.mereCzin
			self.etoileMere = self.base
		self.calculerGrappes()
		if self.mode == ModeCzin.rassemblementForces:
			self.rassemblementBase()
		elif self.mode == ModeCzin.etablirBase:
	   		#if self.enDirection(self.nouvelleBase) == False:
	   		if self.parent.listeEtoiles[self.parent.listeEtoiles.index(self.nouvelleBase)].typeEtoile == TypeEtoile.czin: #Si on a gagne la base
	   			self.base = self.nouvelleBase
	   			self.essaimerGrappes()
	   			self.mode = ModeCzin.conquerirGrappe
	   		else:
	   			self.base = self.etoileMere
	   			self.mode = ModeCzin.rassemblementForces
		elif self.mode == ModeCzin.conquerirGrappe:
	   		if len(self.flottes) == 0:
	   			self.mode = ModeCzin.rassemblementForces
	
	def rassemblementBase(self):
		changementBase = True
		for etoile in self.parent.listeEtoiles:
			if etoile.typeEtoile == TypeEtoile.czin:
				if Jeu.calculerDistance(self.base.posX, self.base.posY, etoile.posX, etoile.posY) > 6:
					if etoile.nombreVaisseau > self.nbVaisseauxLaisser:
						self.flottes.append(etoile.creationFlotte(self.base, etoile.nombreVaisseau - self.nbVaisseauxLaisser))
						changementBase = False
		if changementBase == True:
			self.base = self.etoileMere
		if self.base.nombreVaisseau >= (self.calculerForceAttaque()*3):
			self.nouvelleBase = self.calculerBase()
			self.flottes.append(self.base.creationFlotte(self.nouvelleBase,self.base.nombreVaisseau)) #Faire base temp ???
			self.mode = ModeCzin.etablirBase
	
	def calculerGrappes(self):
		for etoile1 in self.parent.listeEtoiles:
			for etoile2 in self.parent.listeEtoiles:
				distance = Jeu.calculerDistance(etoile1.posX, etoile1.posY, etoile2.posX, etoile1.posY)
				if distance <= self.distanceGrappe:
					s = self.distanceGrappe - distance +1
					etoile1.valeurGrappe += s*s
	
	def essaimerGrappes(self):
		listeEtoileGrappe = [] #Toutes les etoiles de la grappe de la base
		for etoile in self.parent.listeEtoiles:
			if etoile.valeurGrappe == self.base.valeurGrappe and (etoile.typeEtoile != TypeEtoile.czin or etoile.typeEtoile != TypeEtoile.mereCzin):
				listeEtoileGrappe.append(etoile)
		print("LISTE ETOIEL", listeEtoileGrappe)
		listeEtoileGrappe = self.calculerDistanceEtoile(self.base, listeEtoileGrappe)
		forceAttaque = self.calculerForceAttaque()
		noEtoile = 0
		while self.base.nombreVaisseau >= forceAttaque:
			self.flottes.append(self.base.creationFlotte(listeEtoileGrappe[noEtoile],forceAttaque))
			noEtoile +=1
			if noEtoile > (len(listeEtoileGrappe)-1):
				noEtoile = 0
		
	def calculerDistanceEtoile(self, etoileDepart, listeEtoileArrivee):
		for etoile in listeEtoileArrivee:
			etoile.distanceAutreEtoile = Jeu.calculerDistance(etoileDepart.posX,etoileDepart.posY,etoile.posX,etoile.posY)
		return sorted(listeEtoileArrivee, key=lambda x: x.distanceAutreEtoile)
	
	def calculerBase(self):
		nouvelleBase = self.parent.listeEtoiles[0]
		for etoile in self.parent.listeEtoiles:
			if etoile.valeurGrappe == 0:
				etoile.valeurBase = 0
			else:
				distanceBase = Jeu.calculerDistance(self.base.posX, self.base.posY, etoile.posX, etoile.posY)
				etoile.valeurBase = (etoile.valeurGrappe-3)*distanceBase
			if etoile.valeurBase > nouvelleBase.valeurBase:
				nouvelleBase = etoile
		return nouvelleBase
	   	
	def calculerForceAttaque(self):
		return self.parent.tempsCourant * self.nbVaisseauxParAttaque * self.forceAttaqueBasique
		
	def enDirection(self, etoileArrivee):
		for flotte in self.flottes:
			if flotte.etoileArrivee == etoileArrivee:
				return True
		return False
	
class Gubru():
	def __init__(self, parent, etoileMere):
		self.parent = parent #De type Jeu
		self.forceAttaqueBasique = 10
		self.nbVaisseauxParAttaque = 5
		self.etoileMere = etoileMere
		self.flottes = [] #Toutes les flottes des Gubru
		
	def choixDeplacementFlottes(self):
		if self.etoileMere.typeEtoile != TypeEtoile.mereGubru:
			for etoile in self.parent.listeEtoiles:
				if etoile.typeEtoile == TypeEtoile.gubru:
					etoile.typeEtoile = TypeEtoile.mereGubru
					self.etoileMere = etoile
					break
		self.creationFlottesEtoileMere()
		for etoile in self.parent.listeEtoiles:
			if etoile.typeEtoile == TypeEtoile.gubru:
				print("nombre vaisseau" , etoile.nombreVaisseau)
				if etoile.nombreVaisseau > 25:
					self.flottes.append(etoile.creationFlotte(self.etoileMere, etoile.nombreVaisseau - 15))
	
	def calculerForceAttaque(self):
		forceAttaque = self.parent.tempsCourant*(self.nbVaisseauxParAttaque+self.forceAttaqueBasique)
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
		print("GUbRU", self.etoileMere.nombreVaisseau, " > ", self.calculerForceAttaque() + self.forceAttaqueBasique)
		forceAttaque = self.calculerForceAttaque()
		while self.etoileMere.nombreVaisseau > forceAttaque + self.forceAttaqueBasique:
			if forceAttaque > 0:
				self.flottes.append(self.etoileMere.creationFlotte(self.calculerEtoilePlusProche(self.etoileMere),forceAttaque))

class Etoile():
	def __init__(self, typeEtoileAttribue,parent):
		self.jeu = parent
		self.IntelligenceHumain = NiveauIntelligence.aucun
		self.posX = None
		self.posY = None
		self.valeurGrappe = 0 #Pour la strategie des Czin
		self.valeurBase = 0 #Pour la strategie des Czin
		self.distanceAutreEtoile = None #Pour pouvoir classer les etoiles avec leur distance
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
			self.nombreUsine = random.randrange(1,6)

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
			self.nombreVaisseau += random.randrange(6)
	
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
			prob = 5 #Chiffre a verifier
		else:
			prob = 7
		for vaisseau in range(int(self.nombreVaisseau)):
			probabiliteEliminer =random.randrange(10)
			if probabiliteEliminer >= prob:
				if flotteEnnemi.nombreVaisseau > 0:
					flotteEnnemi.nombreVaisseau -=1
				else:
					break

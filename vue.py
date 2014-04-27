from tkinter import *
import math
from PIL import Image, ImageTk 


class Vue():
	def __init__(self, parent):
		self.parent = parent
		self.root=Tk()
		self.initLobby()

	def initLobby(self):
		
		self.cadreLobby=Frame(self.root)

		self.background=Image.open("background.jpg")#Agrandir selon la fenetre
		self.background_image=ImageTk.PhotoImage(self.background)
		self.background_label = Label(self.cadreLobby, image=self.background_image)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		
		self.logoGalax = Image.open("logo.jpg") 
		self.photoGalax = ImageTk.PhotoImage(self.logoGalax)
		self.labelLogo = Label(self.cadreLobby,image=self.photoGalax)
		self.labelLogo.pack()
		#self.canevas=Canvas(self.cadreMain,width=800,height=800)
		#self.canevas.create_image(400,300,image=self.photoGalax)
		#self.canevas.pack()
		
		b1=Button(self.cadreLobby,text="Commencer partie",width=15,command=self.initPartie)
		b1.pack()
		b2=Button(self.cadreLobby,text="Options",width=15,command=self.initOption)
		b2.pack()
		b3=Button(self.cadreLobby,text="HighScore",width=15,command=self.initHighScore)
		b3.pack()
		b4=Button(self.cadreLobby,text="Quitter",width=15,command=self.initFermer)
		b4.pack()

		self.cadreLobby.pack()

		
	def initPartie(self):
		self.parent.commencerPartie()
		self.etoileDepart=None
		self.etoileArrivee=None
		self.cadrePartie=Frame(self.root)
		self.cadreJeu=Frame(self.cadrePartie)
		self.cadreFlotte=Frame(self.cadrePartie)
		self.cadreInfo=Frame(self.cadrePartie)
		self.cadreCommande=Frame(self.cadrePartie)
		self.cadreInfo=Frame(self.cadrePartie)
		self.cadreJeu.grid(column=0,row=0)
		self.cadreFlotte.grid(column=0,row=1)
		self.cadreInfo.grid(column=1,row=0,sticky=N)
		#self.cadreInfo.grid(column=2,row=0)#appelle des functions pour resultat 
		self.cadreCommande.grid(column=1,row=1,columnspan=2)
		
		self.canevas=Canvas(self.cadreJeu,width=800,height=800,bg="black")
		
		self.backgroundCanevas=Image.open("background.jpg")#Agrandir selon la fenetre
		self.background_image=ImageTk.PhotoImage(self.backgroundCanevas)
		self.canevas.create_image(0,0,image=self.background_image,anchor=NW)
		self.canevas.pack()
		
		
		self.sliderDeplacement = Scale(self.cadreFlotte,orient=HORIZONTAL,length=400,width=20,sliderlength=10,from_=0,to=0)
		self.sliderDeplacement.pack()
		
		
		
		self.logoGalax = Image.open("logo.jpg") 
		self.photoGalax = ImageTk.PhotoImage(self.logoGalax)
		self.labelLogo = Label(self.cadreInfo,image=self.photoGalax)
		self.labelLogo.grid(column=0,row=0,columnspan=2)
		
		labelInfo=Label(self.cadreInfo,text="Informations",relief=SOLID,width=15)
		labelInfo.grid(column=0,row=1,pady=16)
		labelHumain=Label(self.cadreInfo,text="Humain",relief=GROOVE,width=15)
		labelHumain.grid(column=0,row=2)
		labelGubru=Label(self.cadreInfo,text="Gubru",relief=GROOVE,width=15)
		labelGubru.grid(column=0,row=3)
		labelCzin=Label(self.cadreInfo,text="Czin",relief=GROOVE,width=15)
		labelCzin.grid(column=0,row=4)
		labelIndep=Label(self.cadreInfo,text="Ind\xE9pendant",relief=GROOVE,width=15)
		labelIndep.grid(column=0,row=5)
		
		labelEtoile=Label(self.cadreInfo,text="Etoiles",relief=SOLID,width=15)#e accent aigue majuscule
		labelEtoile.grid(column=0,row=6,pady=16)
		labelProprio=Label(self.cadreInfo,text="Propri\xE9taire",relief=GROOVE,width=15)
		labelProprio.grid(column=0,row=7)
		labelVaisseau=Label(self.cadreInfo,text="Nb Vaisseau(x)",relief=GROOVE,width=15)
		labelVaisseau.grid(column=0,row=8)
		labelManu=Label(self.cadreInfo,text="Nb Manufacture(s)",relief=GROOVE,width=15)
		labelManu.grid(column=0,row=9)
		
		labelDestination=Label(self.cadreInfo,text="Destination",relief=SOLID,width=15)
		labelDestination.grid(column=0,row=10,pady=16)
		labelProprio=Label(self.cadreInfo,text="Propri\xE9taire",relief=GROOVE,width=15)
		labelProprio.grid(column=0,row=11)
		labelVaisseau=Label(self.cadreInfo,text="Nb Vaisseau(x)",relief=GROOVE,width=15)
		labelVaisseau.grid(column=0,row=12)
		labelManu=Label(self.cadreInfo,text="Nb Manufacture(s)",relief=GROOVE,width=15)
		labelManu.grid(column=0,row=13)
		
		
		labelInfoResultat=Label(self.cadreInfo)
		labelInfoResultat.grid(column=1,row=1,pady=16)
		self.labelHumainResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
		self.labelHumainResultat.grid(column=1,row=2)
		self.labelGubruResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
		self.labelGubruResultat.grid(column=1,row=3)
		self.labelCzinResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
		self.labelCzinResultat.grid(column=1,row=4)
		self.labelIndepResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
		self.labelIndepResultat.grid(column=1,row=5)
		
		labelEtoileResultat=Label(self.cadreInfo)
		labelEtoileResultat.grid(column=1,row=6,pady=16)
		self.labelEtoileProprioResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
		self.labelEtoileProprioResultat.grid(column=1,row=7)
		self.labelEtoileVaisseauResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
		self.labelEtoileVaisseauResultat.grid(column=1,row=8)
		self.labelEtoileManuResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
		self.labelEtoileManuResultat.grid(column=1,row=9)
		
		labelDestinationResultat=Label(self.cadreInfo)
		labelDestinationResultat.grid(column=1,row=10,pady=16)
		self.labelDestinationProprioResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
		self.labelDestinationProprioResultat.grid(column=1,row=11)
		self.labelDestinationVaisseauResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
		self.labelDestinationVaisseauResultat.grid(column=1,row=12)
		self.labelDestinationManuResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
		self.labelDestinationManuResultat.grid(column=1,row=13)
		
		self.canevas.bind("<Button-1>", self.clickCanevas)
		self.labelTemps = Label(self.cadreCommande,text=self.parent.getTemps(),relief=GROOVE,width=15)
		self.labelTemps.pack()
		
		
		
		b1=Button(self.cadreFlotte,text="Faire D\xE9placement")
		b1.pack()
		
		b2=Button(self.cadreCommande,text="Prochain Tour",width=12, command= self.prochainTour)
		b2.pack()
		b3=Button(self.cadreCommande,text="Quitter",width=12,command=self.initFermer)
		b3.pack()
		
		
		
		#self.canevas.create_oval(0, 0, 100, 100)
		#print(self.parent.getListeEtoile())
		self.updateEtoile()
			#self.canevas.create_image(etoile.posX*(800/self.parent.getGrandeurJeuX())+10,etoile.posY*(800/self.parent.getGrandeurJeuY())+10,image=photo)
			#(etoile.posX*(800/self.parent.getGrandeurJeuX())+10, etoile.posY*(800/self.parent.getGrandeurJeuY())+10, etoile.posX*(800/self.parent.getGrandeurJeuX())+20, etoile.posY*(800/self.parent.getGrandeurJeuY()) +20)
			#A FAIRE : Afficher selon le x et y des etoiles dans liste etoile
			#A FAIRE: BIEN AFFICHER LES ETOILES
		
		self.cadreLobby.pack_forget()
		self.cadrePartie.pack()
	
	def prochainTour(self):
		self.parent.changementTour()	
		self.labelTemps.config(text=self.parent.getTemps())
		self.updateEtoile()
	
	def updateEtoile(self):
		try:
			self.canevas.delete("etoile")
		except:
			pass
		compteur = 0
		self.photo = []
		for etoile in self.parent.getListeEtoile():
			#print(self.canevas.winfo_width())
			#print(self.canevas.winfo_height())
			if etoile.typeEtoile == 2 or etoile.typeEtoile == 6:
				image = Image.open("etoile_gubru.jpg")
			elif etoile.typeEtoile == 1 or etoile.typeEtoile == 5:
				image = Image.open("etoile_humain.jpg")
			elif etoile.typeEtoile == 3 or etoile.typeEtoile == 7:
				image = Image.open("etoile_czin.jpg")
			elif etoile.typeEtoile == 4:
				image = Image.open("etoile_ind.jpg")
			self.photo.append(ImageTk.PhotoImage(image))
			self.canevas.create_image(etoile.posX*(800/self.parent.getGrandeurJeuX())+20,etoile.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[compteur], tags="etoile")
			compteur += 1   
	
	def clickCanevas(self,event):	#capturing click in a window
		id = self.canevas.find_withtag("current")
		etoile = None
		print(self.canevas.coords(id))
		try:
			x = math.floor((self.canevas.coords(id)[0]/(800/self.parent.getGrandeurJeuX())))
			y = math.floor((self.canevas.coords(id)[1]/(800/self.parent.getGrandeurJeuY())))
			etoile = self.parent.getInfoEtoile(x,y)
		except:
			pass
		if etoile==None :
			self.etoileDepart=None#detecte toujours a nul
			self.etoileArrivee=None
			self.labelEtoileProprioResultat.config(text="")
			self.labelEtoileVaisseauResultat.config(text="")
			self.labelEtoileManuResultat.config(text="")
			self.labelDestinationProprioResultat.config(text="")
			self.labelDestinationManuResultat.config(text="")
			self.labelDestinationVaisseauResultat.config(text="")
			#verifier si etoileDepart est = a none
		elif etoile.typeEtoile==1 or etoile.typeEtoile==5:
			if self.etoileDepart == None:#premier click
				self.etoileDepart=etoile
			else:#deuxieme click
				self.etoileArrivee = etoile
				
			self.sliderDeplacement.config(to=etoile.nombreVaisseau)
			self.labelEtoileProprioResultat.config(text= "Humain")
			self.labelEtoileVaisseauResultat.config(text=etoile.nombreVaisseau)
			self.labelEtoileManuResultat.config(text=etoile.nombreUsine)
			#if self.etoileArrivee==None:
			#	self.etoileDepart=None
			if self.etoileArrivee==self.etoileDepart:
				self.etoileArrivee=None
			elif self.etoileArrivee.typeEtoile==1 or self.etoileArrivee.typeEtoile==5:
				self.parent.Humain.deplacementFlotte(self.etoileDepart,self.etoileArrivee,self.sliderDeplacement.get())
				
				
		elif etoile.typeEtoile==2 or etoile.typeEtoile==6 :
			self.labelEtoileProprioResultat.config(text= "Gubru")
			if self.etoileDepart !=None:#verifier si on a clicker sur une etoile humaine en premier
				self.etoileArrivee=etoile
				self.parent.Humain.deplacementFlotte(self.etoileDepart,self.etoileArrivee,self.sliderDeplacement.get())
				self.labelDestinationProprioResultat.config(text="Gubru")
				if etoile.nombreUsine==None:
					self.labelDestinationManuResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationManuResultat.config(text=etoile.nombreUsine)
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelDestinationVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationVaisseauResultat.config(text=etoile.nombreVaisseau)
			else:
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelEtoileVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileVaisseauResultat.config(text=etoile.nombreVaisseau)
					
				if etoile.nombreUsine==None:
					self.labelEtoileManuResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileManuResultat.config(text=etoile.nombreUsine)
			#self.labelEtoileVaisseauResultat.config(text=etoile.nombreVaisseau)#niveau d'intelligence
			#self.labelEtoileManuResultat.config(text=etoile.nombreUsine)
			
			#self.etoileDepart=None
			#self.etoileArrivee=None
			
			
		elif etoile.typeEtoile==3 or etoile.typeEtoile==7:
			self.labelEtoileProprioResultat.config(text= "Czin")
			if self.etoileDepart !=None:#verifier si on a clicker sur une etoile humaine en premier
				self.etoileArrivee=etoile
				self.parent.Humain.deplacementFlotte(self.etoileDepart,self.etoileArrivee,self.sliderDeplacement.get())
				self.labelDestinationProprioResultat.config(text="Czin")
				if etoile.nombreUsine==None:
					self.labelDestinationManuResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationManuResultat.config(text=etoile.nombreUsine)
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelDestinationVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationVaisseauResultat.config(text=etoile.nombreVaisseau)
			else:
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelEtoileVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileVaisseauResultat.config(text=etoile.nombreVaisseau)
				
				if etoile.nombreUsine==None:
					self.labelEtoileManuResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileManuResultat.config(text=etoile.nombreUsine)
			
			#self.etoileDepart=None
			#self.etoileArrivee=None
			
			
		elif etoile.typeEtoile==4:
			self.labelEtoileProprioResultat.config(text= "Ind\xE9pendant")
			if self.etoileDepart !=None:#verifier si on a clicker sur une etoile humaine en premier
				self.etoileArrivee=etoile
				self.parent.Humain.deplacementFlotte(self.etoileDepart,self.etoileArrivee,self.sliderDeplacement.get())
				self.labelDestinationProprioResultat.config(text="Ind\xE9pendant")
				if etoile.nombreUsine==None:
					self.labelDestinationManuResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationManuResultat.config(text=etoile.nombreUsine)
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelDestinationVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationVaisseauResultat.config(text=etoile.nombreVaisseau)
			else:
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelEtoileVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileVaisseauResultat.config(text=etoile.nombreVaisseau)
					
				if etoile.nombreUsine==None:
					self.labelEtoileManuResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileManuResultat.config(text=etoile.nombreUsine)
			
	
			
		#frame = Frame(root, width=100, height=100)
		#frame.bind("<Button-1>", callback)
		#frame.pack()
		
	def initOption(self):
		self.canevas=Canvas(self.root,width=800,height=600,bg="white")
		
		self.background=Image.open("background.jpg")#Agrandir selon la fenetre
		self.background_images=ImageTk.PhotoImage(self.background)
		self.background_label = Label(self.canevas, image=self.background_images)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		
		
		self.logoGalax = Image.open("logo.jpg") 
		self.photoGalax = ImageTk.PhotoImage(self.logoGalax)
		self.labelLogo = Label(self.canevas,image=self.photoGalax)
		self.labelLogo.pack()
		
		labelDifficulte=Label(self.canevas,text="Difficult\xE9e",relief=SOLID,width=15)
		labelDifficulte.pack(padx=5,side=LEFT)
		labelFacile=Label(self.canevas,text="Facile",relief=GROOVE,width=15)#remplacer par un boutton
		labelFacile.pack(padx=1,side=LEFT)
		labelIntermediaire=Label(self.canevas,text="Interm\xE9diaire",relief=GROOVE,width=15)#remplacer par un boutton
		labelIntermediaire.pack(padx=1,side=LEFT)
		labelDifficile=Label(self.canevas,text="Difficile",relief=GROOVE,width=15)#remplacer par un boutton
		labelDifficile.pack(padx=1,side=LEFT)
		
		b=Button(self.canevas,text="Quitter",width=15,command=self.initFermer)
		b.pack()
		b1=Button(self.canevas,text="Menu Principal",width=15,command=self.initMenu)
		b1.pack()
		
		self.cadreLobby.pack_forget()
		self.canevas.pack()
		
	def initHighScore(self):
		self.cadrePartieHighScore=Frame(self.root)

		self.background=Image.open("background.jpg")#Agrandir selon la fenetre
		self.background_images=ImageTk.PhotoImage(self.background)
		self.background_label = Label(self.cadrePartieHighScore, image=self.background_images)
		self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
		
		self.logoGalax = Image.open("logo.jpg") 
		self.photoGalax = ImageTk.PhotoImage(self.logoGalax)
		self.labelLogo = Label(self.cadrePartieHighScore,image=self.photoGalax)
		self.labelLogo.grid(column=0,row=0,columnspan=2)
		#self.canevas.grid(column=0,row=0,columnspan=2)
		

		
		labelTitre=Label(self.cadrePartieHighScore,text="HIGHSCORE",bg="red",width=20)
		labelTitre.grid(column=0,row=1,columnspan=2)
		
		labelNom=Label(self.cadrePartieHighScore,text="NOM",bg="blue",fg="white",relief=SOLID,width=18)
		labelNom.grid(column=0,row=2,pady=8)
		
		for i in range (0,5):
			labelNomScore=Label(self.cadrePartieHighScore,text="NOM D'UN JOUEUR",relief=GROOVE,width=18)#inserer la fonction pour les noms
			labelNomScore.grid(column=0,row=3+i)
			
		labelHighScore=Label(self.cadrePartieHighScore,text="SCORE",bg="blue",fg="white",relief=SOLID,width=18)
		labelHighScore.grid(column=1,row=2,pady=8)
		
		for i in range (0,5):
			labelScore=Label(self.cadrePartieHighScore,text="SCORE DU JOUEUR",relief=GROOVE,width=18)#inserer la fonction pour les scores
			labelScore.grid(column=1,row=3+i)
			
		b=Button(self.cadrePartieHighScore,text="Quitter",width=15,command=self.initFermer)
		b.grid(column=0,row=9,columnspan=2)
		b1=Button(self.cadrePartieHighScore,text="Menu Principal",width=15,command=self.initMenu)
		b1.grid(column=0,row=10,columnspan=2)
		
		self.cadreLobby.pack_forget()
		self.cadrePartieHighScore.pack()

	def initFermer(self):
		self.root.destroy()
		
	def initMenu(self):#Petit bug pour le retour au menu principal
		
		try:
			self.cadrePartieHighScore.pack_forget()
			self.labelLogo.pack_forget()
		except:
			try:
				self.canevas.pack_forget()
			except:
				pass #si on a pas packer highscore...
	
		self.cadreLobby.pack()
		#self.initLobby()
		
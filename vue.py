#Francois Genest
#Julien Metivier
#Mathias Perreault-Guimond

from tkinter import *
import math
from PIL import Image, ImageTk 


class Vue():
	def __init__(self, parent):
		self.parent = parent
		self.root=Tk()
		self.root.iconbitmap(default='iconhumain.ico')
		self.root.wm_title("GALAX")
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
		
		b1=Button(self.cadreLobby,text="Commencer partie",width=15,command=self.initPartie)
		b1.pack()
		b2=Button(self.cadreLobby,text="Options",width=15,command=self.initOption)
		b2.pack()
		b3=Button(self.cadreLobby,text="Quitter",width=15,command=self.initFermer)
		b3.pack()

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
		
		labelEtoile=Label(self.cadreInfo,text="\xC9toiles",relief=SOLID,width=15)
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
		self.labelHumainResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
		self.labelHumainResultat.grid(column=1,row=2)
		self.labelGubruResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
		self.labelGubruResultat.grid(column=1,row=3)
		self.labelCzinResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
		self.labelCzinResultat.grid(column=1,row=4)
		self.labelIndepResultat=Label(self.cadreInfo,text="",relief=GROOVE,width=15)
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
		self.labelDistanceEtoile = Label(self.cadreInfo,text="",width=50)
		self.labelDistanceEtoile.grid(column=0,row=14)
		
		self.labelNbFlottes = Label(self.cadreCommande, text= "Flotte(s) en d\xE9placement  : 0")
		self.labelNbFlottes.pack()
		
		self.canevas.bind("<Button-1>", self.clickCanevas)
		self.labelTemps = Label(self.cadreCommande,text=self.parent.getTemps(),relief=GROOVE,width=15)
		self.labelTemps.pack()
		
		
		
		self.b1=Button(self.cadreFlotte,text="Faire D\xE9placement", command= self.deplacementHumain)
		self.b1.pack()
		self.b2=Button(self.cadreCommande,text="Prochain Tour",width=12, command= self.prochainTour)
		self.b2.pack()
		self.b3=Button(self.cadreCommande,text="Quitter",width=12,command=self.initFermer)
		self.b3.pack()
		
		
		self.updateEtoile()
		
		self.cadreLobby.pack_forget()
		self.cadrePartie.pack()
		
	def deplacementHumain(self):
		if self.etoileDepart != None and self.etoileArrivee != None:
			self.parent.deplacementHumain(self.parent.getEtoile(self.etoileDepart.posX,self.etoileDepart.posY) ,self.parent.getEtoile(self.etoileArrivee.posX,self.etoileArrivee.posY),self.sliderDeplacement.get())
			self.labelEtoileVaisseauResultat.config(text=self.etoileDepart.nombreVaisseau)
			self.sliderDeplacement.config(to=self.etoileDepart.nombreVaisseau)
			self.updateEtoile()
			self.labelDistanceEtoile.config(text="")
			
	def prochainTour(self):
		self.parent.changementTour()	
		self.labelTemps.config(text=self.parent.getTemps())
		self.updateEtoile()
		
	def updateNombrePlaneteVisiter(self):
		nombrePlaneteVisiter = 0
		for etoile in self.parent.getListeEtoile():
			if etoile.IntelligenceHumain != 1:
				nombrePlaneteVisiter += 1
				
		return nombrePlaneteVisiter
		
	def trouverImageInit(self,etoile):
		if etoile.typeEtoile == 2 or etoile.typeEtoile == 6:
			image = Image.open("etoile_gubru.jpg")
		elif etoile.typeEtoile == 1 or etoile.typeEtoile == 5:
			image = Image.open("etoile_humain.jpg")
		elif etoile.typeEtoile == 3 or etoile.typeEtoile == 7:
			image = Image.open("etoile_czin.jpg")
		elif etoile.typeEtoile == 4:
			image = Image.open("etoile_ind.jpg")
		
		return image
	
	def updateEtoile(self):
		try:
			self.canevas.delete("etoile")
		except:
			pass
		self.compteur = 0
		self.photo = []
		for etoile in self.parent.getListeEtoile():
			if etoile.typeEtoile == 2 or etoile.typeEtoile == 6:
				image = Image.open("etoile_gubru.jpg")
			elif etoile.typeEtoile == 1 or etoile.typeEtoile == 5:
				image = Image.open("etoile_humain.jpg")
			elif etoile.typeEtoile == 3 or etoile.typeEtoile == 7:
				image = Image.open("etoile_czin.jpg")
			elif etoile.typeEtoile == 4:
				image = Image.open("etoile_ind.jpg")
			self.photo.append(ImageTk.PhotoImage(image))
			self.canevas.create_image(etoile.posX*(800/self.parent.getGrandeurJeuX())+20,etoile.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
			self.compteur += 1
			
		if self.updateNombrePlaneteVisiter() >= 10:
			self.labelHumainResultat.config(text= len(self.parent.getFlottesHumaines()))
			self.labelGubruResultat.config(text = len(self.parent.getFlottesGubru()))
			self.labelCzinResultat.config(text = len(self.parent.getFlottesCzin()))
		self.labelEtoileProprioResultat.config(text="")
		self.labelEtoileVaisseauResultat.config(text="")
		self.labelEtoileManuResultat.config(text="")
		self.labelDestinationProprioResultat.config(text="")
		self.labelDestinationManuResultat.config(text="")
		self.labelDestinationVaisseauResultat.config(text="")
		texteNbFlottes = "Flotte(s) en d\xE9placement  : " + str(len(self.parent.getFlottesHumaines())) 
		self.labelNbFlottes.config(text = texteNbFlottes)
		
		self.etoileDepart = None
		self.etoileArrivee = None
	
	def clickCanevas(self,event):
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
			self.updateEtoile()
			self.labelDistanceEtoile.config(text="")
		elif etoile.typeEtoile==1 or etoile.typeEtoile==5:
			if self.etoileDepart == None:
				self.etoileDepart=etoile
				image = Image.open("etoile_humain2.jpg")
				self.photo.append(ImageTk.PhotoImage(image))
				self.canevas.create_image(etoile.posX*(800/self.parent.getGrandeurJeuX())+20,etoile.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
				self.compteur += 1
				
				self.sliderDeplacement.config(to=etoile.nombreVaisseau)
				self.labelEtoileProprioResultat.config(text= "Humain")
				self.labelEtoileVaisseauResultat.config(text=etoile.nombreVaisseau)
				self.labelEtoileManuResultat.config(text=etoile.nombreUsine)
			else:
				if etoile != self.etoileDepart:
					if(self.etoileArrivee != None):
						image = self.trouverImageInit(self.etoileArrivee)
						self.photo.append(ImageTk.PhotoImage(image))
						self.canevas.create_image(self.etoileArrivee.posX*(800/self.parent.getGrandeurJeuX())+20,self.etoileArrivee.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
						self.compteur += 1
					self.etoileArrivee = etoile
					image = Image.open("etoile_humain3.jpg")
					self.photo.append(ImageTk.PhotoImage(image))
					self.canevas.create_image(etoile.posX*(800/self.parent.getGrandeurJeuX())+20,etoile.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
					self.compteur += 1
					
					self.labelDestinationProprioResultat.config(text= "Humain")
					self.labelDestinationVaisseauResultat.config(text=etoile.nombreVaisseau)
					self.labelDestinationManuResultat.config(text=etoile.nombreUsine)
					self.labelDistanceEtoile.config(text="Distance entre les deux \xE9toiles: " + str(self.parent.getDistance(self.etoileDepart, self.etoileArrivee)))
				
			
			if self.etoileArrivee != None:
				if self.etoileArrivee==self.etoileDepart:
					self.etoileArrivee=None

				
		elif etoile.typeEtoile==2 or etoile.typeEtoile==6 :
			if self.etoileDepart !=None:
				if(self.etoileArrivee != None):
					image = self.trouverImageInit(self.etoileArrivee)
					self.photo.append(ImageTk.PhotoImage(image))
					self.canevas.create_image(self.etoileArrivee.posX*(800/self.parent.getGrandeurJeuX())+20,self.etoileArrivee.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
					self.compteur += 1
				self.etoileArrivee=etoile
				image = Image.open("etoile_gubru3.jpg")
				self.photo.append(ImageTk.PhotoImage(image))
				self.canevas.create_image(etoile.posX*(800/self.parent.getGrandeurJeuX())+20,etoile.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
				self.compteur += 1
				self.labelDestinationProprioResultat.config(text="Gubru")
				etoile = self.parent.getInfoEtoile(self.etoileArrivee.posX, self.etoileArrivee.posY)
				if etoile.nombreUsine==None:
					self.labelDestinationManuResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationManuResultat.config(text=etoile.nombreUsine)
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelDestinationVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationVaisseauResultat.config(text=etoile.nombreVaisseau)
				self.labelDistanceEtoile.config(text="Distance entre les deux \xE9toiles: " + str(self.parent.getDistance(self.etoileDepart, self.etoileArrivee)))
			else:
				self.labelEtoileProprioResultat.config(text= "Gubru")
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelEtoileVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileVaisseauResultat.config(text=etoile.nombreVaisseau)
					
				if etoile.nombreUsine==None:
					self.labelEtoileManuResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileManuResultat.config(text=etoile.nombreUsine)
					
		elif etoile.typeEtoile==3 or etoile.typeEtoile==7:
			if self.etoileDepart !=None:
				if(self.etoileArrivee != None):
					image = self.trouverImageInit(self.etoileArrivee)
					self.photo.append(ImageTk.PhotoImage(image))
					self.canevas.create_image(self.etoileArrivee.posX*(800/self.parent.getGrandeurJeuX())+20,self.etoileArrivee.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
					self.compteur += 1
				self.etoileArrivee=etoile
				image = Image.open("etoile_czin3.jpg")
				self.photo.append(ImageTk.PhotoImage(image))
				self.canevas.create_image(etoile.posX*(800/self.parent.getGrandeurJeuX())+20,etoile.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
				self.compteur += 1
				self.labelDestinationProprioResultat.config(text="Czin")
				etoile = self.parent.getInfoEtoile(self.etoileArrivee.posX, self.etoileArrivee.posY)
				if etoile.nombreUsine==None:
					self.labelDestinationManuResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationManuResultat.config(text=etoile.nombreUsine)
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelDestinationVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationVaisseauResultat.config(text=etoile.nombreVaisseau)
				self.labelDistanceEtoile.config(text="Distance entre les deux \xE9toiles: " + str(self.parent.getDistance(self.etoileDepart, self.etoileArrivee)))
			else:
				self.labelEtoileProprioResultat.config(text= "Czin")
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelEtoileVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileVaisseauResultat.config(text=etoile.nombreVaisseau)
				
				if etoile.nombreUsine==None:
					self.labelEtoileManuResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileManuResultat.config(text=etoile.nombreUsine)
			
		elif etoile.typeEtoile==4:
			if self.etoileDepart !=None:
				if(self.etoileArrivee != None):
					image = self.trouverImageInit(self.etoileArrivee)
					self.photo.append(ImageTk.PhotoImage(image))
					self.canevas.create_image(self.etoileArrivee.posX*(800/self.parent.getGrandeurJeuX())+20,self.etoileArrivee.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
					self.compteur += 1
				self.etoileArrivee=etoile
				image = Image.open("etoile_ind3.jpg")
				self.photo.append(ImageTk.PhotoImage(image))
				self.canevas.create_image(etoile.posX*(800/self.parent.getGrandeurJeuX())+20,etoile.posY*(800/self.parent.getGrandeurJeuY())+20, image=self.photo[self.compteur], tags="etoile")
				self.compteur += 1
				self.labelDestinationProprioResultat.config(text="Ind\xE9pendant")
				etoile = self.parent.getInfoEtoile(self.etoileArrivee.posX, self.etoileArrivee.posY)
				if etoile.nombreUsine==None:
					self.labelDestinationManuResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationManuResultat.config(text=etoile.nombreUsine)
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelDestinationVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelDestinationVaisseauResultat.config(text=etoile.nombreVaisseau)
				self.labelDistanceEtoile.config(text="Distance entre les deux \xE9toiles: " + str(self.parent.getDistance(self.etoileDepart, self.etoileArrivee)))
			else:
				self.labelEtoileProprioResultat.config(text= "Ind\xE9pendant")
				if etoile.nombreVaisseau==None or etoile.nombreVaisseau==0:
					self.labelEtoileVaisseauResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileVaisseauResultat.config(text=etoile.nombreVaisseau)
					
				if etoile.nombreUsine==None:
					self.labelEtoileManuResultat.config(text="Aucune Info.")
				else:
					self.labelEtoileManuResultat.config(text=etoile.nombreUsine)
		
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
		
		self.labelDifficulte=Label(self.canevas,text="Difficult\xE9 ",relief=SOLID,width=20,height=2)
		self.labelDifficulte.pack(padx=5,side=LEFT)
		self.updateLabelDifficulte()
		b1=Button(self.canevas,text="Facile",relief=GROOVE,width=15, command=self.changerDifficulteFacile)
		b1.pack(padx=1,side=LEFT)
		b2=Button(self.canevas,text="Interm\xE9diaire",relief=GROOVE,width=15, command = self.changerDifficulteInter)
		b2.pack(padx=1,side=LEFT)
		b3=Button(self.canevas,text="Difficile",relief=GROOVE,width=15, command = self.changerDifficulteDifficile)
		b3.pack(padx=1,side=LEFT)
		b4=Button(self.canevas,text="Quitter",width=15,command=self.initFermer)
		b4.pack()
		b5=Button(self.canevas,text="Menu Principal",width=15,command=self.initMenu)
		b5.pack()
		
		self.cadreLobby.pack_forget()
		self.canevas.pack()
	
	def updateLabelDifficulte(self):
		if self.parent.getDifficulte() == 1:
			self.labelDifficulte.config(text="Difficult\xE9: Facile")
		elif self.parent.getDifficulte() == 2:
			self.labelDifficulte.config(text="Difficult\xE9: Interm\xE9diaire")
		elif self.parent.getDifficulte() == 3:
			self.labelDifficulte.config(text="Difficult\xE9: Difficile")
	
	def changerDifficulteFacile(self):
		self.parent.changerDifficulteFacile()
		self.updateLabelDifficulte()
		
	def changerDifficulteInter(self): 
		self.parent.changerDifficulteInter()
		self.updateLabelDifficulte()
		
	def changerDifficulteDifficile(self):
		self.parent.changerDifficulteDifficile()
		self.updateLabelDifficulte()
		
	def initFermer(self):
		self.root.destroy()
		
	def initMenu(self):
		try:
			self.canevas.pack_forget()
		except:
			pass
		try:
			self.popUp.destroy()
		except:
			pass
		try:
			self.cadrePartie.pack_forget()
		except:
			pass	
		self.initLobby()
		
	def finPartie(self, humainGagnant):
		self.popUp = Toplevel(self.root)
		if humainGagnant == True:
			Label(self.popUp, text="Fin de la partie ! Vous avez gagne !", padx = 250, pady= 15).pack()
		else:
			Label(self.popUp, text="Fin de la partie ! Vous avez perdu !", padx = 250, pady= 15).pack()
		self.b1.destroy()
		self.b2.destroy()
		self.b3.destroy()
		Button(self.popUp, text="Retour menu", command=self.initMenu).pack()
		
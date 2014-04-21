from tkinter import *

class Vue():
    def __init__(self, parent):
        self.parent = parent
        self.root=Tk()
        self.initLobby()
    def initLobby(self):
        self.cadreLobby=Frame(self.root)
        labelTitre=Label(self.cadreLobby,text="GALAX",bg="red",width=20)
        labelTitre.pack()
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
        self.cadrePartie=Frame(self.root)
        self.cadreJeu=Frame(self.cadrePartie)
        self.cadreFlotte=Frame(self.cadrePartie)
        self.cadreInfo=Frame(self.cadrePartie)
        self.cadreCommande=Frame(self.cadrePartie)
        self.cadreInfoResultat=Frame(self.cadrePartie)
        self.cadreJeu.grid(column=0,row=0)
        self.cadreFlotte.grid(column=0,row=1)
        self.cadreInfo.grid(column=1,row=0)
        self.cadreInfoResultat.grid(column=2,row=0)#appelle des functions pour resultat 
        self.cadreCommande.grid(column=1,row=1)
        self.canevas=Canvas(self.cadreJeu,width=800,height=600,bg="white")
        self.canevas.pack()
        
        SliderDeplacement = Scale(self.cadreFlotte,orient=HORIZONTAL,length=400,width=20,sliderlength=10,from_=0,to=500)
        SliderDeplacement.pack()
           
        labelInfo=Label(self.cadreInfo,text="Informations",relief=SOLID,width=15)
        labelInfo.pack(pady=16)
        labelHumain=Label(self.cadreInfo,text="Humain",relief=GROOVE,width=15)
        labelHumain.pack()
        labelGubru=Label(self.cadreInfo,text="Gubru",relief=GROOVE,width=15)
        labelGubru.pack()
        labelCzin=Label(self.cadreInfo,text="Czin",relief=GROOVE,width=15)
        labelCzin.pack()
        labelIndep=Label(self.cadreInfo,text="Ind\xE9pendant",relief=GROOVE,width=15)
        labelIndep.pack()
        
        labelEtoile=Label(self.cadreInfo,text="Etoiles",relief=SOLID,width=15)
        labelEtoile.pack(pady=16)
        labelProprio=Label(self.cadreInfo,text="Propri\xE9taire",relief=GROOVE,width=15)
        labelProprio.pack()
        labelVaisseau=Label(self.cadreInfo,text="Nb Vaisseau(x)",relief=GROOVE,width=15)
        labelVaisseau.pack()
        labelManu=Label(self.cadreInfo,text="Nb Manufacture(s)",relief=GROOVE,width=15)
        labelManu.pack()
        
        labelDestination=Label(self.cadreInfo,text="Destination",relief=SOLID,width=15)
        labelDestination.pack(pady=16)
        labelProprio=Label(self.cadreInfo,text="Propri\xE9taire",relief=GROOVE,width=15)
        labelProprio.pack()
        labelVaisseau=Label(self.cadreInfo,text="Nb Vaisseau(x)",relief=GROOVE,width=15)
        labelVaisseau.pack()
        labelManu=Label(self.cadreInfo,text="Nb Manufacture(s)",relief=GROOVE,width=15)
        labelManu.pack()
        
        
        labelInfoResultat=Label(self.cadreInfoResultat)
        labelInfoResultat.pack(pady=16)
        labelHumainResultat=Label(self.cadreInfoResultat,text="45",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelHumainResultat.pack()
        labelGubruResultat=Label(self.cadreInfoResultat,text="22",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelGubruResultat.pack()
        labelCzinResultat=Label(self.cadreInfoResultat,text="35",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelCzinResultat.pack()
        labelIndepResultat=Label(self.cadreInfoResultat,text="0",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelIndepResultat.pack()
        
        labelEtoileResultat=Label(self.cadreInfoResultat)
        labelEtoileResultat.pack(pady=16)
        labelProprioResultat=Label(self.cadreInfoResultat,text="42",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelProprioResultat.pack()
        labelVaisseauResultat=Label(self.cadreInfoResultat,text="15",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelVaisseauResultat.pack()
        labelManuResultat=Label(self.cadreInfoResultat,text="1",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelManuResultat.pack()
        
        labelDestinationResultat=Label(self.cadreInfoResultat)
        labelDestinationResultat.pack(pady=16)
        labelProprioResultat=Label(self.cadreInfoResultat,text="42",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelProprioResultat.pack()
        labelVaisseauResultat=Label(self.cadreInfoResultat,text="15",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelVaisseauResultat.pack()
        labelManuResultat=Label(self.cadreInfoResultat,text="1",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelManuResultat.pack()
        
        
        
        b1=Button(self.cadreFlotte,text="Faire D\xE9placement")
        b1.pack()
        
        b2=Button(self.cadreCommande,text="Prochain Tour",width=12)
        b2.pack()
        b3=Button(self.cadreCommande,text="Quitter",width=12,command=self.initFermer)
        b3.pack()
        
        self.parent.commencerPartie()
        tabloJeu=[]
        for i in self.parent.getListeEtoile():#problem ici pour faire apparaitre les etoiles dans le canvas
            tabloJeu[i.posX][i.posY]=labelEtoileJeu=Label(self.canevas,text="*")
            labelEtoileJeu.pack()#A FAIRE : Afficher selon le x et y des etoiles dans liste etoile
        
        self.cadreLobby.pack_forget()
        self.cadrePartie.pack()
        
        
       

        
    #def callback(event):    capturing click in a window
        #print "clicked at", event.x, event.y
        #frame = Frame(root, width=100, height=100)
        #frame.bind("<Button-1>", callback)
        #frame.pack()
        
    def initOption(self):
        self.canevas=Canvas(self.root,width=800,height=600,bg="white")
        
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
        
        self.cadreLobby.pack_forget()
        self.canevas.pack()
        
    def initHighScore(self):
        self.cadrePartieHighScore=Frame(self.root)
        self.cadreHighScore=Frame(self.cadrePartieHighScore)
        self.cadreNom=Frame(self.cadrePartieHighScore)
        self.cadreTitre=Frame(self.cadrePartieHighScore)
        self.cadreQuitter=Frame(self.cadrePartieHighScore)
        self.cadreTitre.grid(column=1,row=0)
        self.cadreNom.grid(column=0,row=1)
        self.cadreHighScore.grid(column=2,row=1)
        self.cadreQuitter.grid(column=1,row=2)
        self.canevas=Canvas(self.cadreTitre,width=800,height=600,bg="white")
        self.canevas.pack()

        
        labelTitre=Label(self.canevas,text="HIGHSCORE",bg="red",width=20)
        labelTitre.pack()
        
        labelNom=Label(self.cadreNom,text="NOM",bg="blue",fg="white",relief=SOLID,width=12)
        labelNom.pack(pady=8)
        
        for i in range (0,5):
            labelNomScore=Label(self.cadreNom,text="NOM D'UN JOUEUR",relief=GROOVE,width=12)#inserer la fonction pour les noms
            labelNomScore.pack()
            
        labelHighScore=Label(self.cadreHighScore,text="SCORE",bg="blue",fg="white",relief=SOLID,width=12)
        labelHighScore.pack(pady=8)
        
        for i in range (0,5):
            labelScore=Label(self.cadreHighScore,text="SCORE DU JOUEUR",relief=GROOVE,width=12)#inserer la fonction pour les scores
            labelScore.pack()
            
        b=Button(self.cadreQuitter,text="Quitter",width=15,command=self.initFermer)
        b.pack()
        
        self.cadreLobby.pack_forget()
        self.cadrePartieHighScore.pack()

    def initFermer(self):
        self.root.destroy()
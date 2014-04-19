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
        b2=Button(self.cadreLobby,text="Options",width=15)
        b2.pack()
        b3=Button(self.cadreLobby,text="HighScore",width=15)
        b3.pack()
        b4=Button(self.cadreLobby,text="Quitter",width=15)
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
        labelInfo.pack(pady=8)
        labelHumain=Label(self.cadreInfo,text="Humain",relief=GROOVE,width=15)
        labelHumain.pack()
        labelGubru=Label(self.cadreInfo,text="Gubru",relief=GROOVE,width=15)
        labelGubru.pack()
        labelCzin=Label(self.cadreInfo,text="Czin",relief=GROOVE,width=15)
        labelCzin.pack()
        labelIndep=Label(self.cadreInfo,text="Ind\xE9pendant",relief=GROOVE,width=15)
        labelIndep.pack()
        
        
        labelHumain=Label(self.cadreInfo)
        labelHumain.pack(pady=8)
        
        labelHumainResultat=Label(self.cadreInfoResultat,text="45",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelHumainResultat.pack()
        labelGubruResultat=Label(self.cadreInfoResultat,text="22",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelGubruResultat.pack()
        labelCzinResultat=Label(self.cadreInfoResultat,text="35",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelCzinResultat.pack()
        labelIndepResultat=Label(self.cadreInfoResultat,text="0",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelIndepResultat.pack()
        
        labelEtoile=Label(self.cadreInfo,text="Etoiles",relief=SOLID,width=15)
        labelEtoile.pack(pady=8)
        labelProprio=Label(self.cadreInfo,text="Propri\xE9taire",relief=GROOVE,width=15)
        labelProprio.pack()
        labelVaisseau=Label(self.cadreInfo,text="Nb Vaisseau(x)",relief=GROOVE,width=15)
        labelVaisseau.pack()
        labelManu=Label(self.cadreInfo,text="Nb Manufacture(s)",relief=GROOVE,width=15)
        labelManu.pack()
        
        
        labelHumain=Label(self.cadreInfo)
        labelHumain.pack(pady=8)
        
        labelEtoileResultat=Label(self.cadreInfoResultat)#changer text pour les fonctions qui montre le resultat
        labelEtoileResultat.pack()
        labelProprioResultat=Label(self.cadreInfoResultat,text="42",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelProprioResultat.pack()
        labelVaisseauResultat=Label(self.cadreInfoResultat,text="15",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelVaisseauResultat.pack()
        labelManuResultat=Label(self.cadreInfoResultat,text="1",relief=GROOVE,width=15)#changer text pour les fonctions qui montre le resultat
        labelManuResultat.pack()
        
        labelDestination=Label(self.cadreInfo,text="Destination",relief=SOLID,width=15)
        labelDestination.pack(pady=8)
        labelProprio=Label(self.cadreInfo,text="Propri\xE9taire",relief=GROOVE,width=15)
        labelProprio.pack()
        labelVaisseau=Label(self.cadreInfo,text="Nb Vaisseau(x)",relief=GROOVE,width=15)
        labelVaisseau.pack()
        labelManu=Label(self.cadreInfo,text="Nb Manufacture(s)",relief=GROOVE,width=15)
        labelManu.pack()
        
        labelHumain=Label(self.cadreInfo)
        labelHumain.pack(pady=8)
        
        labelHumain=Label(self.cadreInfo)
        labelHumain.pack(pady=8)
        labelDestinationResultat=Label(self.cadreInfoResultat)#changer text pour les fonctions qui montre le resultat
        labelDestinationResultat.pack()
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
        b3=Button(self.cadreCommande,text="Quitter",width=12)
        b3.pack()
        
        self.cadreLobby.pack_forget()
        self.cadrePartie.pack()
        
    
    #def callback(event):    capturing click in a window
        #print "clicked at", event.x, event.y
        #frame = Frame(root, width=100, height=100)
        #frame.bind("<Button-1>", callback)
        #frame.pack()
        

class Execution():
    def __init__(self):
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
if __name__=='__main__':
    e=Execution()
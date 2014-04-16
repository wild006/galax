from tkinter import *

class Vue():
    def __init__(self, parent):
        self.parent = parent
        self.root=Tk()
        self.initLobby()
    def initLobby(self):
        self.cadreLobby=Frame(self.root)
        labelTitre=Label(self.cadreLobby,text="GALAX",bg="red")
        labelTitre.pack()
        b1=Button(self.cadreLobby,text="Commencer partie",command=self.initPartie)#Besion de fonction pour sizer
        b1.pack()
        b1=Button(self.cadreLobby,text="         Options         ")#Besion de fonction pour sizer
        b1.pack()
        b1=Button(self.cadreLobby,text="       HighScore       ")#Besion de fonction pour sizer
        b1.pack()
        b1=Button(self.cadreLobby,text="         Quitter          ")#Besion de fonction pour sizer
        b1.pack()
        self.cadreLobby.pack()
        
        
    def initPartie(self):
        self.cadrePartie=Frame(self.root)
        self.cadreJeu=Frame(self.cadrePartie)
        self.cadreFlotte=Frame(self.cadrePartie)
        self.cadreInfo=Frame(self.cadrePartie)
        self.cadreCommande=Frame(self.cadrePartie)
        self.cadreJeu.grid(column=0,row=0)
        self.cadreFlotte.grid(column=0,row=1)
        self.cadreInfo.grid(column=1,row=0)
        self.cadreCommande.grid(column=1,row=1)
        self.canevas=Canvas(self.cadreJeu,width=800,height=600,bg="white")
        self.canevas.pack()
        b=Button(self.cadreCommande,text="Quitter")
        b.pack()
        self.cadreLobby.pack_forget()
        self.cadrePartie.pack()
        
    
    #def callback(event):    capturing click in a window
        #print "clicked at", event.x, event.y
        #frame = Frame(root, width=100, height=100)
        #frame.bind("<Button-1>", callback)
        #frame.pack()
        
        
        #grid layout introduction to tkinter p.34
class Execution():
    def __init__(self):
        self.vue=Vue(self)
        self.vue.root.mainloop()
        
if __name__=='__main__':
    e=Execution()
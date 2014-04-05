from modele import *
from vue import *

class Controleur():
    def __init__(self):
        self.m = Modele(self)
        self.v = Vue(self)

#----Main----

if __name__ == '__main__':
    c = Controleur()
"""
Creare una classe chiamata Animale che deve avere le properties:
specie, zampe, coda
E il metodo:
verso
Il metodo verso fa il print del verso dell'animale

A vostra scelta creare 2 classi derivate da Animale (cane, gatto)
che gestirà le properties e i metodi dell'animale specifico 
"""

class Animale:
    def __init__(self, specie, coda, zampe):
        self.specie = specie
        self.coda = coda
        self.zampe = zampe
    
    def verso():
        return "Questo è il verso"
    
class Cane(Animale):
    def __init__(self, coda, zampe):
        super().__init__("cane", coda, zampe)
        
    def verso(self):
        return "Bau Bau"
    
class Gatto(Animale):
    def __init__(self, coda, zampe):
        super().__init__("gatto", coda, zampe)
        
    def verso(self):
        return "Miao Miao"
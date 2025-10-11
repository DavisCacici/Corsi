"""
Create una classe per gestire i file avendo:
una property 'path' che viene inizializzata nel costruttore;
3 metodi per la lettura (read), per la scrittura (write) e per l'aggiornamento (update) 
"""

class HandleFile:
    def __init__(self, path):
        self.path = path
    
    def read(self):
        result = ""
        with open(self.path, "rt") as file:
            result = file.read()
        return result
    
    def write(self, text):
        with open(self.path, "wt") as file:
            file.write(text)
    
    def update(self, text):
        with open(self.path, "at") as file:
            file.write(text)
        
#--------------------------------------------------------------------------
file = HandleFile("C:\\_SORGENTI\\Corsi\\BigData\\Class_Object\\test.txt")

file.update("Questo è un test")
print(file.read())
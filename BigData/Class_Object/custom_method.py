"""
You can create your own methods inside objects. 
Methods in objects are functions that belong to the object.
Let us create a method in the Person class

The self parameter is a reference to the current instance of the class, a
nd is used to access variables that belong to the class.

It does not have to be named self, you can call it whatever you like, 
but it has to be the first parameter of any function in the class
"""

class Person:
    def __init__(self, name, surname):
        self.nome = name
        self.cognome = surname
    def __str__(self):
        return f"{self.nome} {self.cognome}"
    
    def salutare(self):
        return f"Piacere di conoscerti {self.nome}"
    
    def stampa_saluti(self):
        print(self.salutare())

persona = Person("Stefano", "Rossi")
print(persona.salutare())
persona.stampa_saluti()

# Modify property
persona.cognome = "Pingo"
print(persona.cognome)
# You can delete objects by using the del keyword:
del persona
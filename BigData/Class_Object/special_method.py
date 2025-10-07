"""
The __str__() method controls what should be returned 
when the class object is represented as a string.

If the __str__() method is not set, 
    the string representation of the object is returned:
"""

class Person:
    def __init__(self, name, surname):
        self.nome = name
        self.cognome = surname
    def __str__(self):
        return f"{self.nome} {self.cognome}"

persona = Person("Stefano", "Rossi")
print(persona)
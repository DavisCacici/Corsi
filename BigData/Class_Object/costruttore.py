"""
The examples above are classes and objects in their simplest form, 
and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() method.

All classes have a method called __init__(), 
which is always executed when the class is being initiated.

Use the __init__() method to assign values to object properties, 
or other operations that are necessary to do when the object is being created
"""

class Person:
    def __init__(self, name, surname):
        self.nome = name
        self.cognome = surname
        
persona = Person("Mario", "Rossi")
persona.nome = 'Stefano'
persona2 = Person("Marco", "Rossi")
persona3 = Person("Marco", "Versi")
print(persona.nome, persona.cognome)
print(persona2.nome, persona2.cognome)
print(persona3.nome, persona3.cognome)